import serial

class Serial:
    def serial_conect(self, porta='/dev/ttyACM0'):
        MSP = serial.Serial(str(porta), 9600, timeout=3)
        telemetria = list()
        try:
            while True:
                MSP.flushOutput()
                MSP.flushInput()

                data = MSP.readline().decode()
                dataSplit = data.split(',')
                if (len(dataSplit) != 0):
                    telemetria[0].append(dataSplit[0])
                    telemetria[1].append(dataSplit[1])
                    telemetria[2].append(dataSplit[2])
                    telemetria[3].append(dataSplit[3])
                    if (telemetria[0] > 9):
                        telemetria[0].clear()
                        telemetria[1].clear()
                        telemetria[2].clear()
                        telemetria[3].clear()
        except:
            print("erro para instanciar porta serial")

    def avg_telemetria(telemetria):
        avg_tel = []
        if (len(telemetria) > 0):
            for i in range(len(telemetria)):
                for b in range(len(telemetria[0])):
                    avg_tel[i] = avg_tel[i] + telemetria[b]
        return avg_tel