artists = input().split(',')
tasks = input().split(',')

for artist in tasks:
    name, delta = artist.split()
    artist_index: int = artists.index(name)
    # artists.insert(artist_index - int(delta), artists[artist_index])
    # del artists[artist_index]
    artists.insert(artist_index - int(delta), artists.pop(artist_index))
print(artists)
