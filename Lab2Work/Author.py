# Public Static Void Main (String[] args){}
def main():
    # Init a name and his list of books

    Jordan_Peterson = Author('Jordan B Peterson')

    Jordan_Peterson.publish('Maps of Meaning')
    Jordan_Peterson.publish('Beyond Order')
    Jordan_Peterson.publish('12 Rules For Life')
    Jordan_Peterson.publish('12 Rules For Life')

    print(Jordan_Peterson)

    DrSeuss = Author('Dr. Seuss')

    DrSeuss.publish('Cat in the Hat')

    print(DrSeuss)

    Jay = Author('Jay')
    print(Jay)


# Author Class
class Author:
    # books = None because if Books = [] is inside the parameters, it will be shared across all instance of the class being used. So there maybe books from other authors that don't belong to them. Meaning the list will be shared across other Authors
    def __init__(self, authorName, books=None):
        self.authorName = authorName

        # If books is None, initiate a array, else keep it being None.
        if books is None:
            self.books = []
        else:
            self.books = books

    def publish(self, bookTitle):

        # Duplicate book error handling
        if bookTitle in self.books:
            print(f'Error adding "{bookTitle}", duplicate book added. ')
        else:
            self.books.append(bookTitle)

    # String method to convert object code to readable print lines

    def __str__(self):
        # Author name and their books published
        if len(self.books) > 0:
            book_list = ', '.join(self.books)
            return f'Author Name: {self.authorName}\nList of books: {book_list}'
        else:
            return f'Author Name: {self.authorName}\nList of books: No Books Published So Far!'

# Can also use truthy and falsy statements like in JavaScript. Python uses 'or' keyword rather in Javascript it is implicit when you put conditions together.
    # titles = book_list = ', '.join(self.books) or No Books Published So far!


# Calling main here
if __name__ == '__main__':
    main()
