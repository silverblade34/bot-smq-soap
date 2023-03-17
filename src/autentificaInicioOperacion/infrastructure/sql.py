from src.mysql.connect import ConnectionMysql 

class consultasMysql:
    def __init__(self):
        self.connect = ConnectionMysql()

    def listAutentificaInicioOperacion(self):
        try:
            cursor = self.connect.cursor
            print("--------------2")
            cursor.execute(f"SELECT * FROM tb_autentificaInicioOperacion") 
            # cursor.execute( "SELECT * FROM tb_alerts")  
            dt = cursor.fetchall() 
            self.connect.conn.close()
            
            return dt
        except Exception as err :
            return err