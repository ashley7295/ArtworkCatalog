from catalog import Catalog, Artist, Artwork




def message(msg):
    print(msg)


def display_all_art(artwork):
    if artwork:
        for art in artwork:
            print('\n', art, '\n')
    else:
        print('No artwork currently in catalog')

def get_new_artwork():
    name_of_artpiece = input('Enter the name of the Artpiece: ')
    price = int(input('Enter the price of the Artpiece: '))

    return Artwork(name_of_artpiece, price)

def get_new_artist():
    name_of_artist = input('Enter the Artists Name: ')
    email = input('Enter the email for the artist: ')

    return Artist(name_of_artist, email)

