import sqlite3

db = 'catalog.sqlite'

class Art:

    def __init__(self, artist, email, artPiece, price, available = True, id=None):
        self.artist = artist
        self.email = email
        self.artPiece = artPiece
        self.price = price
        self.availabe = available
        self.id = id

        self.catalog = Catalog()

    def save(self):
        if self.id:
            self.catalog._update_art(self)
        else:
            self.catalog._add_art(self)

    def delete(self):
        self.catalog._delete_art(self)
        print('Art has been removed from the catalog')



class Catalog:

    instance = None

    def __init__(self):
        with sqlite3.connect(db) as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS catalog (artist TEXT, email TEXT, artpiece TEXT, price int, available BOOLEAN, UNIQUE(artpiece COLLATE NOCASE)')
        conn.close()
    
    def _add_art(self, art):
        
        add_sql = 'INSERT INTO catalog (artist, email, artpiece, price, available) VALUES (?,?,?,?,?)'
        
        try:
            with sqlite3.connect(db) as conn:
                result = conn.execute(add_sql, (art.artist, art.email, art.artpiece, art.price, art.available))
                new_id= result.lastrowid
                art.id = new_id
        except:
            print("This art piece has already been entered into the catalog")
        finally:
            conn.close()

    def _update_art(self, art):
        
        if not art.id:
            print("Art does not have an ID, cannot update.")
        
        update_sql = 'UPDATE catalog SET artist = ?, email = ?, artpiece = ?, price = ?, available = ?, WHERE rowid = ?'

        with sqlite3.connect(db) as conn:
            updated = conn.execute(update_sql, (art.artist, art.email, art.artpiece, art.price, art.available ))
            items_modified = updated.rowcount
        conn.close()

        if items_modified == 0:
            print('Art not Found')

    def _delete_art(self, art):
        
        if not art.id:
            print('Art not found or does not have ID')

        delete_sql = 'DELETE FROM catalog WHERE rowid = ?'

        with sqlite3.connect(db) as conn:
            deleted = conn.execute(delete_sql, (art.id, ))
            items_deleted = deleted.rowcount
        conn.close()

        if items_deleted == 0:
            print('Art not found in catalog')

    def search_artist(self, term):

        search_sql = 'SELECT rowid, * FROM catalog WHERE UPPER(artist) like UPPER(?)'

        search = f'%{term}%'

        conn = sqlite3.connect(db)
        conn.row_factory = sqlite3.Row
        rows = conn.execute(search_sql, (search, ))
        art_list = []

        for r in rows:

            art = Art(r['artist'], r['email'], r['artpiece'], r['price'], r['available'], r['rowid'])
            art_list.append(art)
        
        conn.close()

        return art_list

    def  search_available_art(self, artist):

        search_avail_artist_sql = ' SELECT rowid, * FROM catalog WHERE UPPER(artist) like UPPER(?) AND available = TRUE'

        conn = sqlite3.connect(db)
        conn.row_factory = sqlite3.Row
        rows = conn.execute(search_avail_artist_sql, (artist, ))

        artist_list = []

        for r in rows:
            art = Art(r['artist'], r['email'], r['artpiece'], r['price'], r['available'], r['rowid'])
            artist.append(art)
        
        conn.close()

        return artist_list





        


   