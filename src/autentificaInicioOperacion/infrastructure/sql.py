from src.sql.connect import ConnectionMysql   
import datetime

class consultasMysql:
    def __init__(self):
        self.connect = ConnectionMysql()

    def __del__(self):
        self.connect.conn.close()

    def listAutentificaInicioOperacion(self):
        try:
            cursor = self.connect.cursor
            cursor.execute(f"SELECT TOP 1 * FROM tb_autentificaInicioOperacion ORDER BY id DESC") 
            dt = cursor.fetchall() 
            dataresult = {}
            dataresult["id"] = dt[0][0]
            dataresult["fecha"] = dt[0][1]
            dataresult["CodEntidad"] = dt[0][2]
            dataresult["CodLocal"] = dt[0][3]
            dataresult["CodIV"] = dt[0][4]
            return dataresult
        except Exception as err :
            return err
        
    def actualizarCodigoInicioOperacion(self, datamtc, dataconn):
        cursor = self.connect.cursor
        id = dataconn["id"]
        codigo = datamtc["codigoInOperacion"]
        mensaje = datamtc["mensaje"]
        cursor.execute("UPDATE tb_autentificaInicioOperacion SET R_CODIGO = ?, R_MENSAJE = ? WHERE id = ?", (codigo, mensaje, id))
        if cursor.rowcount == 1:
            self.connect.conn.commit()
            return "La actualización del codigo de Inicio de Operacion se realizó correctamente"
        else:
            self.connect.conn.rollback()
            return "No se encontró ninguna fila para actualizar el codigo de Inicio de Operacion"


    