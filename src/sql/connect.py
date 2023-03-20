import pyodbc

class ConnectionMysql:

    def __init__(self):
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
        self.conn = pyodbc.connect(conn_str)
        self.cursor = self.conn.cursor()

