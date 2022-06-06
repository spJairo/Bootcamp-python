from zipfile import *

with ZipFile ("WebScrapingTeste1.zip", "w") as myzip:
    myzip.write("Anexo 1.pdf")
    myzip.write("Anexo 2.pdf")
    myzip.write("Anexo 3.pdf")
    myzip.write("Anexo 4.pdf")
