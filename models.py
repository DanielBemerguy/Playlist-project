

class PlayItem:
    def __init__(self, author):
        self._author = author.title()
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def give_like(self):
        self._likes += 1

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author.title()

    def __str__(self):
        return f'{self.author}: Likes:{self.likes}'


class Music(PlayItem):
    def __init__(self, song, author, rhythm):
        super().__init__(author)
        self._song = song.title()
        self._rhythm = rhythm.title()

    def __str__(self):
        return f'{self.author} - {self._song} - {self._rhythm}: Likes:{self.likes}'

    def search(self, item):
        return item == self._song or item == self._rhythm or item == self.author


class Podcast(PlayItem):
    def __init__(self, episode, author, subject):
        super().__init__(author)
        self._episode = episode.title()
        self.subject = subject.title()
        self._likes = 0

    def __str__(self):
        return f'{self.author} - {self._episode} - {self.subject}: Likes:{self.likes}'

    def search(self, item):
        return item == self._episode or item == self.subject or item == self.author

