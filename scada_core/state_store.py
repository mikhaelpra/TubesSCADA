# [STUDENT]
# Minggu 1:
# - Buat penyimpanan point in-memory
# - Sediakan fungsi add/update/get/list
#
# Minggu 6:
# - Pastikan sinkronisasi state stabil untuk demo
class StateStore:
    def __init__(self):
        self.points = {}
