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
#print(data[0])
#print(len(data))

def WriteToMySQLTable(sql_data, tableName):
    try:
        connection = mysql.connector.connect(
            user=mc.user,
            password=mc.password,
            host=mc.host,
            #port=mc.port,
            #database=mc.database
        )
        # sql_drop = "DROP TABLE IF EXISTS {}".format(tableName)
        # sql_create_table = """CREATE TABLE {}(
        #     Column1 INT(11),
        #     Column2 VARCHAR(30),
        #     Column3 DATETIME,
        #     PRIMARY KEY(Column1)
        #     )""".format(tableName)
        # sql_insert_statement = """INSERT INTO {}( Column1, Column2, Column3) VALUES(%s, %s, %s)""".format(tableName)

        # cursor = connection.cursor()
        # cursor.execute(sql_drop)
        # print('Table {} has been dropped'.format(tableName))
        # cursor.execute(sql_create_table)
        # print('Table {} has been created'.format(tableName))

        # for i in sql_data:
        #     cursor.execute(sql_insert_statement, i)
        
        # connection.commit()
        # print('Table {} successfully updated'.format(tableName))

    except mysql.connector.Error as error:
        connection.rollback()
        print('Error: {}'.format(error))

    # finally:
    #     cursor.execute('SELECT COUNT(*) FROM {}'.format(tableName))
    #     rowCount = cursor.fetchone()[0]
    #     print(tableName, 'row count:', rowCount)
    #     if connection.is_connected():
    #         cursor.close()
    #         connection.close()
    #         print('MySQL connection is closed')

WriteToMySQLTable(data, 'Prediccion_de_apuestas')