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
