from enum import Enum
from .. import config

class Type(Enum):
    TV      = 1
    Movie   = 2
    OVA     = 3
    Special = 4

    @classmethod
    def exists(cls, name):
        try:
            cls[name]
            return True
        except KeyError:
            return False

    @classmethod
    def get(cls, name):
        try:
            return cls[name]
        except KeyError:
            return None

    @classmethod
    def get_string(cls, name):
        try:
            return cls[name]
        except KeyError:
            return None

    @classmethod
    def get_all(cls):
        all = []
        for i in inspect.getmembers(cls):
            if not i[0].startswith('_'):
                all.append(i[0])
        return all

