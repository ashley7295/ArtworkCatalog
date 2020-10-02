from catalog import Artist, Artwork, Catalog
import UI


test = 'test message'

#UI.display_all_art()


UI.message(test)
new_artist = UI.get_new_artist()

new_artwork = UI.get_new_artwork()

artwork = []
artwork.append(new_artwork)

UI.display_all_art(artwork)
