from DataStructures import DataStructures


class Stack(DataStructures):
    def __init__(self):
        super().__init__()

    def push(self, value: any) -> None:
        """
        Push value to the top of the stack
        """
        self._addNodeAtEnd(val=value)