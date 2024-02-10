from Media_Module import Media


class Series(Media):
    def __init__(self, movie_type, name, director, imdb_score, duration, casts, season, episode):
        super().__init__(movie_type, name, director, imdb_score, duration, casts)
        self.season = season
        self.episode = episode

    def __str__(self) -> str:
        return f"{super().__str__()}\t|Season: {self.season}\t|Episodes: {self.episode}"
