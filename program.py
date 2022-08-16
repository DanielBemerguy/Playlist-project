from util import save, load
from models import Music, Podcast
from os import remove


def create_playlist():
    # well done!
    playlist_name = input(f'What is your playlist name?').title()
    song = input(f'Insert the song name.')
    author = input(f'Insert the author name.')
    rhythm = input(f'Insert the rhythm')
    templist = [Music(song, author, rhythm)]
    save(templist, playlist_name)


def read_playlist():
    existent_playlist = input(f"Which playlist do you want to read?").title()
    while True:
        try:
            # better to  return the playlist  from the function  and then you can print, add, etc.
            templist = load(existent_playlist)
            for file in templist:
                print(file)
            break
        except:
            print('Playlist does not exist!\nTry again')
            break


def add_music():
    existent_playlist = input(f'What is the list name that you want to add a music?')
    while True:
        try:
            # good!
            templist = load(existent_playlist)
            song = input(f'Insert the song name.')
            author = input(f'Insert the author name.')
            rhythm = input(f'Insert the rhythm')
            templist.append(Music(song, author, rhythm))
            save(templist, existent_playlist)
            break
        except:
            print('Playlist does not exist!\nTry again')
            break


def add_podcast():
    existent_playlist = input(f"Which playlist do you want to add a podcast?").title()
    while True:
        try:
            # good!
            templist = load(existent_playlist)
            author = input(f'Insert the podcast name.')
            episode = input(f'Insert the podcast episode.')
            subject = input(f'Insert the subject')
            templist.append(Podcast(author, episode, subject))
            save(templist, existent_playlist)
            break
        except:
            print('Playlist does not exist!\nTry again')
            break

def search_on_playlist(existent_playlist):
    found_items = []
    try:
        index = 0
        templist = load(existent_playlist)
        item = input('What is the name of the music/author/rhythm do you want to search?').title()
        for file in templist:
            index += 1
            if file.search(item):
                found_items.append(file)
                found_items.append(f'Number: {index}')
                continue
        for file in found_items:
            print(file)
        if found_items:
            return 1
        if not found_items:
            print('Item does not exist!\n Try again')
    except:
        print('Playlist does not exist!\nTry again')



def delete_item(existent_playlist):
    if search_on_playlist(existent_playlist) == 1:
        command = input(f'Do you want to delete an item? choose y/n').lower()
        if command == 'y':
            my_index = int(input(f'Which number from the playlist do yo want to delete?'))
            templist = load(existent_playlist)
            del templist[my_index - 1]
            save(templist, existent_playlist)
            print(f'Number {my_index} is deleted')
        elif command != 'n':
            print('Invalid choice')


def delete_playlist():
    existent_playlist = input(f"Which playlist do you want to delete?").title()
    command = input(f'Do you really want to delete {existent_playlist}? s/n').lower()
    if command == "s":
        remove(existent_playlist)


def copy_playlist():
    while True:
        try:
            new_playlist = []
            playlist_1 = input(f'What is the first playlist do you want to add').title()
            playlist_2 = input(f'What is the second playlist do you want to add').title()
            name = input(f'What is the name of the new playlist').title()
            # what happens if one playlist does not exist - i cannot copy?
            # why not?
            templist1 = load(playlist_1)
            for file in templist1:
                new_playlist.append(file)
            templist2 = load(playlist_2)
            for file in templist2:
                new_playlist.append(file)
            save(new_playlist, name)
            for file in new_playlist:
                print(file)
            # this loop never ends. also i can add the same list twice
            # which may be ok. but maybe check that the song is not double
            # what if 2 different playlists have the same song? is it supposed to be added twice?
        except:
            print('One of the Playlists is not existent.')
            break
