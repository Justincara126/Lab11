from database.DB_connect import DBConnect
from model.rifugio import Rifugio
from model.connessione import Connessione


class DAO:

    def __init__(self):
        pass
    def search_all_rifugi(self):
        conn=DBConnect()
        db=conn.get_connection()
        cursor=db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM rifugio")
        DB=DBConnect.get_connection()
        cursor=DB.cursor(dictionary=True)
        cursor.execute('''SELECT * FROM rifugio''')
        result=[]
        for row in cursor:
            rifugio=Rifugio(row['id'],row['nome'],row['localita'],row['altitudine'],row['aperto'])
            result.append(rifugio)
        cursor.close()
        DB.close()

        return result










    def get_all_connessioni_anno(self,anno):
        DB=DBConnect.get_connection()
        cursor=DB.cursor(dictionary=True)
        query='SELECT * FROM connessione as r WHERE r.anno<=%s'
        cursor.execute(query,(anno,))
        result=[]
        for row in cursor:


            id_rifugio1=row['id_rifugio1']
            id_rifugio2=row['id_rifugio2']
            x=Connessione(row['id'],id_rifugio1,id_rifugio2,row['anno'])
            result.append(x)
        cursor.close()
        DB.close()
        return result
