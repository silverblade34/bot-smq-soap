from src.autentificaInicioOperacion.application.response import BotResponse
from .sql import consultasMysql 

class BotControllerInicio:
    def codAutentificacion(self):
        response = BotResponse()
        conec = consultasMysql()
        dataconn = conec.listAutentificaInicioOperacion()
        data = response.respCodInicioOperacion(dataconn) 
        return data