#!/usr/bin/python3
import os, getopt, sys, stat, shutil
from datetime import datetime
import segno

# Preparativos e variaveis
zoom_imagem = 6
lista_etiquetas = "./lista.txt"
pasta_etiquetas = "./etiquetas_" + datetime.now().strftime('%Y-%m-%d')

# Remove 1st argument from the list of command line arguments
argumentList = sys.argv[1:]

# Options
options = "hz:"

# Long options
long_options = ["Help", "Zoom="]

try: 
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)

    # Checking each argument
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-h", "--Help"):
            print("\n./lab.py [options]\n\n Options:\n    -h | --Help   Mostra esta ajuda\n    -z | --Zoom=   Indica zoom da imagem resultante (padrão é 6)\n\n  É necessária presença de arquivo lista.txt contento string de 12 catacteres no formato padrão T1R-T-NNNNNN para gerar etiquetas coerentes")
            quit()
        elif currentArgument in ("-z", "--Zoom"):
            print(("Utilizando valor de zoom resultante (%s)") % (currentValue))
            zoom_imagem = (currentValue)
except getopt.error as err:
    # Output error, and return with an error code
    print(str(err))

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
                scale=zoom_imagem,
                )
    etiquetas.close
    print("OK - Imagens de etiquetas geradas com sucesso")
else:
    print("ERROR - Arquivo de lista não localizado")

