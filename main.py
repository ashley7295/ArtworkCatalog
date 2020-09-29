import sqlite3

db = 'catalog.sqlite'

class Artist:

    def __init__(self, artist, email, artPiece, price, available = True):
        self.artist = artist
        self.email = email
        self.artPiece = artPiece
        self.price = price
        self.availabe = available

        self.catalog = Catalog()

class Catalog:

    def __init__(self):
        
    

   