from bipolar import *
from SBipolar import SBipolar


class Circuit:
    def __init__(self):
        self.t_circuit: list[Bipolar] = []
        self.s_circuit: list[SBipolar] = []

    # time circuit - реальная схема с i u r c l элементами
    def import_time_circuit(self, data: list[Bipolar]):
        self.t_circuit: list[Bipolar] = data

    #s circuit - схема замещения
    def create_s_circuit(self):
        self.s_circuit: list[SBipolar] = [SBipolar(src=self.t_circuit[i]) for i in range(len(self.t_circuit))]