#python
import logging
class mylogger:
    
    def __init__(self,str):
        logging.basicConfig(filename="f:\\temp.txt",filemode='a', level=logging.DEBUG)
        self.logger=logging.getLogger("logger")
        fh=logging.FileHandler(str,'a')
        fh.setLevel(logging.DEBUG)
        # fh.setFormatter(logging.Formatter('[%(asctime)s]%(filename)-1s:%(funcName)-1s:%(message)s'))
        fh.setFormatter(logging.Formatter('[%(asctime)s]%(funcName)-1s:%(message)s'))
        self.logger.addHandler(fh)
    
    def getLogger(self):
        return self.logger

mylogger=mylogger('F:\\adebug.txt')

def debug(str):
    mylogger.getLogger().debug(str)


