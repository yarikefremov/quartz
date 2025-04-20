from circuit import *

#1.Получение цепи
#Примерный ввод:
#Количество элементов: 5
#Элемент 1: 112 i 5 (id+положение, тип, значение величины)
def input_from_console(circuit_data: list[Bipolar]):
    amount_bipolar = int(input("Количество элементов: "))
    print("Пример ввода: 112 i 5")
    # Список двухполюсников
    circuit_data[:] = [Bipolar.make_from_std_annotation(input(f"Элемент {s + 1}: ")) for s in range(amount_bipolar)]


def std_input(circuit_data: list[Bipolar]):
    src_data = ["131 i 1",
                "213 r 1",
                "313 c 1",
                "412 l 2",
                "523 c 1",
                "623 r 1"]
    circuit_data[:] = [Bipolar.make_from_std_annotation(src_data[s]) for s in range(len(src_data))]


#Режим работы программы в этом файле
if __name__ == "__main__":
    circuit_data: list[Bipolar] = []
    std_input(circuit_data)
