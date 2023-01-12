import sqlite3 as lite

# functionality goes here

class DatabaseManage(object):

    def __init__(self):
        # global variable for database connection
        global con
        try:
            # Connect to the database and create the table if it does not exist
            con = lite.connect('courses.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            # Print an error message if the connection or table creation fails
            print("Unable to create a DB !")

    # Method for inserting data into the database
    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO course(name, description, price, is_private) VALUES (?,?,?,?)", data
                    )
                return True
        except Exception:
            # Return false if the insert fails
            return False

    # Method for fetching all data from the database
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM course")
                # Return the fetched data
                return cur.fetchall()
        except Exception:
            # Return false if the fetch fails
            return False

    # Method for deleting data from the database
    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM course WHERE id = ?"
                cur.execute(sql, [id])
                return True
        except Exception:
            # Return false if the delete fails
            return False

# Provide an interface for the user to interact with the class
def main():
    print("*"*40)
    print("\n:: COURSE MANAGEMENT :: \n")
    print("*"*40)
    print("\n")

    db = DatabaseManage()

    print("#"*40)
    print("\n :: User Manual :: \n")
    print("#"*40)

    print('\nPress 1. Insert a new Course\n')
    print('Press 2. Show all courses\n')
    print('Press 3. Delete a course (NEED ID OF COURSE)\n')
    print("#"*40)
    print("\n")

    choice = input("\n Enter a choice: ")

    if choice == "1":
        name = input("\n Enter course name: ")
        description = input("\n Enter course description: ")
        price = input("\n Enter course price: ")
        private = input("\n Is this course private (0/1): ")

        if db.insert_data([name, description, price, private]):
            print("Course was inserted successfully")
        else:
            print("OOPS SOMEthing is wrong")


    elif choice==2:
        print("\n:: Course List ::")

        for index, item in enumerate(db.fetch_data()):
            print("\n Sl no : " + str(index + 1))
            print("Course ID : " + str(item[0]))
            print("Course Name : " + str(item[1]))
            print("Course description : " + str(item[2]))
            print("Course Price : " + str(item[3]))
            private = 'Yes' if item[4] else 'NO'
            print("Is Private : " + private)
            print("\n")
    
    elif choice==3:
        record_id  = int(input("Enter course id: "))
        if db.delete_data(record_id):
            print("Deleted")
        else:
            print("Something went wrong")

    else:
        print("\n BAD CHOICE")

if __name__ == '__main__':
    main()
