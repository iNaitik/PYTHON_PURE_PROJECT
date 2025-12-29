class Book:
    def __init__(self,book_id,title,author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False
        self.issued_to = None

    def issue_to(self,member_id):
        self.issued_to = member_id
        self.is_issued = True
    def return_book(self):
        self.issued_to = None
        self.is_issued = False
    def __str__(self):
        status_info = None
        issued_info = None
        if self.is_issued:
            status_info = "Issued"
        else:
            status_info = "Available"
        if self.issued_to:
            issued_info = f"Issued to {self.issued_to}"
        else:
            issued_info = "N/A"

        return f"Book ID: {self.book_id} || Title: {self.title} || Author: {self.author} || Issued: {status_info} || Issued to: {issued_info}"

class Member:
    def __init__(self,member_id, name):
        self.member_id = member_id
        self.name = name
        self.issued_books = []
    
    def add_book(self,book_id):
        self.issued_books.append(book_id)

    def remove_book(self,book_id):
        self.issued_books.remove(book_id)
    
    def __str__(self):
        if self.issued_books:
            books = ", ".join(self.issued_books)
        else:
            books = "None"

        return f"ID: {self.member_id} || Name: {self.name} || Books: {books}"
    
class Library:
    def __init__(self,MAX_ISSUE_LIMIT = 3):
        self.books = {}
        self.members = {}
        self.MAX_ISSUE_LIMIT = MAX_ISSUE_LIMIT
        
    def add_book(self,book_id,title,author):
        if book_id in self.books:
            print("Book already exist")
        else:
            self.books[book_id] = Book(book_id,title,author)  #Class Book object is created stores refrence
            print("BOOK ADDED SUCESSFULLY!!")
    def add_member(self,member_id,name):
        if member_id in self.members:
            print("Member already exixts")
        else:
            self.members[member_id] = Member(member_id,name)
            print("MEMBER ADDED SUCESSFULLY!!")
    def issue_book(self,book_id,member_id):
        if book_id not in self.books:
            print("Book not exists")
            return
        if member_id not in self.members:
            print("Member Not exists")
            return
        book = self.books[book_id]  #Now above refrence goes to book
        member = self.members[member_id]
        if book.is_issued:
            print("Book is Issued to someone")
            return
        if len(member.issued_books) >= 3:
            print("MAX LIMIT OF BOOK REACHED")
            return
        book.issue_to(member_id)
        member.add_book(book_id)
        print("BOOK ISSUED SUCESSFULLY!!")
    def return_book(self, book_id, member_id):
        if book_id not in self.books:
            print("Book does not exist")
            return
        if member_id not in self.members:
            print("Member does not exist")
            return
        book = self.books[book_id]
        member = self.members[member_id]
        if not book.is_issued:
            print("Book is not issued")
            return
        if book_id not in member.issued_books:
            print("This book is not issued to you")
            return
        book.return_book()
        member.remove_book(book_id)
        print("Book returned successfully")
    def view_books(self):
        if not self.books:
            print("There is no books in the library")
            return
        print("----LIBRARY BOOKS----")
        for i,bookk in enumerate(self.books.values()):
            print(f"{i+1}.{bookk}")
            
    def view_members(self):
        if not self.members:
            print("No members in the library")
            return
        print("\n--- Library Members ---")
        for j,member in enumerate(self.members.values()):
            print(f"{j+1}.{member}")

library = Library()  
if __name__ == "__main__":
    while True:
        print("\nLIBRARY MANAGEMENT SYSTEM MENU:")
        print("1. Add Book")
        print("2. Add Members")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. View Book")
        print("6. View Members")
        print("7. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            library.add_book(book_id, title, author)

        elif choice == '2':
            member_id = input("Enter Member ID: ")
            name = input("Enter Member Name: ")
            library.add_member(member_id, name)

        elif choice == '3':
            book_id = input("Enter Book ID: ")
            member_id = input("Enter Member ID: ")
            library.issue_book(book_id, member_id)

        elif choice == '4':
            book_id = input("Enter Book ID: ")
            member_id = input("Enter Member ID: ")
            library.return_book(book_id, member_id)

        elif choice == '5':
            library.view_books()

        elif choice == '6':
            library.view_members()

        elif choice == '7':
            print("Exiting LMS. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")