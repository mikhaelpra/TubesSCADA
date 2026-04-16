# [STUDENT]
# Minggu 1:
# - Rancang model point SCADA
# - Minimum field: point_id, type, value, quality, timestamp
# - Buat mekanisme update value dan timestamp
#
# Minggu 2:
# - Tambahkan metadata yang dibutuhkan oleh command/feedback
#
# Minggu 3:
# - Tambahkan field yang mendukung alarm dan SOE
from dataclasses import dataclass, field
from typing import Any
import time

@dataclass
class Point:
    point_id: str
    point_type: str
    value: Any = None
    quality: str = "GOOD"
    timestamp: float = field(default_factory=lambda: time.time())
