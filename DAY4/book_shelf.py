class bookshelf:
    def __init__(self,book,magazine):
        self.book= book
        self.magazine= magazine
list =[]
list.append(bookshelf('book1','jchgdchghfdcggc'))

for i in list:
    print(i.book,i.magazine)
