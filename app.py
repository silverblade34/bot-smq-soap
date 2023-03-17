from logging.handlers import RotatingFileHandler 
from logging import handlers
from src.enviarMTC.infrastructure.controller import BotControllerEnviar
from src.autentificaInicioOperacion.infrastructure.controller import BotControllerInicio

def main():
    try:
        #while True:
            _botCL = BotControllerInicio()
            data = _botCL.codAutentificacion()
            print(data)
            return data
    except Exception as err:
        pass

main()