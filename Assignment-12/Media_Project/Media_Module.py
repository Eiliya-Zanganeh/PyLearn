from Actor_Module import Actor


class Media:
    def __init__(self, movie_type, name, director, imdb_score, duration, casts):
        self.movie_type = movie_type
        self.name = name
        self.director = director
        self.imdb_score = imdb_score
        self.duration = duration
        casts = casts.split(",")
        all_actor = []
        for cast in casts:
            cast = cast.strip()
            name, family = cast.split(" ")
            actor = Actor(name, family)
            all_actor.append(actor)
        self.casts = all_actor

    def download(self):
        ...

    def show_info(self):
        return self.__str__()

    def __str__(self):
        return f"type: {self.movie_type}\t|name: {self.name}\t|director: {self.director}\t|IMDB score: {self.imdb_score}\t|duration: {self.duration}\t|casts: {[cast.show_full_name() for cast in self.casts]}"
