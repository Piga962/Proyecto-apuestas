import gspread
import MySQLCredentials as mc
import mysql.connector
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/cesar/Downloads/miproyectoapuestas-47a340346052.json', scope)

client = gspread.authorize(creds)

def GetSpreadsheetData(sheetName, worksheetIndex):
    sheet = client.open(sheetName).get_worksheet(worksheetIndex)
    return sheet.get_all_values()[1:]

data = GetSpreadsheetData('Prediccion_de_apuestas', 0)
print(data[0,0])
print(len(data))