import sqlite3

db = 'catalog.sqlite'

class Artist:

    def __init__(self, name, email, id=None):
        self.name = name
        self.email = email
        self.id = id

        self.catalog = Catalog()

    def save(self):
        if self.id:
            self.catalog._update_artist(self)
        else:
            self.catalog._add_artist(self)

    def delete(self):
        self.catalog._delete_artist(self)
        print('Artist has been removed from the catalog')

class Artwork:

    def __init__(self, name, price, available = True, id = None):
        self.name = name
        self.price = price
        self.available = available
        self.id = id

        self.catalog = Catalog()

    def save(self):
        if self.id:
            self.catalog._update_artwork(self)
        else:
            self.catalog._add_artwork(self)

    def delete(self):
        self.catalog._delete_artwork(self)
        print('Artwork has been removed from the catalog')


class Catalog:

    instance = None

    def __init__(self):
        with sqlite3.connect(db) as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS artist (name TEXT, email TEXT')
            conn.execute('CREATE TABLE IF NOT EXISTS artwork (name TEXT, price INTEGER, available BOOLEAN, UNIQUE(name COLLATE NOCASE')
        conn.close()
    

    def _add_artwork(self, artwork):
        
        add_sql = 'INSERT INTO artwork (name, price, available) VALUES (?,?,?)'
        
        try:
            with sqlite3.connect(db) as conn:
                result = conn.execute(add_sql, (artwork.name, artwork.price, artwork.available))
                new_id= result.lastrowid
                art.id = new_id
        except:
            print("This art piece has already been entered into the catalog")
        finally:
            conn.close()
    

    def _add_artist(self, artwork):
        
        add_sql = 'INSERT INTO artist (name, email) VALUES (?,?)'
        
        try:
            with sqlite3.connect(db) as conn:
                result = conn.execute(add_sql, (artist.name, artist.email))
                new_id= result.lastrowid
                art.id = new_id
        except:
            print("This artist has already been entered into the catalog")
        finally:
            conn.close()


    def _update_artist(self, artist):
        
        if not artist.id:
            print("Artist does not have an ID, cannot update.")
        
        update_sql = 'UPDATE artist SET name = ?, email = ?,  WHERE rowid = ?'

        with sqlite3.connect(db) as conn:
            updated = conn.execute(update_sql, (artist.name, artist.email ))
            items_modified = updated.rowcount
        conn.close()

        if items_modified == 0:
            print('Artist not Found')


    def _update_artwork(self, artwork):
        
        if not artwork.id:
            print("Art does not have an ID, cannot update.")
        
        update_sql = 'UPDATE artwork SET name = ?, price = ?, available = ?, WHERE rowid = ?'

        with sqlite3.connect(db) as conn:
            updated = conn.execute(update_sql, (artwork.name, artwork.price, artwork.available ))
            items_modified = updated.rowcount
        conn.close()

        if items_modified == 0:
            print('Artwork not Found')


    def _delete_artist(self, artist):
        
        if not artist.id:
            print('Artist not found or does not have ID')

        delete_sql = 'DELETE FROM artist WHERE rowid = ?'

        with sqlite3.connect(db) as conn:
            deleted = conn.execute(delete_sql, (artist.id, ))
            items_deleted = deleted.rowcount
        conn.close()

        if items_deleted == 0:
            print('Artist not found in catalog')

    
    def _delete_artwork(self, artwork):
            
        if not artwork.id:
            print('Artwork not found or does not have ID')

        delete_sql = 'DELETE FROM artwork WHERE rowid = ?'

        with sqlite3.connect(db) as conn:
            deleted = conn.execute(delete_sql, (artwork.id, ))
            items_deleted = deleted.rowcount
        conn.close()

        if items_deleted == 0:
            print('Art not found in catalog')

    def search_artist(self, term):

        search_sql = 'SELECT rowid, * FROM artist WHERE UPPER(name) like UPPER(?)'

        search = f'%{term}%'

        conn = sqlite3.connect(db)
        conn.row_factory = sqlite3.Row
        rows = conn.execute(search_sql, (search, ))
        art_list = []

        for r in rows:

            artist = Artist(r['name'], r['email'], r['rowid'])
            art_list.append(artist)
        
        conn.close()

        return art_list


    def  search_available_art(self, artist):

        search_avail_artist_sql = ' SELECT rowid, * FROM catalog WHERE UPPER(artist) like UPPER(?) AND available = TRUE'

        conn = sqlite3.connect(db)
        conn.row_factory = sqlite3.Row
        rows = conn.execute(search_avail_artist_sql, (artist, ))

        artist_list = []

        for r in rows:
            art = Art(r['artist'], r['email'], r['rowid'])
            artist.append(art)
        
        conn.close()

        return artist_list





        


   