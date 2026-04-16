# [STUDENT]
# Minggu 5:
# - Simpan data historis sederhana ke SQLite
# - Buat query rentang waktu
#
# Minggu 6:
# - Pastikan trend dapat dibuka tanpa error saat demo
import sqlite3

class Historian:
    def __init__(self, db_path="data/historian.db"):
        self.db_path = db_path
