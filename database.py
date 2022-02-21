from datetime import datetime

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
        cursor = self._open_cursor()
        table = """create table tweets (
            id int,
            tweet_id int,
            twitter_user_id int,
            content text,
            tweet_date text,
            date text,
        )"""
        cursor.execute(table)
        self._close_cursor(cursor)

    def inset(self, tweet_id, tweet_user_id, content, tweet_date):
        cursor = self._open_cursor()
        current_data = datetime.now()
        req = f"""insert into tweets
          values ({tweet_id}, {tweet_user_id}, {content}, {tweet_date}, {current_date})
        """
        cursor.execute(req)

        # Save (commit) the changes
        self.conn.commit()
        self._close_cursor(cursor)

    def save_db_as_text_file(self, path):
        cursor = self._open_cursor()

        self._close_cursor(cursor)