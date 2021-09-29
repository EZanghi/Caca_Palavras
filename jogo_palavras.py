# Para a execução do programa inicialmente é feita a declaração de todas as variáveis
# do ambiente, como o banco de palavras, a tabela de pontos, em seguida é feito o tratamento
# das palavras do banco retirando todos os caracteres especiais e substiuindo-os por
# seus equivalentes simples (ex: á = a).

# - A lógica do programa se baseia em:
#     - receber do usuário os caracteres;
#     - em seguida o "gera_palavras" gera uma lista com todas as combinações possíveis com as letras informadas;
#     - As "palavras_geradas" vão para o "compara_palavras", que entrega nova lista "palavras_validas" formada pelas palavras
#       que existem no banco de palavras; 
#     - Da lista de "palavras_validas", é feito o score_palavra com a pontuação de cada uma delas;
#     - a "lista_score_palavra" é tratada pelas outras regras do jogo ("palavra_maior_pontuacao", 
#       "palavra_menos_letras_ordenado")
#     - e só então é feita a escolha da palavra conforme as regras.

 #-*- coding: utf-8 -*-

import unicodedata # Usada para tratar os caracteres especiais do banco_palavras
import executa_jogo

##DECLARANDO AS VARIÁVEIS DO JOGO

# Declarando a lista de palavras
banco_palavras = ["Abacaxi", "Manada", "mandar", "porta", "mesa", "Dado", "Mangas", "Já", "coisas",
"radiografia", "matemática", "Drogas", "prédios", "implementação", "computador", "balão",
"Xícara", "Tédio", "faixa", "Livro", "deixar", "superior", "Profissão", "Reunião", "Prédios",
"Montanha", "Botânica", "Banheiro", "Caixas", "Xingamento", "Infestação", "Cupim",
"Premiada", "empanada", "Ratos", "Ruído", "Antecedente", "Empresa", "Emissário", "Folga",
"Fratura", "Goiaba", "Gratuito", "Hídrico", "Homem", "Jantar", "Jogos", "Montagem",
"Manual", "Nuvem", "Neve", "Operação", "Ontem", "Pato", "Pé", "viagem", "Queijo", "Quarto",
"Quintal", "Solto", "rota", "Selva", "Tatuagem", "Tigre", "Uva", "Último", "Vitupério",
"Voltagem", "Zangado", "Zombaria", "Dor"]


#Tratando o banco de palavras
# Para tratar os caracteres especiais no banco de palavras está sendo utilizado o método "normalize" da lib "unicodedata"
novo_banco_palavras = []
for palavra in banco_palavras:
    novo_banco_palavras.append(''.join(ch for ch in unicodedata.normalize('NFKD', palavra) 
                                if not unicodedata.combining(ch)).upper())


# Definindo a pontuação de cada letra
# Este é um gerador de dicionário com a pontuação de cada letra conforme às regras do jogo
letras_um_ponto = ("E", "A", "I", "O", "N", "R", "T", "L", "S", "U")
letras_dois_ponto = ("D", "G")
letras_tres_ponto = ("B", "C", "M", "P")
letras_cinco_ponto = ("F", "H", "V")
letras_oito_ponto = ("J", "X")
letras_treze_ponto = ("Q", "Z")
listas = [letras_um_ponto, letras_dois_ponto, letras_tres_ponto, 
        letras_cinco_ponto, letras_oito_ponto, letras_treze_ponto]
pontos = (1, 2, 3, 5, 8, 13)

tabela_pontos = dict()
pos_pontos = -1

for lista in listas:
    pos_pontos += 1
    for letra in lista:
        tabela_pontos[letra] = pontos[pos_pontos]




#Gerador de combinações
# A lógica deste gerador consiste em:
#     - formar uma lista com os caracteres informados pelo usuário;
#     - enquanto a maior palavra gerada não tiver tantos caracteres quanto o informados pelo usuário;
#     - o programa irá percorrer cada valor da lista;
#     - e acrescentar um dos caracteres informados;
#         se o caracter acrescentado tiver menos ou a mesma quantidade deste nos caracteres informados*
#         * essa condição foi usada para permitir que um mesmo caracter possa ser incluido na palavra,
#         * desde que seja a mesma quantidade informada pelo usuário.
#     - verdadeiro para as condições a palavra gerada vai para a lista "palavras_geradas"

def gera_palavras(conjunto_letras):
    palavras_geradas = list(map(str, conjunto_letras))
    
    while len(max(palavras_geradas)) < len(conjunto_letras):
        for pos in range(len(palavras_geradas)):
            for j in range(len(conjunto_letras)):
                palavra_nova = palavras_geradas[pos] + conjunto_letras[j]
                if palavra_nova.count(conjunto_letras[j]) <= conjunto_letras.count(conjunto_letras[j]):
                    palavras_geradas.append(palavra_nova)
        
    return palavras_geradas


