# [MODIFY]
# Minggu 1:
# - Tambahkan endpoint /ingest untuk menerima update point dari gateway/RTU
# - Tambahkan endpoint /points untuk membaca seluruh state point
# Minggu 2:
# - Tambahkan endpoint /command/send
# Minggu 3:
# - Tambahkan endpoint /alarms dan /soe
# Minggu 5:
# - Tambahkan endpoint /historian/query
'''
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__, static_folder="../ui")
    CORS(app)

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.get("/")
    def index():
        return send_from_directory(app.static_folder, "index.html")

    return app
'''
from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import os
import time
from rtu import simulator#WEEK2

def create_app():
    app = Flask(__name__, static_folder="../ui")
    CORS(app)

    # 🔥 STATE (penyimpanan data sementara)
    STATE = {}

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.get("/")
    def index():
        return send_from_directory(app.static_folder, "index.html")

    # 🔥 ENDPOINT TERIMA DATA
    @app.post("/ingest")
    def ingest():
        nonlocal STATE
        data = request.json

        for key, value in data.items():
            STATE[key] = {
                "value": value,
                "timestamp": time.time()
            }

        print("STATE UPDATE:", STATE)  # debug

        return jsonify({"status": "ok"})

    # 🔥 ENDPOINT AMBIL DATA
    '''@app.get("/points")
    def points():
        return jsonify(STATE) #WEEK1
    
    @app.route("/points") #WEEK2
    def points():
        return {
            "pump_status": {
                "value": simulator.STATE["pump_status"]
            },
            "temperature": {
                "value": simulator.STATE["temperature"]
            }
        }'''
    @app.route("/points")
    def points():
        simulator.update()  # 🔥 ini penting

        return {
            "pump_status": {
                "value": simulator.STATE["pump_status"]
            },
            "temperature": {
                "value": simulator.STATE["temperature"]
            }
        }

#WEEK 1


    @app.route("/command/send", methods=["POST"])
    def send_command():
        data = request.json
        cmd = data.get("command")

        if cmd == "OPEN":
            simulator.set_pump(0)
        elif cmd == "CLOSE":
            simulator.set_pump(1)

        return {"status": "executed"}



    return app