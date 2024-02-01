'''
 Explanation of Refactoring: This refactoring demonstrates SOLID principles.
    The Single Responsibility Principle (SRP) is applied by having Book and Movie classes manage their own data and behavior, while MediaLibrary is responsible for the collection management. 
    The Open/Closed Principle (OCP) is evident as new media types can be integrated by adding new classes inheriting from Media, without modifying MediaLibrary. The Liskov Substitution Principle (LSP) ensures that Book and Movie can be used interchangeably as they are substitutable for their parent class, Media.
    The Interface Segregation Principle (ISP) is addressed by the Media abstract class, which serves as a contract for different media types, allowing for the creation of specific interfaces for varied media categories. Lastly, the Dependency Inversion Principle (DIP) is observed where both the MediaLibrary and individual media types like Book and Movie depend on the Media abstraction, ensuring a decoupling of high-level data handling from low-level data types.
''' 

from abc import ABC, abstractmethod

class Media(ABC):
    @abstractmethod
    def add_to_library(self, library):
        pass

class Book(Media):
    def add_to_library(self, library):
        library.add_book(self)

class Movie(Media):
    def add_to_library(self, library):
        library.add_movie(self)

class MediaLibrary:
    def __init__(self):
        self.media_list = []

    def add_media(self, media: Media):
        media.add_to_library(self)

    def add_book(self, book: Book):
        # adding a book to library
        self.media_list.append(book)

    def add_movie(self, movie: Movie):
        # adding a movie to library
        self.media_list.append(movie)
