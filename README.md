# python3-qrcodegenerator
Script to read a list of strings from a local file to generate as QRCode images ready to print as labels

Using popular libraries such as segno

Able do adjust zoom level of genarated lables on the fly passing an argument value (default zoom = 6)

Ablo to export to PNG (default file format) or PDF as a trigger argument

Created assuming naming conventions for PCs in ICTSI Rio, with 12 characters long string (most likely following a nomenclature standard as T1R-T-NNNNNN), but made flexible regardless, whatever valid string lengh and Unicode UTF-8 Charset should be in listas.txt file, and might work if it is able to represent a folder or file name as such.

Assumes python3 under Linux (most likely Debian-like distro), but might be easyly modified to your reality

It usually generates a pretty file, unique per string (still studing a way to create an array of lables)

Exemplo1 (z6) | Exemplo2 (z10) | Exemplo3 (z3) | Exemplo4 (art)
--- | --- | --- | ---
![QRCode Sample1](https://github.com/FabioLeitao/python3-qrcodegenerator/blob/848301fe78c33c5353c9fb45ca4c2b39f98692bc/T1R-D-001161.png)|![QRCode Sample2](https://github.com/FabioLeitao/python3-qrcodegenerator/blob/848301fe78c33c5353c9fb45ca4c2b39f98692bc/T1R-L-00000110.png)|![QRCode Sample3](https://github.com/FabioLeitao/python3-qrcodegenerator/blob/848301fe78c33c5353c9fb45ca4c2b39f98692bc/T1R-N-002004.png)|![QRCode Sample4](https://github.com/FabioLeitao/python3-qrcodegenerator/blob/2ca9e061f4f96617eb0b1350a8a06877451ecaba/icon_T1R-N-002004.png)
