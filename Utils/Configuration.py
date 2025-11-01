# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome_from_dict(json.loads(json_string))
import json
from dataclasses import dataclass
from typing import Any, TypeVar, Type, cast
from uuid import UUID


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


# @dataclass
# class AskPlayerProfile:
#     account_high_id: int
#     account_low_id: int
#     boolean_default: bool

#     @staticmethod
#     def from_dict(obj: Any) -> 'AskPlayerProfile':
#         assert isinstance(obj, dict)
#         account_high_id = from_int(obj.get("AccountHighId"))
#         account_low_id = from_int(obj.get("AccountLowId"))
#         boolean_default = from_bool(obj.get("BooleanDefault"))
#         return AskPlayerProfile(account_high_id, account_low_id, boolean_default)

#     def to_dict(self) -> dict:
#         result: dict = {}
#         result["AccountHighId"] = from_int(self.account_high_id)
#         result["AccountLowId"] = from_int(self.account_low_id)
#         result["BooleanDefault"] = from_bool(self.boolean_default)
#         return result


@dataclass
class ClientHelloMessage:
    protocol: int
    key_version: int
    major: int
    build: int
    minor: int
    content_hash: str
    device_type: int
    app_store: int

    @staticmethod
    def from_dict(obj: Any) -> 'ClientHelloMessage':
        assert isinstance(obj, dict)
        protocol = from_int(obj.get("Protocol"))
        key_version = from_int(obj.get("KeyVersion"))
        major = from_int(obj.get("Major"))
        build = from_int(obj.get("Build"))
        minor = from_int(obj.get("Minor"))
        content_hash = from_str(obj.get("ContentHash"))
        device_type = from_int(obj.get("DeviceType"))
        app_store = from_int(obj.get("AppStore"))
        return ClientHelloMessage(protocol, key_version, major, build, minor, content_hash, device_type, app_store)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Protocol"] = from_int(self.protocol)
        result["KeyVersion"] = from_int(self.key_version)
        result["Major"] = from_int(self.major)
        result["Build"] = from_int(self.build)
        result["Minor"] = from_int(self.minor)
        result["ContentHash"] = from_str(self.content_hash)
        result["DeviceType"] = from_int(self.device_type)
        result["AppStore"] = from_int(self.app_store)
        return result


