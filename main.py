import matplotlib.pyplot as plt
from collections import Counter


def zerarDescobertos():
    for i in range(len(desc)):
        desc[i] = 0


def preencheListaAdjacencia(lista, listaAdjacencia):

    for i in lista[0]:
        separador = i.split()

        v1 = (int(separador[0]))
        v2 = (int(separador[1]))
        peso = (int(separador[2]))

        if (v2, peso) not in listaAdjacencia[v1]:
            listaAdjacencia[v1].append((v2, peso))
        if (v1, peso) not in listaAdjacencia[v2]:
            listaAdjacencia[v2].append((v1, peso))


def preencheMatrizAdjacencia(matriz, matAdj):

    for i in matriz[0]:
        separador = i.split()

        v1 = (int(separador[0]))
        v2 = (int(separador[1]))
        peso = (int(separador[2]))

        matAdj[v1][v2] = peso
        matAdj[v2][v1] = peso
    return matAdj


def exibirInformacoes(grafo):
    listaGraus = []
    grausUnicos = []

    for i in grafo:
        grau = 0
        for j in i:
            if j != 0:
                grau += 1
        listaGraus.append(grau)

    print("Maior grau:", max(listaGraus), "- vertice: ",
          listaGraus.index(max(listaGraus)))
    print("Menor grau:", min(listaGraus), "- vertice: ",
          listaGraus.index(min(listaGraus)))
    print("\nGrau medio:", sum(listaGraus) / len(listaGraus))

    for i in listaGraus:
        if i not in grausUnicos:
            grausUnicos.append(i)
    grausUnicos.sort()

    freqRel = []
    x = []
    for i in range(len(listaGraus)):
        x.append(i)
        freqRel.append(0)

    for i in grausUnicos:
        freqRel[i] = (listaGraus.count(i) / len(listaGraus))

    plt.plot(x, freqRel)
    plt.title('Distribuição empírica')
    plt.xlabel('Grau')
    plt.ylabel('Frequência relativa')
    plt.show()

    input("\nAperte enter para exibir a frequencia relativa de cada grau !\n")
    print("\nFrequencia relativa:")
    for i in grausUnicos:
        print("Grau", i, ":", freqRel[i])


def busca_largura(G, s):
    arquivo = open('busca_largura.txt', 'w')
    string = [[] for i in range((len(G)))]
    nivel = [0 for i in range(len(G))]
    Q = [s]
    R = [s]
    desc[s] = 1
    string[0] = "vertice: nivel\n" + str(s) + ": " + str(nivel[s]) + "\n"
    while len(Q) != 0:
        u = Q.pop(0)
        for v, i in G[u]:
            if desc[v] == 0:
                nivel[v] = nivel[u] + 1
                string[v] = str(v) + ": " + str(nivel[v]) + "\n"
                Q.append(v)
                R.append(v)
                desc[v] = 1
    for i in string:
        if len(i) > 0:
            arquivo.write(i)
    print("\nMaior nivel: ", max(nivel))
    arquivo.close()
    return R


def busca_profundidade(G, s):
    arquivo = open('busca_profundidade.txt', 'w')
    string = [[] for i in range((len(G)))]
    S = [s]
    R = [s]
    desc[s] = 1
    string[0] = "vertice: nivel\n" + str(s) + ": 0\n"
    cont = 1
    while len(S) != 0:
        u = S[-1]
        desempilhar = True
        for v, i in G[u]:
            if desc[v] == 0:
                string[v] = str(v) + ": " + str(cont) + "\n"
                desempilhar = False
                S.append(v)
                R.append(v)
                desc[v] = 1
                cont += 1
                break
        if desempilhar:
            S.pop()
            cont -= 1
    for i in string:
        if len(i) > 0:
            arquivo.write(i)
    arquivo.close()
    return R


def busca_larguraMA(G, s):
    arquivo = open('busca_larguraMatriz.txt', 'w')
    string = [[] for i in range((len(G)))]
    nivel = [0 for i in range(len(G))]
    Q = [s]
    R = [s]
    desc[s] = 1
    string[0] = "vertice: nivel\n" + str(s) + ": " + str(nivel[s]) + "\n"
    while len(Q) != 0:
        u = Q.pop(0)
        for v in range(len(G[u])):
            if desc[v] == 0 and G[u][v] != 0:
                nivel[v] = nivel[u] + 1
                string[v] = str(v) + ": " + str(nivel[v]) + "\n"
                Q.append(v)
                R.append(v)
                desc[v] = 1
    for i in string:
        if len(i) > 0:
            arquivo.write(i)
    arquivo.close()
    return R


