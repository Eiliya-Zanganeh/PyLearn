import Media_Module


class Film(Media_Module.Media):
    def __init__(self, movie_type, name, director, imdb_score, duration, casts, episode):
        super().__init__(movie_type, name, director, imdb_score, duration, casts)
        self.episode = episode

    def __str__(self):
        return f"{super().__str__()}\t|Episode: {self.episode}"
