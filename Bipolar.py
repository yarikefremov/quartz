class Bipolar:
    # Example: 1 12 i 5
    # b_ means bipolar
    # не более 9 элементов в цепи, не более 9 узлов в цепи
    def __init__(self, b_id: int, init_node: int, end_node: int, b_type: str, value: int):
        self.b_id: int = b_id
        self.init_node: int = init_node
        self.end_node: int = end_node
        self.b_type: str = b_type
        self.value: int = value

    @staticmethod
    def make_from_std_annotation(annotation: str):
        if len(annotation) < 7:
            print("Bipolar.make_from_std_annotation: Слишком маленькая аннотация. Должно быть как минимум 7 символов")
            return
        return Bipolar(b_id=int(annotation[0]),
                       init_node=int(annotation[1]),
                       end_node=int(annotation[2]),
                       b_type=annotation[4],
                       value=int(annotation[6:]))  # возможно стоит проверку на isnumeric сделать