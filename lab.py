#!/usr/bin/python3
import os
from datetime import datetime
import shutil
import segno

# Preparativos e variaveis
texto_etiqueta = "T1R-L-000001"
pasta_etiquetas = "./etiquetas_" + datetime.now().strftime('%Y-%m-%d')
arquivo_etiqueta = pasta_etiquetas + "/" + texto_etiqueta + ".png"

# Confere existencia de pasta para salvar etiquetas
if os.path.exists(pasta_etiquetas):
    shutil.rmtree(pasta_etiquetas, ignore_errors=True)
os.makedirs(pasta_etiquetas,exist_ok=True)

# Cria etiqueta(s)
qrcode = segno.make_qr(texto_etiqueta)
qrcode.save(
    arquivo_etiqueta,
    scale=5,
)
