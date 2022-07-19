import sqlite3

from datetime import datetime

class DataBaseManager(object):
    def __init__(self, db_file="tweets.db"):
        self.dbpath = db_file

        self.conn = sqlite3.connect(self.dbpath)
        self._create_tables()

    def _open_cursor(self):
        cursor = self.conn.cursor()
        return cursor

    def _close_cursor(self, cursor):
        cursor.close()

    def _create_tables(self):
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

    def insert(self, tweet_id, tweet_user_id, content, tweet_date):
        cursor = self._open_cursor()
        try:
            current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            req = f'INSERT INTO tweets(tweet_id, twitter_user_id, content, tweet_date, date) VALUES ({int(tweet_id)}, {int(tweet_user_id)}, "{content}", "{tweet_date}", "{current_date}")'
            
            cursor.execute(req)
            # Save (commit) the changes
            self.conn.commit()
            print("tweet successful save!")
        except Exception as e:
            print("An error occurs")
            print(e)
        self._close_cursor(cursor)

    def select_all(self):
        result = []
        cursor = self._open_cursor()
        req = "SELECT id, tweet_id, twitter_user_id, content, tweet_date, date FROM tweets"
        cursor.execute(req)
        result = cursor.fetchall()
        self._close_cursor(cursor)

        return result

    def select_by_id(self, key):
        cursor = self._open_cursor()
        req = f"SELECT id, tweet_id, twitter_user_id, content, tweet_date, date FROM tweets WHRE id={key}"
        cursor.execute(req)
        result = cursor.fetchall()
        self._close_cursor(cursor)

        if len(result) > 0:
            return result[0]
        else:
            return None