@dataclass
class LoginMessage:
    account_high_id: int
    status_account_high_id: int
    account_low_id: int
    status_account_low_id: int
    pass_token: str
    status_pass_token: str
    client_major: int
    client_build: int
    client_minor: int
    resource_sha: str
    device: str
    locales_csv_id: int
    prefered_device_language: str
    imei: UUID
    os_version: str
    is_android: bool
    is_advertising_enabled: bool
    apple_ifv: str
    rnd_key: int
    app_store: int
    client_version: str
    device_name: str
    supercell_id_token: str
    string_default: str
    int_default: int
    boolean_default: bool

    @staticmethod
    def from_dict(obj: Any) -> 'LoginMessage':
        assert isinstance(obj, dict)
        account_high_id = from_int(obj.get("AccountHighId"))
        status_account_high_id = from_int(obj.get("StatusAccountHighId"))
        account_low_id = from_int(obj.get("AccountLowId"))
        status_account_low_id = from_int(obj.get("StatusAccountLowId"))
        pass_token = from_str(obj.get("PassToken"))
        status_pass_token = from_str(obj.get("StatusPassToken"))
        client_major = from_int(obj.get("ClientMajor"))
        client_build = from_int(obj.get("ClientBuild"))
        client_minor = from_int(obj.get("ClientMinor"))
        resource_sha = from_str(obj.get("ResourceSha"))
        device = from_str(obj.get("Device"))
        locales_csv_id = from_int(obj.get("Locales_csvID"))
        prefered_device_language = from_str(obj.get("PreferedDeviceLanguage"))
        imei = UUID(obj.get("IMEI"))
        os_version = from_str(obj.get("OSVersion"))
        is_android = from_bool(obj.get("isAndroid"))
        is_advertising_enabled = from_bool(obj.get("isAdvertisingEnabled"))
        apple_ifv = from_str(obj.get("AppleIFV"))
        rnd_key = from_int(obj.get("RndKey"))
        app_store = from_int(obj.get("AppStore"))
        client_version = from_str(obj.get("ClientVersion"))
        device_name = from_str(obj.get("DeviceName"))
        supercell_id_token = from_str(obj.get("SupercellIdToken"))
        string_default = from_str(obj.get("StringDefault"))
        int_default = from_int(obj.get("IntDefault"))
        boolean_default = from_bool(obj.get("BooleanDefault"))
        return LoginMessage(account_high_id, status_account_high_id, account_low_id, status_account_low_id, pass_token, status_pass_token, client_major, client_build, client_minor, resource_sha, device, locales_csv_id, prefered_device_language, imei, os_version, is_android, is_advertising_enabled, apple_ifv, rnd_key, app_store, client_version, device_name, supercell_id_token, string_default, int_default, boolean_default)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AccountHighId"] = from_int(self.account_high_id)
        result["StatusAccountHighId"] = from_int(self.status_account_high_id)
        result["AccountLowId"] = from_int(self.account_low_id)
        result["StatusAccountLowId"] = from_int(self.status_account_low_id)
        result["PassToken"] = from_str(self.pass_token)
        result["StatusPassToken"] = from_str(self.status_pass_token)
        result["ClientMajor"] = from_int(self.client_major)
        result["ClientBuild"] = from_int(self.client_build)
        result["ClientMinor"] = from_int(self.client_minor)
        result["ResourceSha"] = from_str(self.resource_sha)
        result["Device"] = from_str(self.device)
        result["Locales_csvID"] = from_int(self.locales_csv_id)
        result["PreferedDeviceLanguage"] = from_str(self.prefered_device_language)
        result["IMEI"] = str(self.imei)
        result["OSVersion"] = from_str(self.os_version)
        result["isAndroid"] = from_bool(self.is_android)
        result["isAdvertisingEnabled"] = from_bool(self.is_advertising_enabled)
        result["AppleIFV"] = from_str(self.apple_ifv)
        result["RndKey"] = from_int(self.rnd_key)
        result["AppStore"] = from_int(self.app_store)
        result["ClientVersion"] = from_str(self.client_version)
        result["DeviceName"] = from_str(self.device_name)
        result["SupercellIdToken"] = from_str(self.supercell_id_token)
        result["StringDefault"] = from_str(self.string_default)
        result["IntDefault"] = from_int(self.int_default)
        result["BooleanDefault"] = from_bool(self.boolean_default)
        return result


@dataclass
class Server:
    server: str
    port: int
    server_public_key: str

    @staticmethod
    def from_dict(obj: Any) -> 'Server':
        assert isinstance(obj, dict)
        server = from_str(obj.get("server"))
        port = from_int(obj.get("port"))
        server_public_key = from_str(obj.get("ServerPublicKey"))
        return Server(server, port, server_public_key)

    def to_dict(self) -> dict:
        result: dict = {}
        result["server"] = from_str(self.server)
        result["port"] = from_int(self.port)
        result["ServerPublicKey"] = from_str(self.server_public_key)
        return result


@dataclass
class ClientConfigs:
    client_hello_message: ClientHelloMessage
    login_message: LoginMessage
    server: Server

    @staticmethod
    def from_dict(obj: Any) -> 'ClientConfigs':
        assert isinstance(obj, dict)
        client_hello_message = ClientHelloMessage.from_dict(obj.get("ClientHelloMessage"))
        login_message = LoginMessage.from_dict(obj.get("LoginMessage"))
        server = Server.from_dict(obj.get("Server"))
        return ClientConfigs(client_hello_message, login_message, server)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ClientHelloMessage"] = to_class(ClientHelloMessage, self.client_hello_message)
        result["LoginMessage"] = to_class(LoginMessage, self.login_message)
        result["Server"] = to_class(Server, self.server)
        return result


def client_configs_from_dict(s: Any) -> ClientConfigs:
    return ClientConfigs.from_dict(s)


def client_configs_to_dict(x: ClientConfigs) -> Any:
    return to_class(ClientConfigs, x)
