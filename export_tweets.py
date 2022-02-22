import json
import sqlite3

DATABASE_PATH = "db/database.db"
FILE_PATH = "tweets/tweets.json"

def format_db_data(data):
    return {
        "id": data[0],
        "tweet_id": data[1],
        "twitter_user_id": data[2],
        "content": str(data[3]),
        "tweet_date": str(data[4]),
        "created_at": str(data[5]),
    }


def main():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    req = "SELECT * FROM tweets"
    cursor.execute(req)
    data = cursor.fetchall()
    cursor.close()
    
    with open(FILE_PATH, "w", encoding="utf-8") as fp:
        json.dump(
            list(map(format_db_data, data)),
            fp,
            indent=4,
            ensure_ascii=False
        )
    print(f"file {FILE_PATH} generated")

if __name__ == "__main__":
    main()