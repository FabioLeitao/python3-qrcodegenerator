# basic_qrcode.py

import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save(
    "scaled_qrcode.png",
    scale=5,
)
