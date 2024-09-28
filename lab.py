#!/usr/bin/python3
import os, stat, shutil
from datetime import datetime
import segno

# Preparativos e variaveis
lista_etiquetas = "./lista.txt"
pasta_etiquetas = "./etiquetas_" + datetime.now().strftime('%Y-%m-%d')

# Confere existencia de lista e de pasta para salvar etiquetas
if os.path.exists(lista_etiquetas):
    if os.path.exists(pasta_etiquetas):
        shutil.rmtree(pasta_etiquetas, ignore_errors=True)
    os.makedirs(pasta_etiquetas,exist_ok=True)
    etiquetas = open(lista_etiquetas, "r")
    for etiqueta in etiquetas:
        # Muda variaveis de acordo com input do arquivo de lista
        texto_etiqueta = etiqueta[:12]
        arquivo_etiqueta = pasta_etiquetas + "/" + texto_etiqueta + ".png"
        print (texto_etiqueta)
        # Cria etiqueta(s)
        qrcode = segno.make_qr(texto_etiqueta)
        qrcode.save(
                arquivo_etiqueta,
                scale=5,
                )
    etiquetas.close
    print("OK - Imagens de etiquetas geradas com sucesso")
else:
    print("ERROR - Arquivo de lista não localizado")

