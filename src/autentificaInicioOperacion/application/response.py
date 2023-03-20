import xml.etree.ElementTree as ET
import requests 

class BotResponse:
    def respCodInicioOperacion(self, dataconn):
        try:
            CodEntidad= str(dataconn["CodEntidad"])
            CodIV= str(dataconn["CodIV"])
            CodLocal = str(dataconn["CodLocal"])
            responseAuOpe = self.AutentificaInicioOperacion(CodEntidad, CodIV, CodLocal)
            respdata = self.obtenerDataResponse(responseAuOpe)
            return respdata
        except Exception as err:
            print(err)

    def AutentificaInicioOperacion(self, cod_entidad, cod_iv, cod_local):
        # Construye la solicitud
        headers = {'Content-Type': 'text/xml;charset=UTF-8', 'SOAPAction': 'http://tempuri.org/ICITV_TM_Servicios/AutentificaInicioOperacion'}
        body = f'''<?xml version="1.0" encoding="utf-8"?>
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/" xmlns:mtc="http://schemas.datacontract.org/2004/07/MTC.ServiciosCITV.Dominio.Entidades">
        <soapenv:Header/>
        <soapenv:Body>
            <tem:AutentificaInicioOperacion>
                <!--Optional:-->
                <tem:entLocalLogin>
                    <!--Optional:-->
                    <mtc:CodEntidad>{cod_entidad}</mtc:CodEntidad>
                    <!--Optional:-->
                    <mtc:CodIV>{cod_iv}</mtc:CodIV>
                    <!--Optional:-->
                    <mtc:CodLocal>{cod_local}</mtc:CodLocal>
                </tem:entLocalLogin>
            </tem:AutentificaInicioOperacion>
        </soapenv:Body>
        </soapenv:Envelope>'''

        # Realiza la solicitud
        response = requests.post('https://wscitv.mtc.gob.pe/WSInterOperabilidadCITV.svc', headers=headers, data=body)
        return response
    
    def obtenerDataResponse(self, response):
        root = ET.fromstring(response.content)
        # encuentra el nodo <a:Codigo> y extrae su texto
        codigo = root.find('.//{http://schemas.datacontract.org/2004/07/MTC.ServiciosCITV.Dominio.Entidades}Codigo').text

        # encuentra el nodo <a:Mensaje> y extrae su texto
        mensaje = root.find('.//{http://schemas.datacontract.org/2004/07/MTC.ServiciosCITV.Dominio.Entidades}Mensaje').text
        respdata = {"codigoInOperacion" : codigo, "mensaje": mensaje}
        return respdata
    
