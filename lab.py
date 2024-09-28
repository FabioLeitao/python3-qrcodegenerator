# basic_qrcode.py

import segno

qrcode = segno.make_qr("T1R-L-000001")
qrcode.save(
    "T1R-L-000001_qrcode.png",
    scale=5,
)
