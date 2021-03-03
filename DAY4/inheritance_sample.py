class Book:
    def __init__(self, title, isbn, author, totalpages):
        """

        :type isbn: object
        """
        self.title = title
        self.isbn = isbn
        self.author = author
        self.totalpages = totalpages

    def publish(self):
        print(self.title, self.isbn, self.author, self.totalpages)


class Magazine(Book):
    def __init__(self, title, isbn, author, totalpages, volume, vol_date):
        super().__init__(title, author, isbn, totalpages)
        self.volume = volume
        self.volume_date = vol_date

    def view(self):
        """

        :rtype: object
        """
        print("Title:", self.title, "\n isbn number:", self.isbn, " \nAUTHOR :", self.author, "\nvolume:", self.volume,
              '\nvolume date', self.volume_date)


obj = Magazine("Python", '28', "ATHEEEE", "5566", "myyyyyy", "5732e5676e5723e")

obj.view()
