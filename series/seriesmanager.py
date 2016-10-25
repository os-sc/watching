from seriesdatabase import SeriesDatabase

class SeriesManager:
    def __init__(self, dbpath):
        self._db = SeriesDatabase(dbpath)

    def add_series(self, series):
        assert not self._id_already_exists(series.id)
        self._db.add_item(series)
        self._db.save_changes()

    def add_multiple_series(self, series_list):
        for s in series_list:
            self._add_series_to_cache(s)
        self._db.save_changes()

    def overwrite_series(self, series):
        pass

    def get_all(self):
        return self._db.get_all()

    def get_by_id(self, sid):
        for s in self.get_all():
            if s.id == sid:
                return s
        return None

    def get_by_name(self, name):
        results = []
        for s in self.get_all():
            names = ''.join(s.all_names)
            if name.lower() in names.lower():
                results.append(s)
        return results

    def get_by_status(self, status):
        return filter(lambda s: s.status == status, self.get_all())

    def _add_series_to_cache(self, series):
        assert not self._id_already_exists(series.id)
        self._db.add_item(series)

    def _id_already_exists(self, id):
        for s in self._db.get_all():
            if s.id == id:
                return True
        return False

