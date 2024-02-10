from Media_Module import Media


class Documentary(Media):
    def __init__(self, movie_type, name, director, imdb_score, duration, casts, title):
        super().__init__(movie_type, name, director, imdb_score, duration, casts)
        self.title = title

    def __str__(self):
        return f"{super().__str__()}\t|Title: {self.title}"
