from program import create_playlist, read_playlist, add_music, add_podcast, search_on_playlist, delete_item, \
    delete_playlist, copy_playlist

while True:

    start = input(f"Tap 1 to create a playlist \n"
                  f"Tap 2 to read a playlist \n"
                  f"Tap 3 to add a music\n"
                  f"Tap 4 to add a podcast\n"
                  f"Tap 5 to search a music in a playlist\n"
                  f"Tap 6 to delete a playlist item\n"
                  f"Tap 7  to delete a playlist\n"
                  f"Tap 8 to create a new playlist from existent playlists\n"
                  f"Tap 0 to exit")

    if start == "1":
        create_playlist()

    if start == "2":
        read_playlist()

    if start == "3":
        add_music()

    if start == "4":
        add_podcast()

    if start == "5":
        existent_playlist = input(f'Which playlist do you want to search?').title()
        search_on_playlist(existent_playlist)

    if start == "6":
        existent_playlist = input(f'From which playlist do you want to delete the item?').title()
        delete_item(existent_playlist)

    if start == "7":
        delete_playlist()

    if start == "8":
        copy_playlist()

    if start == "0":
        print('Good Bye!')
        break
