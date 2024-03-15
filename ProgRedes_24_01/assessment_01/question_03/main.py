###############################################################
#                                                             #
#  Author: @pedrohcdsouza & @MatheusLuizSoares                #
#  Date: 14/03/2024                                           #
#                                                             #
###############################################################

import os
from mylib import *

# Verificando o diretório do programa.
strDir = os.path.abspath(__file__)  
strDir = os.path.dirname(strDir)

# Criando um laço de repetição para solicitar o nome do arquivo desejado.
while True: 
    try:
        ArcName = str(input("Please enter the desired filename (including the extension): "))
        ArcDir = os.path.join(strDir, ArcName)
        with open(ArcDir,'rb') as reader:
            ReadTcpDump(reader)

            if not ReadTcpDump(reader):
                print("\nThe file is empty. Please provide a non-empty file.\n")
                continue
            else:
                
                


                
    except Exception as exc:
        print(exc)
    else:
        break



    