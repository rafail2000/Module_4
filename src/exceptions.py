class ZeroProductQuantity(Exception):
    """ Класс для обработки исключений """

    def __init__(self, message=None):
        super().__init__(message)
