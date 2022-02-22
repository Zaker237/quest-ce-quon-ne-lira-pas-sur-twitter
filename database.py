import sqlite3

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

    def create_tables(self):
        cursor = self._open_cursor()
        table = """CREATE TABLE IF NOT EXISTS tweets (
            id INTEGER PRIMARY KEY,
            tweet_id BIGINT,
            twitter_user_id BIGINT,
            content TEXT,
            tweet_date varchar(255),
            date varchar(255)
        )"""
        cursor.execute(table)
        self._close_cursor(cursor)

    def inset(self, tweet_id, tweet_user_id, content, tweet_date):
        cursor = self._open_cursor()
        try:
            current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            req = f'INSERT INTO tweets(tweet_id, twitter_user_id, content, tweet_date, date) VALUES ({int(tweet_id)}, {int(tweet_user_id)}, "{content}", "{tweet_date}", "{current_date}")'
            print(req)
            cursor.execute(req)
            # Save (commit) the changes
            self.conn.commit()
            print("tweet successful save!")
        except Exception as e:
            print("An error occurs")
            print(e)
        self._close_cursor(cursor)

    def save_db_as_text_file(self, path):
        cursor = self._open_cursor()

        self._close_cursor(cursor)