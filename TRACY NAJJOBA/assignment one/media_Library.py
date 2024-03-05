'''
This code demonstrates the application of SOLID principles in a media library context. The Single Responsibility Principle (SRP) is adhered to by separating concerns into different classes for books and movies, ensuring each class has a single responsibility.
 The Open/Closed Principle (OCP) is implemented in the MediaLibrary, which is designed to be open for extension (e.g., adding new media types) but closed for modification. The Liskov Substitution Principle (LSP) is respected, allowing subclasses (Book, Movie) to be used interchangeably without affecting the overall behavior.
The Interface Segregation Principle (ISP) is applied by potentially creating specific interfaces for different media types, making the system more flexible. Finally, the Dependency Inversion Principle (DIP) is observed by having both high-level (MediaLibrary) and low-level (Book, Movie) modules depend on the abstract Media class, reducing dependency on concrete implementations.
'''

class MediaLibrary:
    def __init__(self):
        self.media_list = []

    def add_media(self, media):
        if isinstance(media, Book):
            self.add_book(media)
        elif isinstance(media, Movie):
            self.add_movie(media)
        

    def add_book(self, book):
        # adding a book to library
        pass

    def add_movie(self, movie):
        # adding a movie to library
        pass

class Book:
    # Book related methods
    pass

class Movie:
    # Movie related methods
    pass
