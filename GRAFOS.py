
from collections import defaultdict
class Grafo:
    def __init__(self, direcionado=False):
        self._grafo = defaultdict(set)
        self.direcionado = direcionado
        self.lista_Vertices = []
        self.lista_Arestas = []
        
     
    def criarVertice(self, vertice):
        self.lista_Vertices.append(vertice)

    def criarArestas(self, origem, destino):
        origem_aux = self.busca_Vertice(origem)
        destino_aux = self.busca_Vertice(destino)

        if(origem_aux is not None) and (destino_aux is not None):
            self.lista_Arestas.append(Aresta(origem_aux, destino_aux))
        else:
            print("Um dos vertices ou ambos são inválidos")

        if self.direcionado == False:
            self.lista_Arestas.append(Aresta(destino_aux, origem_aux, peso))

    def removerAresta(self, origem, destino):
        rigem_aux = self.busca_vertice(origem)
        destino_aux = self.busca_Vertice(destino)

        if(origem_aux is not None) and (destino_aux is not None):
            self.lista_Arestas.remove(Aresta(origem_aux, destino_aux))
        else:
            print("Um dos vertices ou ambos são inválidos")

        if self.direcionado == False:
            self.lista_Arestas.append(Aresta(destino_aux, origem_aux, peso))        

    def busca_Vertice(self, vertice): 
        for i in self.lista_Vertices:
            if vertice == i.getId():
                return i
        else:
            return None

    def busca_Aresta(self, origem, destino):
        for i in self.lista_Arestas:
            org = i.getOrigem()
            dest = i.getDestino()

            if org.getId() == origem.getId() and dest.getId() == destino.getId():
                return i
  
    def adjVertice(self, vertice):
        for i in range(len(self.lista_Arestas)):
            origem = self.lista_Arestas[i].getOrigem()
            destino = self.lista_Arestas[i].getDestino()
            if (vertice.getId() == origem.getId()) and (destino.getVisitado() == False):
                destino.setVisitado(True)  # P não retornar o mesmo vertice seguidas veses
                return destino
        else:
            print("vertice inválido")

    def get_vertices(self):
        """ Retorna a lista de vértices do grafo. """
        return list(self._grafo.keys())


    def get_arestas(self):
        """ Retorna a lista de arestas do grafo. """
        return [(k, v) for k in self._grafo.keys() for v in self._grafo[k]]

#######fim do objeto################

grafo = Grafo()

opcao = 0
while opcao != 8:
    print("=============================")
    print("Selecione uma das opções abaixo: ")
    print("1 - Criar grafo")
    print("2 - Inserir aresta")
    print("3 - Remover aresta")
    print("4 - Buscar aresta")
    print("5 - Lista de adjacencias de um vertice")
    print("6 - Exibir grafo")
    print("7 - Nº de vertices e arestas")
    print("8 - Grau de um vertice")
    print("8 - Sair")
    print("=============================")

    opcao = int(input("-> "))

    if opcao == 1:
        sair = 1
        while sair != 0:
            vert = int(input("Vertice a ser adicionado: "))
            grafo.criarVertice(vert)
            sair = int(input("0 - sair//1 - continuar: "))

        print("Vertices criados com sucesso, insira a origem e destinos das arestas a serem inseridas.")

        sair = 1
        while sair !=0:
            origem = int(input("Origem da aresta: "))
            destino = int(input("Destino da aresta: "))
            grafo.criarArestas(origem, destino)
            sair = int(input("1 - continuar//2 - sair: "))

    if opcao == 8:
        break
