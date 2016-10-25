from enum import Enum

class NSFW(Enum):
    sfw  = 1
    some = 2
    nsfw = 3

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

