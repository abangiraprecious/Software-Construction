class MediaLibrary:
    def __init__(self):
        self.media_list = []

    def add_media(self, media):
        if isinstance(media, Book):
            self.add_book(media)
        elif isinstance(media, Movie):
            self.add_movie(media)
        # other media types if any

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
