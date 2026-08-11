#Library System
#Build a simple library system using a class. Each book is an object. Your system lets users borrow and return books and tracks whether each book is currently available.

#What you need to use
#------------------------------------------------------------------------
#1.  Book class      →  __init__ sets title, author, and is_borrowed = False
#2.  borrow()        →  sets is_borrowed to True and prints a confirmation
#3.  return_book()   →  sets is_borrowed to False and prints a confirmation
#4.  3 Book objects  →  demonstrate both borrow() and return_book()
#5.  self            →  used to access and update attributes inside methods
#------------------------------------------------------------------------
#
#What you'll be marked on
#------------------------------------------------------------------------
#1.  Book class with __init__ setting title, author, is_borrowed   →   5 marks
#2.  borrow() sets is_borrowed True and prints confirmation         →  10 marks
#3.  return_book() sets is_borrowed False and prints confirmation   →  10 marks
#4.  At least 3 Book objects with both methods demonstrated         →  10 marks
#5.  Program runs without any errors                                →   5 marks
#========================================================================
#Total  →  40 marks
#========================================================================

class Library:

    def Book1(self, title, author):
        self.title = title
        self.author = author
        title = "Harry Potter"
        author = "J.K. Rowling"
        print("Here is the name of the book", self.title ,"Here is the author of the book", self.author)

    def Book2(self, title, author):
        self.title = title
        self.author = author
        title = "Percy Jackson"
        author = "Rick Riordan"

print(Library.Book1)