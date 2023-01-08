
# coding=utf-8

import sqlite3
import os

class BancoReal:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('src/database/db_real.db')
            print(self.conn)
        except:
            print('erro ao conectar banco')
        self.CriaTabela(self.conn.cursor)
    
    def IniciaBD(self):
        try:
            self.conn = sqlite3.connect('src/database/db_real.db')
        except:
            print('erro ao conectar banco')
        return self.conn.cursor()
    
    def EncerraBD(self):
        self.conn.close()



# # criando a tabela (schema)
# self.cursor.execute("""
# CREATE TABLE Telemetria (
#         count INTEGER NOT NULL PRIMARY KEY,
#         Altitude REAL,
#         Temperatura REAL,
#         Tensao REAL,
#         GpsLatitude REAL,
#         GpsLongitude REAL,
#         GpsAltura REAL,
#         GiroscopioR REAL,
#         GiroscopioP REAL,
#         GiroscopioY REAL,
#         AcelerometroR REAL,
#         AcelerometroP REAL,
#         AcelerometroY REAL,
#         MagnetometroP REAL,
#         MagnetometroR REAL,
#         MagnetometroY REAL
# );
# """)

# cursor.execute("""
#             CREATE TABLE UsersADM (
#                 id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#                 user text NOT NULL,
#                 hash_senha text NOT NULL
#             );
#             """)
#         print('Tabela criada com sucesso.')




    # criando a tabela (schema)
    
    def CriaTabela(self, cursor):
        # criando a tabela (schema)
        cursor.execute("""
            CREATE TABLE telemetria (
                count INTEGER NOT NULL PRIMARY KEY,
                Altitude REAL,
                Temperatura REAL,
                Tensao REAL,
                GpsLatitude REAL,
                GpsLongitude REAL,
                GpsAltura REAL,
                GiroscopioR REAL,
                GiroscopioP REAL,
                GiroscopioY REAL,
                AcelerometroR REAL,
                AcelerometroP REAL,
                AcelerometroY REAL,
                MagnetometroP REAL,
                MagnetometroR REAL,
                MagnetometroY REAL
                );
            """)
        print('Tabela criada com sucesso.')

if __name__ == '__main__':
    BancoReal()