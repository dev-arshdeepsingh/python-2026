import sqlite3

con = sqlite3.connect("videos.db")

cursor = con.cursor()

cursor.execute('''create table if not exists videos(
               id integer primary key,
               name text not null,
               time text not null
                )''')

def view_videos():
    print("\n", "*" * 70, "\n")
    cursor.execute('''select * from videos''')
    for row in cursor.fetchall():
        print(row)
    print("\n", "*" * 70, "\n")

    
def add_videos():
    name = input("Enter Name: ")
    time = input("Enter Duration: ")

    cursor.execute('''insert into videos (name,time)
                   values
                   (?,?)
                   ''',(name,time))
    con.commit()
    print("Video Added!")

def update_videos():
    view_videos()
    index = int(input("Enter Video's Id: "))
    name = input("Enter new name: ")
    time = input("Enter new time: ")
    cursor.execute('''update videos set name = ?, time = ? where id = ?''',(name,time,index))
    con.commit()
    print("Video Updated!")

def delete_videos():
    view_videos()
    index = int(input("Enter Video's id for deletion: "))
    cursor.execute('''delete from videos where id = ?''',(index,))
    con.commit()
    print("Video Deleted!")

def main():
    while True:
        print("\n" * 5)
        print("Welcome To Youtube Manager!")
        print("Press 1 to View Database")
        print("Press 2 to Add Videos")
        print("Press 3 to Update Videos")
        print("Press 4 to Delete Videos")
        print("Press 5 to Exit")

        choice = int(input("Enter Your Choice: "))

        match choice:
            case 1:
                view_videos()
            case 2:
                add_videos()
            case 3:
                update_videos()
            case 4:
                delete_videos()
            case 5:
                break
            case _:
                print("Invalid Input!")
    con.close()



if __name__ == "__main__":
    main()

#.commit() saves/delete file permanently to database, without if we delete then things will delete for now but when we do con.close() and then reopen database things will be still there ie .commit() do the permanent changes in database. 