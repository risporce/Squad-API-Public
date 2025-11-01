from os import urandom
from hashlib import blake2b
from nacl.public import PrivateKey, PublicKey, Box
from nacl.secret import SecretBox
from nacl.utils import random
from Packets.PacketsEnum import LogicSquadPackets

class Nonce:
    def __init__(self, nonce=None, clientKey=None, serverKey=None):
        if not clientKey:
            if nonce:
                self._nonce = nonce
            else:
                self._nonce = urandom(24)
        else:
            b2 = blake2b(digest_size=24)
            if nonce:
                b2.update(bytes(nonce))
            b2.update(bytes(clientKey))
            b2.update(bytes(serverKey))
            self._nonce = b2.digest()

    def __bytes__(self):
        return self._nonce
    def __len__(self):
        return len(self._nonce)
    def increment(self):
        self._nonce = (int.from_bytes(self._nonce, 'little') + 2).to_bytes(24, 'little')


class Crypto:
    def __init__(self, spk):
        self.server_private_key = None
        self.shared_encryption_key = PrivateKey.generate()
        self.server_public_key = PublicKey(bytes.fromhex(spk))
        self.client_public_key = self.shared_encryption_key.public_key
        self.session_key = None
        self.decryptNonce = Nonce()
        self.encryptNonce = None
        self.nonce = Nonce(clientKey=self.client_public_key, serverKey=self.server_public_key)
        self.box = Box(self.shared_encryption_key, self.server_public_key)
        self.s = bytearray(32)
        self.k = None

        self.attestation_token = None

    def encryptClient(self, packet_id, payload):
        if packet_id == LogicSquadPackets.CLIENT_HELLO_MESSAGE.value:
            return payload
        elif packet_id == LogicSquadPackets.LOGIN_MESSAGE.value:
            if not self.attestation_token:
                payload = self.session_key + bytes(self.decryptNonce) + payload
                encrypted = self.box.encrypt(payload, bytes(self.nonce))
                return self.client_public_key.encode() + encrypted.ciphertext
            if self.attestation_token:
                payload = bytes.fromhex("50") + self.attestation_token + bytes(self.decryptNonce) + payload
                encrypted = self.box.encrypt(payload, bytes(self.nonce))
                return self.client_public_key.encode() + encrypted.ciphertext
        else:
            self.decryptNonce.increment()
            box = SecretBox(bytes(self.k))
            encrypted = box.encrypt(bytes(bytearray(payload)), bytes(self.decryptNonce)).ciphertext
            return encrypted
            
    def decryptServer(self, packet_id, payload : bytes):
        if packet_id == LogicSquadPackets.SERVER_HELLO_MESSAGE.value:
            if len(payload) == 28:
                self.session_key = payload[-24:]
                return payload
            return payload
        elif packet_id == LogicSquadPackets.LOGIN_FAILED_MESSAGE.value and not self.session_key:
            return payload
        elif packet_id in  (LogicSquadPackets.LOGIN_FAILED_MESSAGE.value, LogicSquadPackets.LOGIN_OK_MESSAGE.value):
            nonce = Nonce(self.decryptNonce.__bytes__(), self.client_public_key.encode(), self.server_public_key.encode())
            decrypted = self.box.decrypt(payload, nonce.__bytes__())
            self.encryptNonce = Nonce(nonce=decrypted[:24])
            self.k = decrypted[24:56]
            return decrypted[56:]
        else:
            self.encryptNonce.increment()
            decryptBox = SecretBox(bytes(self.k))
            return decryptBox.decrypt(bytes(bytearray(payload)), bytes(self.encryptNonce))
        