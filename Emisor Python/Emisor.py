import socketio
import time #Importar modulo para el manejo de tiempo
import serial #Importar modulo para comunicacion con puerto serial

sio = socketio.Client() #Creacion del socket

@sio.event
def connect():
    print("Conexion establecida")

@sio.event
def disconnect():
    print('disconnected from server')

#Definicion de las variables necesarias
PUERTOSERIE = "COM7"
BAUDIOS = 9600
#IP = "localhost" #IP del server
#PUERTO = "5000"

sio.connect('http://192.168.0.180:5000')

serialArduino = serial.Serial(PUERTOSERIE, BAUDIOS) #Creacion del objeto serial para la comunicacion con el arduino emisor
time.sleep(1) #Tiempo de retardo
mov = 0
while True:
    try:
        mov = int(serialArduino.readline().decode("ascii").strip().rstrip())#Lectrura y conversion de lo recivido por el puerto serieo
        if mov != 0:
            sio.emit('python', mov)
            print(mov) #Imprime lo recibido por el puerto serie
    except:
        print("An exception occurred")
   