from api_client import APIClient
from api_client_status import APIClientStatus
from Files.LogicData.LogicData import LogicData
from Files.LogicData.LogicCharactersData import LogicCharacterData
from Files.LogicData.LogicResourcesData import LogicResourcesData
from Files.LogicData.LogicAvatarStatsData import LogicAvatarStatData
from Files.LogicData.LogicExpLevelsData import LogicExpLevelData
from Files.LogicData.LogicSkinsData import LogicSkinsData
from Files.LogicData.LogicSpellsData import LogicSpellsData
from Files.LogicData.LogicVariablesData import LogicVariablesData
from Files.LogicData.LogicTextsData import LogicTextsData
from Files.LogicData.LogicRegionsData import LogicRegionsData
from ClientGlobals import Configs
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_caching import Cache
from asyncio import Queue
import os
import traceback
from Packets.PacketsEnum import LogicSquadPackets
import threading
import time
from flask import Flask, render_template, request, redirect, url_for, flash
import json

time.sleep(0.5)

game_data = LogicData()
game_data.createReferences()
configs = Configs()

app = Flask('backend', template_folder='templates')
CORS(app)
BACKEND_IP = 'backend'
BACKEND_PORT = int(os.environ.get('PORT', 30000))

cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache'})

USER_ROUTE = '/user'
acc5 = {"h": 0, "l": 0, "p": ""}

accounts = [acc5]
clients : list[APIClient] = []

    
NB_CLIENTS = 8

def initialize_clients():
    global clients
    for i in range(NB_CLIENTS):
        print("intializing client")
        clients.append(APIClient(configs, game_data, accounts[0]))
        clients[i].connecting()


def reset_account_timer(): # auto resets every 30 mins, or at some point the game disconnects us automatically
    while True:
        time.sleep(1800)
        reset_account()

def reset_account():
    global clients
    for i in range(NB_CLIENTS):
        clients[i].stop()
        clients[i] = None
        clients[i] = APIClient(configs, game_data, acc5)
        clients[i].connecting()

keep_alive_thread = threading.Thread(target=(reset_account_timer), daemon=True)
keep_alive_thread.start()


current_account = 0
@app.route('/user/<user_id>', methods=['GET'])
@cache.cached(timeout=60)
def get_user(user_id):
    global clients
    global current_account
    try:
        current_account+=1
        if current_account == NB_CLIENTS:
            current_account = 0
        data = clients[current_account].send_player_profile(user_id)
        return data, 200
    except TimeoutError:
        return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': "Error"}), 500
    finally:
        clients[current_account].clear_account()

@app.route('/leaderboard', methods=['GET'])
@cache.cached(timeout=1800)
def get_leaderboard():
    global current_account
    data = {'ip': request.remote_addr}
    try:
        current_account += 1
        if current_account == NB_CLIENTS:
            current_account = 0
        data = clients[current_account].ask_player_leaderboard()
        return data, 200
    except TimeoutError:
        return jsonify({'error': 'Error fetching leaderboard'}), 404
    except Exception as e:
        return jsonify({'error': "Error"}), 500
    finally:
        clients[current_account].clear_account()

# @app.route('/localleaderboard', methods=['GET']) # not working
# @cache.cached(timeout=60)
# def get_local_leaderboard():
#     data = {'ip': request.remote_addr}
#     try:
#         data = client.ask_player_local_leaderboard()
#         return data, 200
#     except TimeoutError:
#         #client.stop()
#         return jsonify({'error': 'Error fetching leaderboard'}), 404
#     except Exception as e:
#         return jsonify({'error': "Error"}), 500
#     finally:
#         client.clear_account()
#         pass
#         #client.stop()
#         #return client.returningMessage.returning_data, 200

    
@app.route("/status", methods=['GET'])
def status():
    global current_account
    account = accounts[len(accounts) -2]
    client = APIClientStatus(configs, account)
    try:
        status_code : int = client.connect()
        return jsonify({'status': status_code}), 200
    except Exception as e:
        print(str(e))
        return jsonify({'error': "The server appear unreachable, try again later"}), 500


initialize_clients()
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=BACKEND_PORT)
