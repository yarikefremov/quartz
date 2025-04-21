from Bipolar import *
from SBipolar import SBipolar


class CircuitCollection:
    def __init__(self):
        self.t_circuit: list[Bipolar] = []
        self.s_circuit: list[SBipolar] = []
        self.max_node_num = None

    # time circuit - реальная схема с i u r c l элементами
    def import_time_circuit(self, data: list[Bipolar]):
        self.t_circuit: list[Bipolar] = data
        self.t_circuit.sort(key=lambda x: x.b_id)

    # s circuit - схема замещения
    def create_s_circuit(self):
        self.s_circuit: list[SBipolar] = [SBipolar(src=el) for el in self.t_circuit]

    @staticmethod
    def get_nodes(circuit: list[Bipolar]):
        nodes = set()
        for el in circuit:
            if el.init_node not in nodes:
                nodes.add(el.init_node)
            if el.end_node not in nodes:
                nodes.add(el.end_node)
        return list(nodes)

    # Тут пришла гениальная идея: node - это не 3-4, а (3, 1) - (4, 1), где второе число - порядковый номер ДП
    # среди параллельных ДП между узлами 3 и 4 реальной цепи. Тогда можно не использовать MultiGraph.
    # т. к. set работает через хэширование, то не получится его использовать для списков
    @staticmethod
    def get_edges(circuit: list[Bipolar]):
        edges = []
        # тут хранятся комбинации реальных узлов и количество элементов с такими дубликациями
        # например, (3, 4, 1) - где 3 и 4 узлы, 1 - количество элементов
        edges_repeat = []
        for el in circuit:
            node = (el.init_node, el.end_node)
            index_in_list = CircuitCollection.index_node_in_list(edges_repeat, node)
            if index_in_list == -1:
                edges_repeat.append((node[0], node[1], 1))  # добавит (3, 4, 1)
                edges.append(((node[0], 1), (node[1], 1), {"element": el}))  # добавит ((3, 1), (4, 1), Bipolar)
            else:
                # просто увеличиваем на единичку порядковый номер
                edges_repeat[index_in_list] = (edges_repeat[index_in_list][0],
                                               edges_repeat[index_in_list][1],
                                               edges_repeat[index_in_list][2]+1)
                edges.append(((node[0], edges_repeat[index_in_list][2]),
                              (node[1], edges_repeat[index_in_list][2]),
                              {"element": el})) # добавит ((3, 2), (4, 2), Bipolar)
        return edges

    # return -1 если узла нет в списке
    @staticmethod
    def index_node_in_list(edges: list[(int, int, int)], node: (int, int)):
        if len(edges) == 0:
            return -1
        for i in range(len(edges)):
            if edges[i][0] == node[0] and edges[i][1] == node[1]:
                return i
            if edges[i][1] == node[0] and edges[i][0] == node[1]:
                return i
        return -1
