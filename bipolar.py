class Bipolar:
    # Example: 1 12 i 5
    # b_ means bipolar
    # не более 9 элементов в цепи, не более 9 узлов в цепи
    def __init__(self, b_id: int, pos: int, b_type: str, value: int):
        self.b_id: int = b_id
        self.init_node: int = pos // 10
        self.end_node: int = pos % 10
        self.b_type: str = b_type
        self.value: int = value

    @staticmethod
    def make_from_std_annotation(annotation: str):
        if len(annotation) < 7:
            print("Bipolar.make_from_std_annotation: Слишком маленькая аннотация. Должно быть как минимум 7 символов")
            return
        return Bipolar(b_id=int(annotation[0]),
                       pos=int(annotation[1:3]),
                       b_type=annotation[4],
                       value=int(annotation[6:]))  # возможно стоит проверку на isnumeric сделать