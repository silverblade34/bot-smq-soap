import pyodbc

class ConnectionMysql:

    def __init__(self):
        print("-----------------1")
        # Datos para la conexión
        server = '192.168.1.222'
        database = 'SistCITVRD'
        username = 'sa'
        password = '0313334'

        # Cadena de conexión
        conn_str = (
            f"DRIVER={{SQL Server}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password};"
        )
        print("--------------1.2")
        self.conn = pyodbc.connect(conn_str)
        #self.conn = mysql.connector.connect( host='192.168.1.222', user= 'sa', passwd='0313334', db='SistCITVRD')
        # self.conn = mysql.connector.connect( host='104.248.60.94', user= 'root', passwd='Sys4Log$$sa', db='db_test' )
        print("------------------1.3")
        self.cursor = self.conn.cursor()

