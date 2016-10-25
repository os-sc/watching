from os import path
import jsonpickle

class SeriesDatabase:
    def __init__(self, dbpath):
        self._dbpath = dbpath
        if not path.isfile(dbpath):
            self._dbcache = []
            self.save_changes()
        self.refresh_cache()

    def refresh_cache(self):
        with open(self._dbpath, 'r') as f:
            content = f.read()
            if not content:
                self._dbcache = []
            else:
                self._dbcache = jsonpickle.decode(content)

    def save_changes(self):
        json = self.dump_cache()
        with open(self._dbpath, 'w') as f:
            f.write(json)

    def add_item(self, item):
        self._dbcache.append(item)

    def dump_cache(self):
        return jsonpickle.encode(self._dbcache)

    def get_all(self):
        return self._dbcache

    def _serialize_series(self, series):
        return jsonpickle.encode(series)


