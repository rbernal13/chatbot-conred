import json
import sys

import gspread
import pandas as pd
from google.oauth2.service_account import Credentials
from gspread_dataframe import set_with_dataframe
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def guardar_datos(nombre, email, pregunta1, pregunta2, pregunta3, pregunta4) -> None:

  """ Funcion que conecta con google spreadsheet y sube los datos ingresados en el bot usando contextos.

  :nombre del usuario:
  
  :email del usuario:
  
  :pregunta1 de la encuesta:
  
  :pregunta2 de la encuesta:
  
  :pregunta3 de la encuesta:
  
  :pregunta4 de la encuesta:
  """

  try:

    # Conexion con google spreadsheet
    scopes = ['https://www.googleapis.com/auth/spreadsheets',
              'https://www.googleapis.com/auth/drive']
    credentials = Credentials.from_service_account_file('spredsheet-api-key.json', scopes=scopes)
    gc = gspread.authorize(credentials)
    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)

    # Uso del KEY para acceder
    gs = gc.open_by_key('1J1JWyTkEftd-3yUCg30vvhZYH93yJG0mLVhKBlkBrwE')
    # Seleccionar el nombre del spreadsheet
    worksheet1 = gs.worksheet('encuesta_respuestas')

    # Creacion de DataFrame
    df = pd.DataFrame({
      'Nombre':[nombre],
      'Email':[email],
      'Pregunta1':[pregunta1], 
      'Pregunta2':[pregunta2], 
      'Pregunta3':[pregunta3], 
      'Pregunta4':[pregunta4]})

    # Enviar el dato a el excel usando append
    df_values = df.values.tolist()
    gs.values_append('encuesta_respuestas', {'valueInputOption': 'RAW'}, {'values': df_values})
      
  except Exception as e:
    print("Oops!", e.__class__, "occurred.")
    print(e.message)