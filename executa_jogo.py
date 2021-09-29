# -*- coding: utf-8 -*-

import jogo_palavras

def escolhe_modo_jogo():

    print ("#########################################")
    print ("######## ESCOLHA O MODO DO JOGO! ########")
    print ("#########################################")

    jogo = int()
    
    while jogo != 1 or jogo != 2:    
        
        jogo = int(input("\nQual modo você quer jogar?\nDigite: (1)-Modo Convecional, (2)-Sair do jogo: "))

        if (jogo == 1):
            print ("\nJogando Modo Convecional!\n")
            jogo_palavras.jogo_palavras_convecional()

        if (jogo == 2):
            print ("\n\nObrigado por jogar!\n\n")
            break
        
        print("Escolha uma opção válida")

if (__name__ == "__main__"):
    escolhe_modo_jogo()