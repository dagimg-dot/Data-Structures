from DataStructures import DataStructures

class Stack(DataStructures):
    def __init__(self):
        super().__init__()

    def push(self, value: any) -> None:
        self._addNodeAtEnd(val=value)
    
    def pop(self) -> None:
        self._deleteNodeAtEnd()
    