def busca_profundidadeMA(G, s):
    arquivo = open('busca_profundidadeMatriz.txt', 'w')
    string = [[] for i in range((len(G)))]
    S = [s]
    R = [s]
    desc[s] = 1
    string[0] = "vertice: nivel\n" + str(s) + ": 0\n"
    cont = 1
    while len(S) != 0:
        u = S[-1]
        desempilhar = True
        for v in range(len(G[u])):
            if desc[v] == 0 and G[u][v] != 0:
                string[v] = str(v) + ": " + str(cont) + "\n"
                desempilhar = False
                S.append(v)
                R.append(v)
                desc[v] = 1
                cont += 1
                break
        if desempilhar:
            S.pop()
            cont -= 1
    for i in string:
        if len(i) > 0:
            arquivo.write(i)
    arquivo.close()
    return R


def busca_largura_conexos(G, s, comp):
    Q = [s]
    R = [s]
    desc[s] = comp
    while len(Q) != 0:
        u = Q.pop(0)
        for v, i in G[u]:
            if desc[v] == 0:
                Q.append(v)
                R.append(v)
                desc[v] = comp
    return R


def componentes_conexas(G):
    comp = 0
    for v in range(len(G)):
        if desc[v] == 0:
            comp += 1
            busca_largura_conexos(G, v, comp)


def informacoesGrafosConexos(grafo):
    componentes_conexas(grafo)

    conexos = []
    for i in desc:
        if i not in conexos:
            conexos.append(i)
    conexos.sort()

    print("Componentes conexas:", len(conexos))
    input("\nAperte enter para exibir a quantidade de vertices conexos em cada componente !\n")

    for i in conexos:
        print("-", desc.count(i), "vertices")

    frequencia = Counter(desc).most_common()
    print("\nA maior componente conexa possui", frequencia[0][1], "vertice(s) !\n")
    print("A menor componente conexa possui", frequencia[-1][1], "vertice(s) !\n")


def informacoesGrafosConexosMA(grafo):
    G = []

    for i in grafo:
        cont = 0
        aux = []
        for j in i:
            if j != 0:
                aux.append((cont, j))
            cont += 1
        G.append(aux)

    informacoesGrafosConexos(G)


nomeArquivo = input("Digite o nome do arquivo que voce deseja ler: ")
arquivo = open(nomeArquivo, 'r')

cabecalho = arquivo.readline()
cabecalho = cabecalho.split()
numVertices = int(cabecalho[0])
numArestas = int(cabecalho[1])

print("Escolha a maneira que voce deseja representar o seu grafo: ")
print("1 - Lista de Adjacencias")
print("2 - Matriz de Adjacencias")
print("Digite sua opcao: ", end="")
opcao = int(input())

while(opcao != 1 and opcao != 2):
    print("Opcao invalida!")
    print("Digite novamente: ", end="")
    opcao = int(input())

if opcao == 1:
    lista = []
    listaAdjacencia = [[] for i in range(numVertices)]
    lista.append(arquivo.readlines())
    preencheListaAdjacencia(lista, listaAdjacencia)
    desc = [0 for i in range(len(listaAdjacencia))]
    input("\nAperte enter para exibir as informações do grafo !\n")
    exibirInformacoes(listaAdjacencia)
    v = int(input("\nDigite um vertice para comecar a buscar em largura: "))
    busca_largura(listaAdjacencia, v)
    v = int(input("\nDigite um vertice para comecar a buscar em profundidade: "))
    zerarDescobertos()
    busca_profundidade(listaAdjacencia, v)
    input("\nAperte enter para exibir as informações dos grafos conexos !\n")
    zerarDescobertos()
    informacoesGrafosConexos(listaAdjacencia)
else:
    matriz = []
    matAdj = [[0 for i in range(numVertices)]for i in range(numVertices)]
    matriz.append(arquivo.readlines())
    matAdj = preencheMatrizAdjacencia(matriz, matAdj)
    desc = [0 for i in range(len(matAdj))]
    input("\nAperte enter para exibir as informações do grafo !\n")
    exibirInformacoes(matAdj)
    v = int(input("\nDigite um vertice para comecar a buscar em largura: "))
    busca_larguraMA(matAdj, v)
    v = int(input("\nDigite um vertice para comecar a buscar em profundidade: "))
    zerarDescobertos()
    busca_profundidadeMA(matAdj, v)
    input("\nAperte enter para exibir as informações dos grafos conexos !\n")
    zerarDescobertos()
    informacoesGrafosConexosMA(matAdj)

arquivo.close()
