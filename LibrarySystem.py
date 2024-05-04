# Define a Library class to manage available and borrowed books.
class Library:
    # Initialize the library with available and borrowed books.
    def __init__(self):
        self.availableBooks = {
             "Pride and Prejudice": "Jane Austen",
            "1984": "George Orwell",
            "Crime and Punishment": "Fyodor Dostoevsky",
            "Hamlet": "William Shakespeare",
            "One Hundred Years of Solitude": "Gabriel García Márquez",
            "Anna Karenina": "Leo Tolstoy",
            "The Odyssey": "Homer",
            "The Stranger": "Albert Camus",
            "The Brothers Karamazov": "Fyodor Dostoevsky",
            "Lolita": "Vladimir Nabokov",
            "Great Expectations": "Charles Dickens",
            "The Old Man and the Sea": "Ernest Hemingway"
        }
        self.borrowedBooks = {}

    # Display the available books in the library.
    def displayAvailableBooks(self):
        print("\nAVAILABLE BOOKS\n")

        for bookName, author in self.availableBooks.items():
            print(f"Book Name : {bookName}\nAuthor : {author}\n")

    # Borrow a book from the library.
    def borrowBooks(self, bookToBorrow):
        if bookToBorrow in self.availableBooks:
            # Move the book from available to borrowed.
            author = self.availableBooks.pop(bookToBorrow)
            self.borrowedBooks[bookToBorrow] = author

            print(f"\nBook : {bookToBorrow}\nAuthor : {author}\nSuccessfully borrowed!")

        else:
            print(f"\nBook : {bookToBorrow} doesn't exist in the bookshelf")

    # Display the borrowed books.
    def displayBorrowedBooks(self):
        print("\nLIST OF BORROWED BOOKS\n")

        for borrowedBookName, borrowedAuthorName in self.borrowedBooks.items():
            print(f"Book Name : {borrowedBookName}\nAuthor : {borrowedAuthorName}\n")

# Initialize the library system.
librarySystem = Library()
print("Welcome To Library System!")
username = input("Enter your name to start : ")
librarySystem.displayAvailableBooks()

# Allow users to borrow books until they're done.
while True:
    userBorrowBook = str(input("\nEnter the name of the book you want to borrow : "))
    librarySystem.borrowBooks(userBorrowBook)

    userBorrowAgain = str(input("Do you want to borrow more books? (y/n)?: ")).lower()

    if userBorrowAgain != "y":
        break

# Display the borrowed books when finished.
librarySystem.displayBorrowedBooks()
print("Thank You For Visiting Library System!")
