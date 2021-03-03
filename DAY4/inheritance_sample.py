class Book:
     def __init__(self , title,isbn,author,totalpages):
          self.title = title
          self.isbn = isbn
          self.author = author
          self.totalpages = totalpages
     def publish(self):
         print(self.title ,self.isbn,self.author, self.totalpages)
class Magazine(Book):
     def __init__(self ,title ,isbn,author,totalpages):
          Book.__init__(self,title,author,isbn,totalpages)
          self.volium= "vol 1"
          self.voluim_date="hgjdgjhwdgxdjggxsegdxjhxdgh"
     def view(self):
          print("Title:" , self.title ,"\nisbn number:",  self.isbn , " \nAUTHOR :" , self.author,"\nvolium:",self.volium,"\nvolium date",self.voluim_date)
obj = Magazine("Python" , '28',"ATHEEEE","5566")

obj.view()

   
    
    
    
        

