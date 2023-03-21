from logging.handlers import RotatingFileHandler 
from logging import handlers
from src.enviarMTC.infrastructure.controller import BotControllerEnviar
from src.autentificaInicioOperacion.infrastructure.controller import BotControllerInicio
from src.registraPoliza.infrastructure.controller import RegistraPolizaController

def main():
    try:
        #while True:
            _botCL = BotControllerInicio()
            _regCL = RegistraPolizaController()
            dataCodigo = _botCL.codAutentificacion()
            datasql = _regCL.registrarPoliza(dataCodigo)
            print(datasql)
            return datasql
    except Exception as err:
        pass

main()