class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["happy birthday to you", "stop right there"])

bulls_on_parade = Song(["rally round family", "pockets of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
        