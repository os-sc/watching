from enum import Enum

class Genre(Enum):
    Action        = 1
    Adventure     = 2
    Cars          = 3
    Comedy        = 4
    Dementia      = 5
    Demons        = 6
    Drama         = 7
    Ecchi         = 8
    Fantasy       = 9
    Hame          = 10
    Harem         = 11
    Hentai        = 12
    Historical    = 13
    Horror        = 14
    Josei         = 15
    Kids          = 16
    Magic         = 17
    Marial_Arts   = 18
    Mecha         = 19
    Military      = 20
    Music         = 21
    Mystery       = 22
    Parody        = 23
    Police        = 24
    Psychological = 25
    Romance       = 26
    Samurai       = 27
    School        = 28
    SciFi         = 29
    Seinen        = 30
    Shoujo        = 31
    Shoujo_Ai     = 32
    Shounen       = 33
    Shounen_Ai    = 34
    Slice_of_Life = 35
    Space         = 36
    Sports        = 37
    Super_Power   = 38
    Supernatural  = 39
    Thriller      = 40
    Vampire       = 41
    Yaoi          = 42
    Yuri          = 43

    @classmethod
    def exists(cls, name):
        try:
            cls[name.replace(' ', '_')]
            return True
        except KeyError:
            return False

    @classmethod
    def get(cls, name):
        try:
            return cls[name.replace(' ', '_')]
        except KeyError:
            return None

    @classmethod
    def get_string(cls, name):
        try:
            return cls[name].name.replace('_', ' ')
        except KeyError:
            return None

    @classmethod
    def get_all(cls):
        all = []
        for i in inspect.getmembers(cls):
            if not i[0].startswith('_'):
                all.append(i[0])
        return all

