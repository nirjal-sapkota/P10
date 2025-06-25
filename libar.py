class Library:
    def __init__(self, list_of_books, name):
        self.bookList = list_of_books
        self.name = name
        self.lendDict = {}
    
    def displayBooks(self):
        print(f"We have the following books in our library: {self.name}")
        for book in self.bookList:
            print(book)
    def lendBook(self, user, book):
        if book not in self.bookList:
            print("Sorry this book is not available")
        elif book in self.lendDict:
            print("The book is already being used by {self.lendDict[book]}")
        else:
            self.lendDict[book] = user
            print("Lender-Book database has been updated. You can take the book now ")
    def addBook(self, book):
        self.bookList.append(book)
        print(f"{book} has been added to th book list")
    def returnBook(self, book):
        if book in self.lendDict:
            del self.lendDict[book]
            print("Book has been returned")
        else:
            print("That book was not borrowed from us.")
if __name__ == '__main__':
    books = Library([
        'Python', 'Rich dad poor dad', 'Harry pottor', 'Th tale of Nayan'
    ], "Let's Upskill")
    user_name = input("Welcome to the Lajrin's Library, what is your name?")
    
    while True:
        print(
            f"\nHello {user_name}, welcome to the {books.name} libary. Please choose an option:"
        )
        print("1. Display Books\n2. Lend a book\n3. Add a book\n4. Return a book\n5. Quit")
        user_choice = input("Enter your choice to continue")
        if user_choice not in ['1', '2', '3', '4', '5']:
            print("Enter the correct one")
            continue
        if user_choice == '1':
            books.displayBooks()
        elif user_choice == '2':
            book = input("Ente the name of the book to lend")
            books.lendBook(user_name, book)
        elif user_choice == '3':
            book = input("Ente the name of the book to add")
            books.addBook(book)
        elif user_choice == '4':
            book = input("Ente the name of the book to return")
            books.returnBook(book)
        elif user_choice == '5':
            print(f"Thanks for using us!, {user_name}. Goodbye!")
            break




