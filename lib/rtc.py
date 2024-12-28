import machine
# impport the required libraries
from machine import I2C, Pin
from ds1307 import DS1307
import utime

# declarar pines para comunicación I2C
sclPin = Pin(22) # serial clock pin
sdaPin = Pin(21) # serial data pin

# Initiate I2C 
i2c_object = I2C(0,              # argumento posicional - I2C id
                  scl = sclPin,  # argumento con nombre - serial clock pin
                  sda = sdaPin,  # argumento con nombre - serial data pin
                  freq = 400000 )# argumento con nombre - frecuencia i2c 

# clock object at the dedicated i2c port
rtc = DS1307(i2c_object)

#(year,month,date,day,hour,minute,second,p1)=rtc.datetime()

#now = (year,month,date,day,hour,minute,second,0)

def leer_fecha_hora():
        (year,month,date,day,hour,minute,second,p1)=rtc.datetime()
        #year, month, date, day, hour, minute, second = now
        return year, month, date, day, hour, minute, second

#print(rtc.datetime())
#print("probando func...")
#ver = leer_fecha_hora()
#print("func ok...")
#print(ver)