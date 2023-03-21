from .sql import consultasSQL
from ..application.response import RegistraPolizaResponse
class RegistraPolizaController:
    def registrarPoliza(self, dataCodigo):
        sql = consultasSQL()
        response = RegistraPolizaResponse()
        datasqlRegistro = sql.listRegistraPoliza()
        dataListResp = response.enviarMTCPoliza(datasqlRegistro, dataCodigo)
        dataActTable = sql.actualizarTableRegistroPoliza(dataListResp)
        print(dataActTable)
        return dataListResp
