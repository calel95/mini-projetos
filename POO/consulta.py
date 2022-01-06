from datetime import date, time, datetime, timedelta

from paciente import Paciente
from profissional import Profissional
class Consulta():

    consultas = []
    # def __init__(self, data_consulta):
    #     self.data_consulta = data_consulta

    def __init__(self,paciente, profissional, dat_con):
        self.profissional = profissional
        self.dat_con = dat_con
        self.paciente = paciente
        #self.papro = paciente + profissional
    #
        pegaConsulta = [paciente, profissional, dat_con]
        self.consultas.append(pegaConsulta)
          #self.consultas = [self.papro, dat_con]

        # self.consultas.append(paciente)
        # self.consultas.append(profissional)
        # self.consultas.append(dat_con)
        print("Adicionado consulta!!!")
        # print(paciente)
        # print(profissional)
        # print('DATA CONSULTA: ', dat_con)

    # def abrirConsulta(self,paciente, profissional, dat_con):
    #     self.consultas.append(paciente)
    #     self.consultas.append(profissional)
    #     self.consultas.append(dat_con)
    #     print("Adicionado")
    #     print(paciente)
    #     print(profissional)
    #     print('DATA CONSULTA: ', dat_con)

    def buscarConsulta(self, name):
        for i in self.consultas:
            if name in i:
                print(f" Consulta encontrada!!")
                print(i)
                #print(self.consultas.index(i))

    def listarConsultas(self):
        print("**************************************")
        print("         LISTA DE CONSULTAS           ")
        print("**************************************")
        print(self.consultas)
        for i in self.consultas:
            print(i)



    def deletarConsulta(self, nn):
        for i in self.consultas:
            if nn in i:
                print(f" Consulta deletada!!")
                print(i)
                posicao = self.consultas.index(i)

                print(posicao)
                self.consultas.pop(posicao)
                self.consultas.pop(posicao)
                self.consultas.pop(posicao)

    # def toString(self):
    #     return f'''PACIENTE: {self.paciente}
    # PROFISSIONAL: {self.profissional}
    # Data Consulta: {self.dat_con}'''

    def __repr__(self): ##funciona como o toString, mas esse funciona
        return f'''\nDATA CONSULTA {self.dat_con}
    {self.paciente}
    {self.profissional}'''
    #
    # def __str__(self):
    #     return f'''PACIENTE: {self.paciente}
    #         PROFISSIONAL: {self.profissional}
    #         Data Consulta: {self.dat_con}'''

    def adicionaConsulta(self, paciente, profissional, dat_con):
        print("adiciona Consulta")
        self.consultas.append(self.paciente)
        self.consultas.append(self.profissional)
        self.consultas.append(self.dat_con)

        pegaConsulta = [paciente, profissional, dat_con]
        self.consultas.append(pegaConsulta)

    def toString(self):
        return f'''{self.paciente},
    {self.profissional},
    Data da Consulta: {self.dat_con}'''
    # def __getitem__(self, posicao):
    #     """
    #     Por exemplo, quando tentamos acessar um elemento da sequência usando
    #     slice:
    #         >>> iteravel[2]
    #
    #     O interpretador python chama o __getitem__ do objeto e nos retorna
    #         a posição solicitada
    #
    #     um exemplo:
    #     IN: lista = [1, 2, 3, 4]
    #     IN: lista[0]
    #     OUT: 1
    #     """
    #     return self.seq[posicao]



# p = Paciente('calel', '19/01', 'm')
# pro = Profissional('dr', 'todas', 'f')
#
# x = Consulta(p.toString(), pro.toString(), '19/07')
#
#
#
# x.listarConsultas()









# from datetime import date, time, datetime, timedelta
#
# from paciente import Paciente
# from profissional import Profissional
# class Consulta():
#     consultas = []
#
#     # def __init__(self, data_consulta):
#     #     self.data_consulta = data_consulta
#
#     def __init__(self,paciente, profissional, dat_con):
#         self.profissional = profissional
#         self.dat_con = dat_con
#         self.paciente = paciente
#         self.consultas.append(paciente)
#         self.consultas.append(profissional)
#         self.consultas.append(dat_con)
#         print("Adicionado")
#         print(paciente)
#         print(profissional)
#         print('DATA CONSULTA: ', dat_con)
#
#     # def abrirConsulta(self,paciente, profissional, dat_con):
#     #     self.consultas.append(paciente)
#     #     self.consultas.append(profissional)
#     #     self.consultas.append(dat_con)
#     #     print("Adicionado")
#     #     print(paciente)
#     #     print(profissional)
#     #     print('DATA CONSULTA: ', dat_con)
#
#     def buscarConsulta(self, name):
#         for i in self.consultas:
#             if name in i:
#                 print(f" Consulta encontrada!!")
#                 print(i)
#                 #print(self.consultas.index(i))
#
#     def listarConsultas(self):
#         print("**************************************")
#         print("         LISTA DE CONSULTAS           ")
#         print("**************************************")
#         print(self.consultas)
#         for i in self.consultas:
#             print(i)
#
#
#
#     def deletarConsulta(self, nn):
#         for i in self.consultas:
#             if nn in i:
#                 print(f" Consulta deletada!!")
#                 print(i)
#                 posicao = self.consultas.index(i)
#
#                 print(posicao)
#                 self.consultas.pop(posicao)
#                 self.consultas.pop(posicao)
#                 self.consultas.pop(posicao)
#
#     # def toString(self):
#     #     return f'''PACIENTE: {self.paciente}
#     # PROFISSIONAL: {self.profissional}
#     # Data Consulta: {self.dat_con}'''
#
#     def __repr__(self): ##funciona como o toString, mas esse funciona
#         return f'''\nDATA CONSULTA {self.dat_con}
#     {self.paciente}
#     {self.profissional}'''
#     #
#     # def __str__(self):
#     #     return f'''PACIENTE: {self.paciente}
#     #         PROFISSIONAL: {self.profissional}
#     #         Data Consulta: {self.dat_con}'''
