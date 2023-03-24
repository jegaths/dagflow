import logging
class Logger:
    """
    Logger class is to log information to the console.
    ...
    """

    def __new__(cls):
        super().__new__(cls)
        __format = "%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s"
        logging.basicConfig(level=logging.INFO, format=__format)

        return logging.getLogger(__name__)
