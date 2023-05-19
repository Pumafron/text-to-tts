import time
class Voz:
    def __init__(self,voz,tone=0,pitch=0,prefix="default:",sapi=5) -> None:
        self.voz = voz
        self.pitch = pitch
        self.rate = tone
        self.prefix = prefix
        self.sapi = sapi
    def generateDic(self):
        return {
            "prefix":self.prefix,
            "voice":self.voz,
            "rate":self.rate,
            "pitch":self.pitch
        }


def timeis(func):
    '''Decorator that reports the execution time.'''
  
    def wrap(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
          
        print(func.__name__, end-start)
        return result
    return wrap