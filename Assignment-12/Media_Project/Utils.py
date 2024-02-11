from Film_Module import Film
from Series_Module import Series
from Documentary_Module import Documentary
from Clip_Module import Clip
from datetime import time
from pytube import YouTube


def load_dataset():
    all_medias = []
    with open('/home/eiliya/Desktop/MrAemmi/PyLearn/Assignment-12/Media_Project/data.txt', 'r') as file:
        for line in file.readlines():
            properties = line.split("|")
            if properties[0] == "film":
                media = Film("film", properties[1], properties[2], properties[3], properties[4],
                             properties[5], properties[6])
                all_medias.append(media)
            elif properties[0] == "series":
                media = Series("series", properties[1], properties[2], properties[3], properties[4],
                               properties[5], properties[6], properties[7])
                all_medias.append(media)
            elif properties[0] == "documentary":
                media = Documentary("documentary", properties[1], properties[2], properties[3], properties[4],
                                    properties[5], properties[6])
                all_medias.append(media)
            elif properties[0] == "clip":
                media = Clip("clip", properties[1], properties[2], properties[3], properties[4],
                             properties[5], properties[6])
                all_medias.append(media)
    return all_medias


def add_media(all_media):
    media_type = int(input("Enter the 1: film, 2: series, 3: documentary, 4: clip "))
    name = input("Enter the name: ")
    director = input("Enter the director: ")
    imdb_score = input("Enter the imdb score: ")
    duration = input("Enter the duration: ")
    casts = input("Enter the casts: eiliya zanganeh, matin gorbani,...")
    if media_type == 1:
        episode = int(input("Enter the episode number: "))
        new_media = Film("film", name, director, imdb_score, duration, casts, episode)
        all_media.append(new_media)
    elif media_type == 2:
        season = int(input("Enter the season number: "))
        episode = int(input("Enter the episode number: "))
        new_media = Series("series", name, director, imdb_score, duration, casts, season, episode)
        all_media.append(new_media)
    elif media_type == 3:
        title = input("Enter the title: ")
        new_media = Documentary("documentary", name, director, imdb_score, duration, casts, title)
        all_media.append(new_media)
    elif media_type == 4:
        title = input("Enter the title: ")
        new_media = Clip("clip", name, director, imdb_score, duration, casts, title)
        all_media.append(new_media)
    else:
        print("Invalid")
    return all_media


def edit_media(all_media):
    name = input("Enter the name of the media: ")
    for media in all_media:
        if media.name == name:
            name = input("Enter the new name: ")
            director = input("Enter the new director: ")
            imdb_score = input("Enter the new imdb score: ")
            duration = input("Enter the new duration: ")
            media.name = name
            media.director = director
            media.imdb_score = imdb_score
            media.duration = duration
            if media.movie_type == "film":
                episode = int(input("Enter the new episode number: "))
                media.episode = episode
            elif media.movie_type == "series":
                season = int(input("Enter the new season number: "))
                episode = int(input("Enter the new episode number: "))
                media.season = season
                media.episode = episode
            elif media.movie_type == "documentary":
                title = input("Enter the new title: ")
                media.title = title
            elif media.movie_type == "clip":
                title = input("Enter the new title: ")
                media.title = title
            break
    return all_media


def delete_media(all_media):
    name = input("Enter the name of the media: ")
    for media in all_media:
        if media.name == name:
            all_media.remove(media)
            break
    return all_media


def search_media(all_media):
    name = input("Enter the name of the media: ")
    for media in all_media:
        if media.name == name:
            print(media)


def search_media_by_time(all_media):
    user_time_1 = input("Enter the start time: ")
    user_time_2 = input("Enter the stop time: ")
    user_time_1 = user_time_1.split(":")
    user_time_2 = user_time_2.split(":")
    user_time_1 = time(int(user_time_1[0]), int(user_time_1[1]), int(user_time_1[2]))
    user_time_2 = time(int(user_time_2[0]), int(user_time_2[1]), int(user_time_2[2]))
    for media in all_media:
        media_time = media.duration.split(":")
        media_time = time(int(media_time[0]), int(media_time[1]), int(media_time[2]))
        if (user_time_1 < media_time) and (user_time_2 > media_time):
            print(media)


def show_all_media(all_media):
    for media in all_media:
        print(media)


def download_media():
    video_url = input("Enter the url: ")

    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()

    stream.download('downloads/')


def exit_user(all_media):
    with open('/home/eiliya/Desktop/MrAemmi/PyLearn/Assignment-12/Media_Project/data.txt', 'w') as file:
        for media in all_media:
            actors = [cast.show_full_name() for cast in media.casts]
            actors = ", ".join(actors)
            file.write(
                f"{media.movie_type}|{media.name}|{media.director}|{media.imdb_score}|{media.duration}|{actors}|")
            if media.movie_type == "film":
                file.write(f"{media.episode}")
            elif media.movie_type == "series":
                file.write(f"{media.season}|{media.episode}")
            elif media.movie_type == "documentary":
                file.write(f"{media.title}")
            elif media.movie_type == "clip":
                file.write(f"{media.title}")
