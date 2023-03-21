import requests
import xml.etree.ElementTree as ET

class RegistraPolizaResponse:
    def enviarMTCPoliza(self, dataSQLRegistro, dataCodigo):
        lisRespuestas = []
        for poliza in dataSQLRegistro:
            ID = poliza[0]
            ASEGURADORA = str(poliza[8])
            CIOD_CITV = dataCodigo["codigoInOperacion"]
            FECFINPOLIZA = str(poliza[7])
            FECINIPOLIZA = str(poliza[6])
            NUMPOLIZA = str(poliza[5])
            NUM_FICHA = str(poliza[2])
            PLACA = str(poliza[3])
            TPPOLIZA = str(poliza[4])
            dataresp = self.registroPoliza(ASEGURADORA, CIOD_CITV, FECFINPOLIZA, FECINIPOLIZA, NUMPOLIZA, NUM_FICHA, PLACA, TPPOLIZA)
            resp = self.parsearRespuesta(dataresp, ID)
            lisRespuestas.append(resp)
        return lisRespuestas

    def registroPoliza(self, ASEGURADORA, CIOD_CITV, FECFINPOLIZA, FECINIPOLIZA, NUMPOLIZA, NUM_FICHA, PLACA, TPPOLIZA):
        # Construye la solicitud
        headers = {'Content-Type': 'text/xml;charset=UTF-8',
                   'SOAPAction': 'http://tempuri.org/ICITV_TM_Servicios/registraPoliza'}
        
        body = f'''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/" xmlns:mtc="http://schemas.datacontract.org/2004/07/MTC.ServiciosCITV.Dominio.Entidades">
                <soapenv:Header/>
                <soapenv:Body>
                    <tem:registraPoliza>
                        <!--Optional:-->
                        <tem:entVehiculoPoliza>
                            <mtc:ASEGURADORA>{ASEGURADORA}</mtc:ASEGURADORA>
                            <mtc:CIOD_CITV>{CIOD_CITV}</mtc:CIOD_CITV>
                            <mtc:FECFINPOLIZA>{FECFINPOLIZA}</mtc:FECFINPOLIZA>
                            <mtc:FECINIPOLIZA>{FECINIPOLIZA}</mtc:FECINIPOLIZA>
                            <mtc:NUMPOLIZA>{NUMPOLIZA}</mtc:NUMPOLIZA>
                            <mtc:NUM_FICHA>{NUM_FICHA}</mtc:NUM_FICHA>
                            <mtc:PLACA>{PLACA}</mtc:PLACA>
                            <mtc:TPPOLIZA>{TPPOLIZA}</mtc:TPPOLIZA>
                        </tem:entVehiculoPoliza>
                    </tem:registraPoliza>
                </soapenv:Body>
                </soapenv:Envelope>'''
        # Realiza la solicitud
        response = requests.post(
            'https://wscitv.mtc.gob.pe/WSInterOperabilidadCITV.svc', headers=headers, data=body)
        return response
    
    def parsearRespuesta(self, response, ID):
        root = ET.fromstring(response.content)
        # encuentra el nodo <a:Mensaje> y extrae su texto
        mensaje = root.find('.//{http://schemas.datacontract.org/2004/07/MTC.ServiciosCITV.Dominio.Entidades}Mensaje').text
        RetVal = root.find('.//{http://schemas.datacontract.org/2004/07/MTC.ServiciosCITV.Dominio.Entidades}RetVal').text
        result = {"mensaje": mensaje, "RetVal": RetVal, "idtable": ID}
        return result
