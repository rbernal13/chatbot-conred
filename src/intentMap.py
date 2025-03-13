from src.mensajes.asesor import asesor
from src.mensajes.encuesta.encuesta_despedida import encuesta_despedida
from src.mensajes.encuesta.encuesta_inicio import encuesta_satisfaccion
from src.mensajes.encuesta.encuesta_p1 import encuesta_pregunta1
from src.mensajes.encuesta.encuesta_p2 import encuesta_pregunta2
from src.mensajes.saludo import saludo


def intentMap(req):
    try:
        # Obtener la intencion actual de la conversacion
        intencion = req["queryResult"]["intent"]["displayName"] 
        print("=> Intencion solicitada: ", intencion)

        if (intencion == 'Saludo'):
            res = saludo(req)
            return res        
        if (intencion == 'Asesor'):
            res = asesor(req)
            return res
        if (intencion == 'EncuestaSatisfaccion'):
            res = encuesta_satisfaccion(req)
            return res
        if (intencion == 'EncuestaSatisfaccion - P1'):
            res = encuesta_pregunta1(req)
            return res
        if (intencion == 'EncuestaSatisfaccion - P2'):
            res = encuesta_pregunta2(req)
            return res
        if (intencion == 'EncuestaSatisfaccion - Despedida'):
            res = encuesta_despedida(req)
            return res
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print(e.message)
        