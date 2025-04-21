from Bipolar import *


# return -1 если узла нет в списке
def index_node_in_list(edges: list[((int, int), {str: Bipolar})], node: (int, int)):
    if len(edges) == 0:
        return -1
    for i in range(len(edges)):
        if edges[i][0] == node[0] and edges[i][1] == node[1]:
            return i
        if edges[i][1] == node[0] and edges[i][0] == node[1]:
            return i
    return -1


# Цепь с одним источником пока
class Circuit:

    def __init__(self, data: list[Bipolar]):
        self.circuit: list[Bipolar] = data
        self.nodes: list[int] = self.init_nodes()
        self.edges: list[((int, int), {str: Bipolar})] = []
        self.source_bipolar_id: int | None = self.get_source_bipolar_id()
        # для реальных узлов добавим виртуальные (при параллельном подключении элементов)
        self.node_aliases: dict[int, list[int]] = dict()
        self.calculate_edges_and_nodes()

    def init_nodes(self):
        nodes = set()
        for el in self.circuit:
            if el.init_node not in nodes:
                nodes.add(el.init_node)
            if el.end_node not in nodes:
                nodes.add(el.end_node)
        return list(nodes)

    def get_nodes(self):
        return

    # Тут пришла гениальная идея: node - это не 3-4, а (3, 1) - (4, 1), где второе число - порядковый номер ДП
    # среди параллельных ДП между узлами 3 и 4 реальной цепи. Тогда можно не использовать MultiGraph.
    # т. к. set работает через хэширование, то не получится его использовать для списков
    def calculate_edges_and_nodes(self):
        self.edges = []
        # тут хранятся комбинации реальных узлов и количество элементов с такими дубликациями
        # например, (3, 4, 1) - где 3 и 4 узлы, 1 - количество элементов
        for el in self.circuit:
            node = (el.init_node, el.end_node)
            index_in_list = index_node_in_list(self.edges, node)
            # если еще нет такого направления
            if index_in_list == -1:
                self.edges.append((node, {"element": el}))  # добавит ((3, 4), Bipolar)
            else:
                # просто увеличиваем на единичку порядковый номер каждого из узлов и добавляем получившуюся пару
                self.node_aliases[self.edges[index_in_list][0][0]].append(0) #max_node_num+1
                self.node_aliases[self.edges[index_in_list][0][1]].append(0) #max_node_num+2
                self.edges.append(((0, 0), {"element": el}))

    def get_source_bipolar_id(self):
        b_id = None
        for el in self.circuit:
            if el.b_type not in ["u", "i"]:
                continue
            # несколько источников в цепи
            if b_id is not None:
                return None
            # нашли 1 источник в цепи
            b_id = el.b_id
        #1 источник в цепи
        if b_id is not None:
            return b_id
        # источников в цепи нет
        print("Circuit.get_source_bipolar_id: Источник не найден")
        return None
