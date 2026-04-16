# [STUDENT]
# Minggu 1:
# - Buat simulator minimal untuk 1-2 device
# - Misal: breaker status, selector local/remote, analog sederhana
#
# Minggu 2:
# - Buat respon terhadap command OPEN/CLOSE
#
# Minggu 3:
# - Tambahkan kondisi yang memicu alarm untuk pengujian
class SimpleSimulator:
    pass




'''
import random
import time
import requests

URL = "http://localhost:8000/ingest"

def run():
    try:
        while True:
            data = {
                "pump_status": random.randint(0,1),
                "temperature": random.randint(20, 100)
            }

            try:
                requests.post(URL, json=data)
                print("kirim:", data)
            except Exception as e:
                print("gagal kirim:", e)

            time.sleep(2)

    except KeyboardInterrupt:
        print("Simulator dihentikan")


if __name__ == "__main__":
    run()'''
#WEEK1



import time
import random

STATE = {
    "pump_status": 0,
    "temperature": 30
}

def update():
    # temperature tetap berubah
    STATE["temperature"] = random.randint(20, 100)
    return STATE

def set_pump(value):
    STATE["pump_status"] = value