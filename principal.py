import funcoes
import os

a_palavra = funcoes.sortear()
aux = len(a_palavra)
tentativa=[[" _ "]*len(a_palavra)]
chance = 7
erro=0
result= 0

z= funcoes.imprime_mensagem_abertura()
if z==1:
    while True:
        funcoes.desenha_forca(erro)
        
        print(tentativa)
        letra = str(input("Digite uma letra: ")).lower()
        
        erro += funcoes.verificacao(letra,a_palavra,tentativa)
        os.system("cls")
        
        print ("voce já errou : {}".format(erro))
        
        if erro>=chance:
            os.system("cls")
            funcoes.imprime_mensagem_perdedor(a_palavra)
            print ("fim de jogo!")
            break
        result = funcoes.finish(aux,tentativa)
        if result>=1:
            os.system("cls")
            funcoes.imprime_mensagem_vencedor()
            break
   

    
    
        


