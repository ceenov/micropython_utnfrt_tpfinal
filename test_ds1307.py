import machine
# impport the required libraries
from machine import I2C, Pin
from lib.ds1307 import DS1307
import utime

i2c = machine.I2C(0, scl=machine.Pin(22), sda=machine.Pin(21))

print('escanea  bus i2c...')
devices = i2c.scan()

if len(devices) == 0:
  print("No hay dispositivos i2c!")
else:
  print('Se encontro i2c dispositivos:',len(devices))

  for device in devices:  
    print(" Direccion Decimal: ",device," | Direccion Hexa: ",hex(device))

print()

# declarar pines para comunicación I2C
sclPin = Pin(22) # serial clock pin
sdaPin = Pin(21) # serial data pin

#i2c = I2C(scl=sclPin, sda=sdaPin)


# Initiate I2C 
i2c_object = I2C(0,              # argumento posicional - I2C id
                  scl = sclPin,  # argumento con nombre - serial clock pin
                  sda = sdaPin,  # argumento con nombre - serial data pin
                  freq = 400000 )# argumento con nombre - frecuencia i2c 

result = I2C.scan(i2c_object) # scan i2c bus for available devices

print("escanea  bus i2c : ", result)
if result != []:
   print("I2C conexion correcta")
else:
    print("reintentar")


print("configurando DS1307...")
# clock object at the dedicated i2c port
clockObject = DS1307(i2c_object)

#  enable the RTC module
#clockObject.halt(False) # 32 khz crystal enable

choice = input("Desea cambiar los datos de fecha y hora por defecto ( s / n ) : ")

if choice == "s":
    
    print("establecer los datos de fecha y hora por defecto")
    year = int(input("ano : "))
    month = int(input("mes (Ene --> 1 , Dic --> 12): "))
    date = int(input("dia (1...31): "))

    day = int(input("dia (1 --> Lunes , 2 --> Martes ... 0 --> Domingo): ")) # 1 --> Lunes , 2 --> Martes ... 0 --> Domingo

    hour = int(input("hora (24 Horas formato): "))
    minute = int(input("minuto : "))
    second = int(input("segundo : "))

    now = (year,month,date,day,hour,minute,second,0)
    clockObject.datetime(now)

else:
    print("Los datos por defecto no se modifican ")
    print("Ajustes de fecha y hora por defecto : ")
    default = clockObject.datetime()
    print("Ano : ",default[0])
    print("Mes : ",default[1])
    print("dato : ",default[2])
    print("dia : ",default[3])
    print("hora : ",default[4])
    print("minuto : ",default[5])
    print("segundo : ",default[6],"\n")
    utime.sleep(5) # time for user to read serial data properly
    
print("comenzando while true...")
while True:
    (year,month,date,day,hour,minute,second,p1)=clockObject.datetime()
    utime.sleep(1)
    print(clockObject.datetime())