"""summary"""


def make_album(
        artist_name, album_title,
        num_songs=None):
    """Return a dictionary of artist name and album title."""
    music_album = {'artist': artist_name, 'album': album_title}
    if num_songs:
        music_album['songs'] = num_songs
    return music_album


print(make_album('ethan', 'music', 18))
print(make_album('Beyonce', 'Dangerously in Love'))
print(make_album('michael jackson', 'thriller'))

# User Albums:
while True:
    print("\nPlease enter the artist's name and title of the album:")
    print("(enter 'q' at any time to quit)")

    a_name = input("Artist name: ")
    if a_name.lower() == 'q':
        break

    a_title = input("Album title: ")
    if a_title.lower() == 'q':
        break

    print(make_album(a_name, a_title))
