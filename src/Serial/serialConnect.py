import serial
from src.ConectDatabase.ConectReal import ConnectBancoReal

class SerialConnect:
    def __init__(self):
        self.serial_conect()
        
    
    def serial_conect(self, porta='/dev/ttyACM0'):
        MSP = serial.Serial(porta, 9600)
        telemetria = list()
        vectorTelemetria = []
        # dataAux = []

        data = MSP.readline().decode()
        dataSplit = data.split(',')
        print(data)          
        try:
            connectBd = ConnectBancoReal()
            while True:
                MSP.flushOutput()
                MSP.flushInput()
                print(dataSplit)
                vectorTelemetria[0] = dataSplit[0]
                vectorTelemetria[1] = dataSplit[1]
                vectorTelemetria[2] = dataSplit[2]
                vectorTelemetria[3] = dataSplit[3]
                connectBd.SaveTelemetria(vectorTelemetria)
                dataAux = vectorTelemetria
                vectorTelemetria.clear()
                # if (vectorTelemetria[0] > 9):
                #     self.avg_telemetria(dataAux)
                #     dataAux.clear()
        except:
            print("erro para instanciar porta serial", serial.SerialException())

    # def avg_telemetria(telemetria):
    #     avg_tel = []
    #     if (len(telemetria) > 0):
    #         for i in range(len(telemetria)):
    #             for b in range(len(telemetria[0])):
    #                 avg_tel[i] = avg_tel[i] + telemetria[b]
    #     return avg_tel

if __name__ == '__main__':
    SerialConnect()