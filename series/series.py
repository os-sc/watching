import numbers
from nsfwenum import NSFW
from typeenum import Type
from genreenum import Genre
from statusenum import Status

class Series:
    def __init__(self, id):
        self._id        = id
        self._name      = ''
        self._alt_names = []
        self._season    = 0
        self._episode   = 0
        self._status    = None
        self._genres    = []
        self._type      = None
        self._nsfw      = None
        self._year      = None
        self._notes     = ''
        self._url       = ''
        self._img_url   = ''

    def __getattr__(self, attr):
        if attr == 'id':          return self._id
        elif attr == 'name':      return self._name
        elif attr == 'alt_names': return self._alt_names
        elif attr == 'season':    return self._season
        elif attr == 'episode':   return self._episode
        elif attr == 'status':    return self._status
        elif attr == 'genres':    return self._genres
        elif attr == 'type':      return self._type
        elif attr == 'nsfw':      return self._nsfw
        elif attr == 'year':      return self._year
        elif attr == 'notes':     return self._notes
        elif attr == 'url':       return self._url
        elif attr == 'img_url':
            if not self._img_url:
                return config.DEFAULT_THUMBNAIL_PATH
            return self._img_url
        elif attr == 'all_names':
            names = []
            names.append(self._name)
            names.extend(self._alt_names)
            return names
        else:
            raise AttributeError("'Series' has no attribute %r" % attr)

    def __setattr__(self, attr, val):
        if attr == 'id':
            self._id = val
        elif attr == 'name':
            self._name = val
        elif attr == 'add_alt_name':
            self._alt_names.append(val)
        elif attr == 'season':
            if isinstance(val, numbers.Number):
                self._season = val
        elif attr == 'episode':
            if isinstance(val, numbers.Number):
                self._episode = val
        elif attr == 'status':
            if Status.exists(val):
                self._status = Status.get(val)
        elif attr == 'add_genre':
            if Genre.exists(val):
                self._genres.append(Genre.get(val))
        elif attr == 'type':
            if Type.exists(val):
                self._type = Type.get(val)
        elif attr == 'nsfw':
            if NSFW.exists(val):
                self._nsfw = NSFW.get(val)
        elif attr == 'year':
            if val < 10000:
                self._year = val
        elif attr == 'notes':
            return self._notes
        elif attr == 'url':
            if val.startswith('http'):
                self._url = val
            else:
                self._url = 'http://' + val
        elif attr == 'img_url':
            return self._img_url
        else:
            self.__dict__[attr] = val

