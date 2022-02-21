

class DateBaseManager(object):
    def __init__(self, db_file="tweets.db"):
        self.dbpath = db_file

        self.conn = sqlite3.connect(self.dbpath)

    def _open_cursor(self):
        cursor = self.conn.cursor()
        return cursor

    def _close_cursor(self, cursor):
        cursor.close()

    def _create_tables(self):
        pass

    def inset(self):
        cursor = self._open_cursor()

        self._close_cursor(cursor)

    def save_db_as_text_file(self, path):
        cursor = self._open_cursor()

        self._close_cursor(cursor)