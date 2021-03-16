"""from datetime import datetime
time_now = datetime.now()
print(time_now)"""
from datetime import datetime
#time_now =datetime.now()
#date.today()
#print(date.today().isoformat())

class Book:
    def __init__(self, title, isbn, author, total_pages):
        """

        :type isbn: object
        """
        self.title = title
        self.isbn = isbn
        self.author = author
        self.total_pages = total_pages
        self.published_at = None


    def publish(self):
        
        #print(bool(time_now))
        print(self.title, self.isbn, self.author, self.total_pages,self.published_at )
        self.published_at= datetime.now()

class Magazine(Book):
    def __init__(self, title, isbn, author, total_pages, volume, vol_date):
        super().__init__(title, isbn, author, total_pages)
        self.volume = volume
        self.volume_date = vol_date

    def view(self):
        """

        :rtype: object
        """
        print("Title:", self.title, "\n isbn number:", self.isbn, " \nAUTHOR :", self.author, "\ntotal pages:" ,self.total_pages,"\nvolume:", self.volume,
              '\nvolume date', self.volume_date,)


obj = Magazine("Python", '28', "ATHEEEE", "5566", "myyyyyy", "5732e5676e5723e")
obj2= Book("aaaa","aaaaaaaaaaa","aaaaaaaa","aaaaaaaaaaa")
obj2.publish()


obj.view()
