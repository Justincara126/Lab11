import networkx as nx
from networkx.algorithms.connectivity import node_disjoint_paths

from database.dao import DAO


class Model:
    def __init__(self):
        self.G = nx.Graph()
        self.dizionario_rifugi={}
        self.dizionario_connessioni={}

    def build_graph(self, year: int):
        """
        Costruisce il grafo (self.G) dei rifugi considerando solo le connessioni
        con campo `anno` <= year passato come argomento.
        Quindi il grafo avrà solo i nodi che appartengono almeno ad una connessione, non tutti quelli disponibili.
        :param year: anno limite fino al quale selezionare le connessioni da includere.
        """
        # TODO
        self.G.clear()
        lista_rifugi = DAO().search_all_rifugi()
        for rifugi in lista_rifugi:
            self.dizionario_rifugi[rifugi.id]=rifugi
        self.get_connessioni(year)
        for connessioni in self.dizionario_connessioni.values():
            self.G.add_edge(connessioni[0],connessioni[1],anno=connessioni[2])

        #print(self.G.nodes())
        #print(self.G.edges())
        #print(self.G)
        return self.G.nodes



    def get_nodes(self):
        """
        Restituisce la lista dei rifugi presenti nel grafo.
        :return: lista dei rifugi presenti nel grafo.
        """
        # TODo
        return list(self.G.nodes)

    def get_connessioni(self,anno):
        lista_connessioni=DAO().get_all_connessioni_anno(anno)
        for connessione in lista_connessioni:
            self.dizionario_connessioni[connessione.id]=[self.dizionario_rifugi[connessione.id_rifugio1],self.dizionario_rifugi[connessione.id_rifugio2],connessione.anno]


    def get_num_neighbors(self, node):
        """
        Restituisce il grado (numero di vicini diretti) del nodo rifugio.
        :param node: un rifugio (cioè un nodo del grafo)
        :return: numero di vicini diretti del nodo indicato
        """
        # TODO
        #print(self.G.neighbors(node))
        #print(self.G.degree(node))
        return self.G.degree(node)

    def get_num_connected_components(self):
        """
        Restituisce il numero di componenti connesse del grafo.
        :return: numero di componenti connesse
        """
        # TODO
        return len(self.G.nodes)

    def get_reachable_recursive(self,nodo,nodo_visitati):
        if nodo_visitati is None:
            nodo_visitati=set()
        nodo_visitati.add(nodo)

        for vicino in self.G.neighbors(nodo):
            if vicino not in nodo_visitati:
                self.get_reachable_recursive(vicino,nodo_visitati)
        return nodo_visitati



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
        nodi_visitati=set()
        b=self.get_reachable_recursive(start,nodi_visitati)
        b.remove(start)#rimuovo dall'insieme il rifugio di partenza
        #b=self.get_reachable_bfs_tree(start)
        return nodi_visitati
    def get_reachable_bfs_tree(self,start):
        a=nx.bfs_tree(self.G,start)#restituice grafo ma devo levare lo start
        result=[]
        for nodo in a:
            if nodo!=start:
                result.append(nodo)
        return result

        #b=nx-bfs_edges(self.g,start) mi da un insieme di archi
        #b=nx-bfs_successori(self.g,start) mi da un insieme di successori
        return a
    def get_reachable_iterative(self,start):
        luoghi=set()
        pass


