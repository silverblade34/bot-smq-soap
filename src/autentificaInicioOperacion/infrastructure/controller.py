from src.autentificaInicioOperacion.application.response import BotResponse
from .sql import consultasMysql 

class BotControllerInicio:
    def codAutentificacion(self):
        response = BotResponse()
        conec = consultasMysql()
        dataconn = conec.listAutentificaInicioOperacion()
        datamtc = response.respCodInicioOperacion(dataconn)
        dataupdaterow = conec.actualizarCodigoInicioOperacion(datamtc, dataconn)
        print(dataupdaterow)
        return datamtc