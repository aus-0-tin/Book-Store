from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL (SQLite in this case)
DATABASE_URL = 'sqlite:///books.db'

# Create an engine
engine = create_engine(DATABASE_URL)

# Define a base class for the declarative model
Base = declarative_base()

# Define the Book class
class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    author = Column(String, nullable=False)
    pages = Column(Integer, nullable=False)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session maker
Session = sessionmaker(bind=engine)

def main():
    # Initialize a session
    session = Session()
    
    choice = 0
    while choice != 4:
        print("*** Books Manager ***")
        print("1) Add a book")
        print("2) Lookup a book")
        print("3) Display books")
        print("4) Quit")
        choice = int(input())
        
        if choice == 1:
            print("Adding a book...")
            nBook = input("Enter the name of the book >>> ")
            nAuthor = input("Enter the name of the author >>> ")
            nPages = int(input("Enter the number of pages >>> "))
            new_book = Book(name=nBook, author=nAuthor, pages=nPages)
            session.add(new_book)
            session.commit()
            print("Book added successfully.")
        
        elif choice == 2:
            print("Looking up for a book...")
            keyword = input("Search book by name: ")
            books = session.query(Book).filter(Book.name.contains(keyword)).all()
            if books:
                for book in books:
                    print(f"ID: {book.id}, Name: {book.name}, Author: {book.author}, Pages: {book.pages}")
            else:
                print("No books found.")
        
        elif choice == 3:
            print("Displaying all books...")
            books = session.query(Book).all()
            if books:
                for book in books:
                    print(f"ID: {book.id}, Name: {book.name}, Author: {book.author}, Pages: {book.pages}")
            else:
                print("No books available.")
        
        elif choice == 4:
            print("Quitting Program")
    
    # Close the session
    session.close()
    print("Program Terminated!")

if __name__ == "__main__":
    main()
