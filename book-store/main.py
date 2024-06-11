from __init__ import CURSOR, CONN

def main():
        
        # initialize books list
    booksList = []
    
    choice = 0
    while choice !=4:
        print("*** Books Manager ***")
        print("1) Add a book")
        print("2) Lookup a book")
        print("3) Display books")
        print("4) Quit")
        choice = int(input())
        
        if choice == 1:
            print("Addig a book...")
            nBook = input("Enter the name of the book >>>")
            nAuthor = input("Enter the name of the author >>>")
            nPages = input("Enter the number of pages >>>")
            booksList.append([nBook, nAuthor, nPages])
        
        elif choice == 2:
            print("Looking up for a book...")
            keyword = input("Search book by name: ")
            for book in booksList:
                if keyword in book:
                    print(book)
        
        elif choice == 3:
            print("Displaying all books...")
            for i in range(len(booksList)):
                print(booksList[i])
        
        elif choice == 4:
            print("Quitting Program")
    print("Program Terminated!")
    
    

if __name__ == "__main__":
    main()


    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            book TEXT,
            author TEXT,
            pages INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS books;
        """
        CURSOR.execute(sql)
        CONN.commit()