# O comparador de palavras geradas, 
# - verifica se palavras_geradas
# - existem no novo_banco_palavras
# - e gera nova lista "palavras_validas" 
def compara_palavras(palavras_geradas, banco_palavras):
    palavras_validas = []
    for palavra in palavras_geradas:
        if palavra in novo_banco_palavras:
            palavras_validas.append(palavra)
        else:
            continue
    return palavras_validas       

# Atribui a pontuação obtida em cada uma das palavras validadas.
# - verificando o valor para cada caracter que compõem a palavra na "tabela-pontos"
# - e forma uma tupla (pontuacao, palavra)
def score_palavra(palavras_validas, tabela_pontos):
    lista_score_palavra = []
    
    for palavra in palavras_validas:
        pontuacao = 0
        for letra in range(len(palavra)):
            pontuacao += tabela_pontos[palavra[letra]]
        lista_score_palavra.append((pontuacao, palavra))
        
    return lista_score_palavra

# Define as palavras com maior pontuação, devolve lista de palavras organizada pelos pontos
def palavra_maior_pontuacao(lista_score_palavra):
    lista_score_palavra.sort(reverse = True) #Inverte a lista recebida conforme número de pontos da palavra
    maior = lista_score_palavra[0][0]
    lista_palavra_maior_pontuacao = []
    
    for i in lista_score_palavra:
        if i[0] >= maior:
            lista_palavra_maior_pontuacao.append(i)
    return lista_palavra_maior_pontuacao

# Define a palavra que tem menos letras, devolve nova lista com quantidade de caracteres e a palavra
def palavra_menos_letras_ordenado(lista_palavra_maior_pontuacao):
    lista_palavra_menos_letras = []
    
    for i in lista_palavra_maior_pontuacao:
        lista_palavra_menos_letras.append((i[1],i[0]))
    lista_palavra_menos_letras.sort()
    
    return lista_palavra_menos_letras

# Reponsável por chamar as regras para escolha da palavra           
def escolhe_palavra(lista_score_palavra):
    lista_palavra_maior_pontuacao = palavra_maior_pontuacao(lista_score_palavra)
    lista_palavra_menos_letras = palavra_menos_letras_ordenado(lista_palavra_maior_pontuacao)
    
    return lista_palavra_menos_letras[0]

# Faz uma lista de letras não utilizadas;
# - retira da "lista_letras_conjunto_letras" todas as letras dentro de lista_letras_palavra_escolhida;
# - criando um lista de "lista_letras_nao_utilizadas".
def letras_nao_utilizadas(palavra_escolhida, conjunto_letras):
    
    if len(palavra_escolhida) > 0:
        lista_letras_palavra_escolhida = list(map(str, palavra_escolhida[0]))
        lista_letras_conjunto_letras = list(map(str, conjunto_letras))

        for letra in lista_letras_palavra_escolhida:
            lista_letras_conjunto_letras.remove(letra)        

        lista_letras_nao_utilizadas = lista_letras_conjunto_letras
        
    else:
        lista_letras_nao_utilizadas = conjunto_letras
        
    return lista_letras_nao_utilizadas

# Para dar opção do usuário realizar nova partida do jogo.
def pergunta_repetir_jogo():
    repetir = input("\nVocê quer jogar de novo? Digite (S)-sim ou qualquer letra para voltar ao menu: ").upper()
    if (repetir == "S"):
        print("")
        jogo_palavras_convecional()
    else:
        print("\n")
        executa_jogo.escolhe_modo_jogo()

##INÍCIO DO JOGO

def jogo_palavras_convecional():

    print("\n##############################\n")
    conjunto_letras = input("Digite as letras disponíveis nesta jogada: ").upper()

    palavras = gera_palavras(conjunto_letras)
    palavras_validas = compara_palavras(palavras, banco_palavras)
    
    if len(palavras_validas) > 0:

        lista_score_palavra = score_palavra(palavras_validas, tabela_pontos)
        palavra_escolhida = escolhe_palavra(lista_score_palavra)
        lista_letras_nao_utilizadas = letras_nao_utilizadas(palavra_escolhida, conjunto_letras)
        print("{}, palavra de {} pontos".format(palavra_escolhida[0], palavra_escolhida[1]))
        print("Sobraram: {}".format(lista_letras_nao_utilizadas))
        
    else:
        lista_letras_nao_utilizadas = letras_nao_utilizadas([],conjunto_letras)
        print("Nenhuma palavra encontrada")
        print("Sobraram: {}".format(lista_letras_nao_utilizadas))
        print("\n##############################")

    pergunta_repetir_jogo()

if (__name__ == "__main__"):
    jogo_palavras_convecional()