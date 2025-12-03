import networkx as nx
from database.dao import DAO


class Model:
    def __init__(self):
        self.G = nx.Graph()
        self.lista_rifugi=[]
        self.lista_connessioni=[]


    def build_graph(self, year: int):
        """
        Costruisce il grafo (self.G) dei rifugi considerando solo le connessioni
        con campo `anno` <= year passato come argomento.
        Quindi il grafo avrà solo i nodi che appartengono almeno ad una connessione, non tutti quelli disponibili.
        :param year: anno limite fino al quale selezionare le connessioni da includere.
        """
        # TODO
        self.get_nodes()
        self.get_connessioni(year)
        for connessione in  self.lista_connessioni:
            rifugio1=self.lista_rifugi[connessione.id_rifugio1]
            rifugio2=self.lista_rifugi[connessione.id_rifugio2]
            self.G.add_edge(rifugio1, rifugio2)
        print(self.G)
        return self.G.nodes()


    def get_nodes(self):
        """
        Restituisce la lista dei rifugi presenti nel grafo.
        :return: lista dei rifugi presenti nel grafo.
        """
        x=DAO()
        self.lista_rifugi=x.search_all_rifugi()


   #for rifugio in self.lista_rifugi:
   #         self.dizionario_rifugi[rifugio['id']]=rifugio

        # TODO

    def get_num_neighbors(self, node):
        """
        Restituisce il grado (numero di vicini diretti) del nodo rifugio.
        :param node: un rifugio (cioè un nodo del grafo)
        :return: numero di vicini diretti del nodo indicato
        """
        return self.G.degree(node)
        # TODO

    def get_num_connected_components(self):
        """
        Restituisce il numero di componenti connesse del grafo.
        :return: numero di componenti connesse
        """
        # TODO
        return self.G.nodes()

    def get_reachable(self, start):
        """
        Deve eseguire almeno 2 delle 3 tecniche indicate nella traccia:
        * Metodi NetworkX: `dfs_tree()`, `bfs_tree()`
        * Algoritmo ricorsivo DFS
        * Algoritmo iterativo
        per ottenere l'elenco di rifugi raggiungibili da `start` e deve restituire uno degli elenchi calcolati.
        :param start: nodo di partenza, da non considerare nell'elenco da restituire.

        ESEMPIO
        a = self.get_reachable_bfs_tree(start)
        b = self.get_reachable_iterative(start)
        b = self.get_reachable_recursive(start)



























        return a
        """

        # TODO
    def get_connessioni(self, anno):
        x=DAO()
        self.lista_connessioni=x.get_all_connessioni_anno(anno)
