#!/usr/local/bin/python3.13
import io, os, getopt, sys, stat, shutil
from datetime import datetime
from PIL import Image
import segno

# Preparativos e variaveis
icon=False
contador = 0
zoom_imagem = 6
lista_etiquetas = "./lista.txt"
pasta_etiquetas = "./etiquetas_" + datetime.now().strftime('%Y-%m-%d')
extensao_etiquetas = "png"

# Remove 1st argument from the list of command line arguments
argumentList = sys.argv[1:]

# Options
options = "hipz:"

# Long options
long_options = ["Help", "Icon", "PDF", "Zoom="]

try: 
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)

    # Checking each argument
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-h", "--Help"):
            print("\n./lab.py [options]\n\n Options:\n    -h | --Help     Mostra esta ajuda\n    -i | --Icon     Cria arquivo PNG de etiquetas com icone artístico de logotipo da empresa\n    -p | --PDF      Indica formado a ser salvo em PDF (padrão é PNG)\n    -z | --Zoom=    Indica zoom da imagem resultante (padrão é 6)\n\n  Foi criado pensado na geração de etiquetas para PCs da ICTSI Rio seuinda padrão de nomenclatura de strings de 12 catacteres no formato padrão T1R-T-NNNNNN para gerar etiquetas coerentes, mas foi adaptado para aceitar auqleur compimento e formatação, desde que seja mantido um nome unico por linha")
            quit()
        elif currentArgument in ("-i", "--Icon"):
            print(("Gerando arquivos com icone artistico"))
            icon=True
        elif currentArgument in ("-p", "--PDF"):
            print(("Salvando em arquivos formato PDF"))
            if icon:
                icon=False
            extensao_etiquetas = "pdf"
        elif currentArgument in ("-z", "--Zoom"):
            print(("Utilizando valor de zoom resultante (%s)") % (currentValue))
            zoom_imagem = int(currentValue)
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
        # Aumenta contador de loops
        contador = contador + 1
        # Muda variaveis de acordo com input do arquivo de lista
        comprimento = len(etiqueta) - 1
        texto_etiqueta = etiqueta[:comprimento]
        arquivo_etiqueta = pasta_etiquetas + "/" + texto_etiqueta + "." + extensao_etiquetas
        arquivo_art_etiqueta = pasta_etiquetas + "/icon_" + texto_etiqueta + "." + extensao_etiquetas
        print (arquivo_etiqueta)
        # Cria etiqueta(s)
        qrcode = segno.make_qr(
                texto_etiqueta, 
                boost_error=True,
                error='h'
                )
        if icon:
            qrcode.to_artistic(
                    background='src/icon.png',
                    target=arquivo_art_etiqueta,
                    scale=zoom_imagem
                    )
        else:
            qrcode.save(
                    arquivo_etiqueta,
                    scale=zoom_imagem
                    )
    etiquetas.close
    print("OK - " + str(contador) + " Imagens de etiquetas geradas com sucesso")
else:
    print("ERROR - Arquivo de lista não localizado")

