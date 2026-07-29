class QueueError(IndexError):  # Choose base class for the new exception.
    pass

class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.insert(0, elem)

    def get(self):
        if self.isempty():
            raise QueueError
        elem = self.__queue[-1]
        del self.__queue[-1]
        return elem
    def isempty(self):
        return (len(self.__queue) == 0)
