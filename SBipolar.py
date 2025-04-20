from bipolar import *
from sympy import symbols, oo  # бесконечность


# Двухполюсник в схеме замещения
class SBipolar:
    s = symbols("s")

    def __init__(self, src: Bipolar):
        self.b_id: int = src.b_id
        self.init_node: int = src.init_node
        self.end_node: int = src.end_node
        self.b_type: str = src.b_type
        self.value: int = src.value
        self.z = self.get_z()  # комплексное сопротивление
        self.source_value = self.get_source_value()  # напряжение или ток источника

    def get_z(self):
        if self.b_type in ["r", "g"]:
            return self.value
        if self.b_type == "l":
            return self.value * self.s
        if self.b_type == "c":
            return 1 / (self.value * self.s)
        if self.b_type in ["i", "u"]:
            return 0

    def get_source_value(self):
        if self.b_type == ["r", "g"]:
            return 0
        if self.b_type in ["l", "c"]:
            return None  # в будущем цепь должна сама определить т.к. могут быть и НННУ
        if self.b_type in ["i", "u"]:
            return self.value / self.s

    def get_y(self):
        if self.z == 0:
            return oo
        return 1 / self.z
