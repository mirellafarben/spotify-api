def get_songs():
    songs_list = []

    text_file = open('tessa.txt', 'r')
    for line in text_file:

        songs_list.append(line.replace(" ", "%20").strip("\n"))

    return songs_list


get_songs()
