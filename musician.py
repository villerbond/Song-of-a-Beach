from array import *

# В классе Песня хранятся её название и текст, также для разработки добавлены функции вывода на экран

class Song():
    name = ""
    text = ""

    def __init__(self, name_ = "", text_ = ""):
        self.name = name_
        self.text = text_

    def print(self):
        print(self.name, end="")

    def printName(self):
        print(self.name, end="")

# В классе Исполнитель хранятся его название, количество Песен и массив Песен,
# также для разработки добавлены функции вывода на экран,
# помимо этого, добавлены функции добавления Песни и сортировки массива Песен

class Musician():
    name = ""
    count_of_songs = 0
    songs = []

    def __init__(self, name_ = ""):
        self.name = name_
        self. count_of_songs = 0
        self.songs = []

    def addSong(self, song_):
        self.count_of_songs += 1
        self.songs.append(song_)

    def print(self):
        print(self.name + ":", end = " ")
        for i in range(self.count_of_songs):
            self.songs[i].print()
            print(" ", end="")
            if i != (self.count_of_songs - 1):
                print(", ", end="")

    def sort(self):
        self.songs.sort(key=lambda song: song.name)

# В классе База Исполнителей хранятся количество Исполнителей и массив Исполнителей,
# также для разработки добавлены функции вывода на экран,
# помимо этого, добавлены функции добавления Исполнителя и сортировки массива Исполнителей

class Base_of_Musicians():
    count_of_musicians = 0
    musicians = []

    def __init__(self, count_ = 0):
        self.count_of_musicians = count_
        self.musicians = []

    def addMusician(self, musician_):
        self.count_of_musicians += 1
        self.musicians.append(musician_)

    def print(self):
        for i in range(self.count_of_musicians):
            self.musicians[i].print()

    def sort(self):
        self.musicians.sort(key=lambda musician: musician.name)