import sqlite3

# create the database
def create_database():
    conn = sqlite3.connect('book_keeper.db')
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS books
                 (id INTEGER PRIMARY KEY,
                 title TEXT NOT NULL,
                 author TEXT NOT NULL,
                 status TEXT NOT NULL,
                 rating INTEGER,
                 description TEXT)''')

    conn.commit()
    conn.close()

#  add a book
def add_book(title, author, status, rating=None, description=None):
    conn = sqlite3.connect('book_keeper.db')
    c = conn.cursor()

    # Insert book into the table
    c.execute("INSERT INTO books (title, author, status, rating, description) VALUES (?, ?, ?, ?, ?)",
              (title, author, status, rating, description))

    conn.commit()
    conn.close()

# edit a book
def edit_book(book_id, status=None, rating=None, description=None):
    conn = sqlite3.connect('book_keeper.db')
    c = conn.cursor()

    # Update book details based on provided parameters
    if status is not None:
        # Convert 't' or 'f' to 'Read' or 'Currently Reading'
        status = 'Read' if status.lower() == 't' else 'Currently Reading'
        c.execute("UPDATE books SET status = ? WHERE id = ?", (status, book_id))
    if rating is not None:
        c.execute("UPDATE books SET rating = ? WHERE id = ?", (rating, book_id))
    if description is not None:
        c.execute("UPDATE books SET description = ? WHERE id = ?", (description, book_id))

    conn.commit()
    conn.close()

# view all books 
def view_books():
    conn = sqlite3.connect('book_keeper.db')
    c = conn.cursor()

    # Select all books from the table and print them
    c.execute("SELECT * FROM books")
    books = c.fetchall()

    for book in books:
        print(book)

    conn.close()

#  view currently reading books
def view_currently_reading_books():
    conn = sqlite3.connect('book_keeper.db')
    c = conn.cursor()

    # Select currently reading books from the table and print them
    c.execute("SELECT * FROM books WHERE status = 'Currently Reading'")
    currently_reading_books = c.fetchall()

    if currently_reading_books:
        print("\nCurrently reading books:")
        for book in currently_reading_books:
            print(book)
    else:
        print("\nNo currently reading books found.")

    conn.close()

# Function to view badly rated books (ratings below or equal to 2)
def view_badly_rated_books():
    conn = sqlite3.connect('book_keeper.db')
    c = conn.cursor()

    # Select badly rated books from the table and print them
    c.execute("SELECT * FROM books WHERE rating <= 4")
    badly_rated_books = c.fetchall()

    if badly_rated_books:
        print("\nBadly rated books (Rating <= 4):")
        for book in badly_rated_books:
            print(book)
    else:
        print("\nNo badly rated books found.")

    conn.close()

# Function to find common authors
def find_common_authors():
    conn = sqlite3.connect('book_keeper.db')
    c = conn.cursor()

    # Select authors and count how many times they appear in the table
    c.execute("SELECT author, COUNT(*) as count FROM books GROUP BY author HAVING count > 1")
    common_authors = c.fetchall()

    if common_authors:
        print("\nCommon authors (appearing in more than one book):")
        for author, count in common_authors:
            print(f"{author}: {count} books")
    else:
        print("\nNo common authors found.")

    conn.close()

# Function to view highly rated books
def view_highly_rated_books():
    conn = sqlite3.connect('book_keeper.db')
    c = conn.cursor()

    # Select books with ratings over 5 from the table and print them
    c.execute("SELECT * FROM books WHERE rating > 5")
    highly_rated_books = c.fetchall()

    if highly_rated_books:
        print("\nHighly rated books (Rating > 5):")
        for book in highly_rated_books:
            print(book)
    else:
        print("\nNo highly rated books found.")

    conn.close()

# Main function to interact with the user
def main():
    create_database()

    while True:
        print("\nWhat would you like to do?")
        print("1. Add a book")
        print("2. Edit a book")
        print("3. View all books")
        print("4. View currently reading books")
        print("5. View badly rated books")
        print("6. Find common authors")
        print("7. View highly rated books")
        print("8. Exit")

        choice = input("Enter your choice (1, 2, 3, 4, 5, 6, 7, or 8): ")

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            status = input("Enter 't' if the book is read, 'f' if it's currently reading: ")
            rating = input("Enter the rating of the book (optional): ")
            if rating:
                rating = int(rating)
            description = input("Enter a description of the book (optional): ")
            add_book(title, author, status, rating, description)
            print("Book added successfully!")
        elif choice == '2':
            view_books()
            book_id = input("Enter the ID of the book you want to edit: ")
            status = input("Enter 't' if the book is read, 'f' if it's currently reading: ")
            rating = input("Enter the new rating of the book (optional): ")
            if rating:
                rating = int(rating)
            description = input("Enter the new description of the book (optional): ")
            edit_book(book_id, status, rating, description)
            print("Book updated successfully!")
        elif choice == '3':
            print("\nAll books:")
            view_books()
        elif choice == '4':
            view_currently_reading_books()
        elif choice == '5':
            view_badly_rated_books()
        elif choice == '6':
            find_common_authors()
        elif choice == '7':
            view_highly_rated_books()
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, 7, or 8.")

if __name__ == "__main__":
    main()


