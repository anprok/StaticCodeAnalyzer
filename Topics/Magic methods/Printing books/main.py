class Book:
    def __init__(self, author, title, price, book_id):
        self.author = author
        self.title = title
        self.price = price
        self.book_id = book_id

    # define the necessary method here
    def __str__(self):
        return "{title} by {author}. ${price}. [{book_id}]".format(title=self.title,
                                                                   author=self.author,
                                                                   price=self.price,
                                                                   book_id=self.book_id)
