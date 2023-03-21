from src.sql.connect import ConnectionMysql   
import datetime

class consultasSQL:
    def __init__(self):
        self.connect = ConnectionMysql()

    def __del__(self):
        self.connect.conn.close()

    def listRegistraPoliza(self):
        try:
            cursor = self.connect.cursor
            cursor.execute(f"SELECT * FROM tb_registraPoliza where FLG_PROCESADO = 0 and FLG_ACTIVO = 0") 
            dt = cursor.fetchall()
            return dt
        except Exception as err :
            return err
        
    def actualizarTableRegistroPoliza(self, dataListResp):
        cursor = self.connect.cursor
        statusInserted = {}
        correct =[]
        error = []
        for resp in dataListResp:
            id = resp["idtable"]
            mensaje = resp["mensaje"]
            RetVal = resp["RetVal"]
            cursor.execute("UPDATE tb_registraPoliza SET R_MENSAJE = ?, R_RETVAL = ?, FLG_PROCESADO = 1  WHERE id = ?", (mensaje, RetVal, id))
            if cursor.rowcount == 1:
                self.connect.conn.commit()
                correct.append(id)
            else:
                self.connect.conn.rollback()
                error.append(id)
        statusInserted["correct"] = correct
        statusInserted["error"] = error
        return statusInserted