class Library:   
    def __init__(self):
        self.books_list = []
        self.counter = 0 
    def add_books(self,books):
        self.books_list.append(books)
        self.counter = self.counter+1
        
    def show_books(self):
        print(f"the books present in the library is {self.books_list} and length is {self.counter} original length is {len(self.books_list)}")
        
new_library = Library()  
new_library.add_books("java book")
new_library.add_books("python book")
new_library.add_books("javascript books")
new_library.show_books()