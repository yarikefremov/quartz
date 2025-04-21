from CircuitCollection import *


# 1.Получение цепи
# Примерный ввод:
# Количество элементов: 5
# Элемент 1: 12 i 5 (id+положение, тип, значение величины)
def input_from_console(circuit_data: list[Bipolar]):
    amount_bipolar = int(input("Количество элементов: "))
    print("Пример ввода: 12 i 5. Номер элемента указывать не надо.")
    # Список двухполюсников
    circuit_data[:] = [Bipolar.make_from_std_annotation(f"{i + 1}" + input(f"Элемент {i + 1}: "))
                       for i in range(amount_bipolar)]


def std_input():
    data = ["31 i 1",
            "13 r 1",
            "13 c 1",
            "12 l 2",
            "23 c 1",
            "23 r 1"]
    circuit_data[:] = [Bipolar.make_from_std_annotation(f"{i + 1}" + data[i]) for i in range(len(data))]


# Режим работы программы в этом файле
if __name__ == "__main__":
    circuit_data: list[Bipolar] = []
    std_input()
    circ = CircuitCollection()
    circ.import_time_circuit(circuit_data)
