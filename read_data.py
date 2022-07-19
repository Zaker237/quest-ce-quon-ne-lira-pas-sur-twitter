from database import DataBaseManager

DATABASE_PATH = "db/database.db"

db = DataBaseManager(DATABASE_PATH)

def main():
    datas = db.select_all()
    for data in datas:
        print("id: ", data[0])
        print("tweet'id: ", data[1])
        print("tweet's user's id: ", data[2])
        print("tweet: ", data[3])
        print("tweet's date: ", data[4])
        print("date: ", data[5])
        print("\n\n")


if __name__ == "__main__":
    main()