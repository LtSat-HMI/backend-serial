
# coding=utf-8

import sqlite3
import os


class ConnectBancoReal:
    def __init__(self):
        self.cursor = self.IniciaBD()
        # self.CriaTabela(self.cursor)

    def IniciaBD(self):
        try:
            self.conn = sqlite3.connect('BD/hotel.db')
        except print('error'):
            print('erro ao conectar banco')
        return self.conn.cursor()

    def EncerraBD(self):
        self.conn.close()

    def SaveTelemetria(self, lista):
        self.cursor.executemany("""
            INSERT INTO Telemetria (Count, Altitude, Temperatura, Tensao, GpsLatitude, GpsLongitude, GpsAltura, GiroscopioR, GiroscopioP, GiroscopioY, AcelerometroR, AcelerometroP, AcelerometroY, MagnetometroP, MagnetometroR, MagnetometroY)
            VALUES (?,?,?,?,?,?,?,?)
            """, [lista])
        self.conn.commit()
        print('Dados inseridos com sucesso.')
        self.EncerraBD()


# # criando a tabela (schema)
# cursor.execute("""
# CREATE TABLE clientes (
#         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#         Nome TEXT NOT NULL,
#         Telefone TEXT,
#         cpf     VARCHAR(14) NOT NULL,
#         Tempo_hospedagem INTEGER NOT NULL,
#         Numero_quarto INTEGER,
#         Tipo_quarto INTEGER,
#         Data_entrada TEXT NOT NULL,
#         Pagamento TEXT NOT NULL
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

    # def CriaTabela(self, cursor):
    #     cursor.execute("""
    #         CREATE TABLE UsersADM (
    #             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    #             user text NOT NULL,
    #             hash_senha text NOT NULL
    #         );
    #         """)
    #     print('Tabela criada com sucesso.')

    # def BuscaHash(self):
    #     self.cursor.execute('''select hash_senha
    #                     from UsersADM;''')
    #     rec= []
    #     for linha in self.cursor.fetchall():
    #         rec.append(linha)
    #         # retorna uma tupla
    #     return rec
    #     self.EncerraBD()
# if __name__ == '__main__':
#     Banco()
