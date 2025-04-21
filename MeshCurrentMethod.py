import networkx as nx
from CircuitCollection import *


class MeshCurrentMethod:

    def __init__(self, circuit):
        pass

    @staticmethod
    def solve(circuit):
        if not len(circuit):
            print(f"MeshCurrentMethod.solve: пустой список как аргумент функции неуместен.")
        if isinstance(circuit[0], SBipolar):
            pass
        if isinstance(circuit[1], Bipolar):
            pass

    #ПОКА РАБОТАЕТ ТОЛЬКО ДЛЯ НННУ И ПРИ ОДНОМ ИСТОЧНИКЕ
    @staticmethod
    def solve_s_circuit(circuit: list[SBipolar]):
        source_sbipolar_id : int = MeshCurrentMethod.get_source_bipolar_id(circuit) # находим источник
        graph = nx.Graph()
        graph.add_nodes_from(CircuitCollection.get_nodes(circuit))
        graph.add_edges_from(CircuitCollection.get_edges(circuit))
        #countours: list[]= nx.cycle_basis(graph, 0)
        #while()

    @staticmethod
    def count_source_bipolar_id_in_countours(countours: list[list[int]], source_bipolar_id: int):
        counter = 0
        for el in countours:
            if source_bipolar_id in el:
                counter += 1
        return counter