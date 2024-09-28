# python3-qrcodegenerator
Script to read a list of strings from a local file to generate as QRCode images ready to print as labels

Using popular libraries such as segno

Able do adjust zoom level of genarated lables on the fly passing an argument value

Created assuming naming conventions for PCs in ICTSI Rio, with 12 characters long string (most likely following a nomenclature standard as T1R-T-NNNNNN), but made flexible regardless, whatever valid string lengh and Unicode UTF-8 Charset should and might work

Assumes python3 under Linux (most likely Debian-like distro), but might be easyly modified to your reality

It usually generates a pretty file, unique per string

Exemplo1 | Exemplo2 | Exemplo3
--- | --- | ---
![QRCode Sample1](https://github.com/FabioLeitao/python3-qrcodegenerator/blob/848301fe78c33c5353c9fb45ca4c2b39f98692bc/T1R-D-001161.png)|![QRCode Sample2](https://github.com/FabioLeitao/python3-qrcodegenerator/blob/848301fe78c33c5353c9fb45ca4c2b39f98692bc/T1R-L-00000110.png)|![QRCode Sample3](https://github.com/FabioLeitao/python3-qrcodegenerator/blob/848301fe78c33c5353c9fb45ca4c2b39f98692bc/T1R-N-002004.png)
