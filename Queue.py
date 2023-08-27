from DataStructures import DataStructures


class Queue(DataStructures):
    """
    Queue Implementation
    """

    def __init__(self):
        super().__init__()

    def enqueue(self, value: any) -> None:
        """
        Add value to the start of the queue
        """
        self._addNodeAtFirst(value)
