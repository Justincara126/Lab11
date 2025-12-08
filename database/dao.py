from database.DB_connect import DBConnect
from model.rifugio import Rifugio

class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    # TODO
    def __init__(self):
        pass
    def search_all_rifugi(self):
        conn=DBConnect()
        db=conn.get_connection()
        cursor=db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM rifugio")
        result=[]
        for row in cursor:
            rifugio=Rifugio(row['id_rifugio',row['nome'],row['localita',row['altitude'],
            row['capienza'],row['aperto']]])
            result.append(rifugio)
            print(rifugio)
        return result





