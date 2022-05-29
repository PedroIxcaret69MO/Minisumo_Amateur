# from machine import Pin, PWM
# import utime
# 
# freq = 15000
# ENA = PWM(Pin(13), freq)
# IN1 = Pin(12, Pin.OUT)
# IN2 = Pin(14, Pin.OUT)
# ENB = PWM(Pin(25), freq)
# IN3 = Pin(27, Pin.OUT)
# IN4 = Pin(26, Pin.OUT)
# 
# while True:
#     utime.sleep(1)
#     ENA.duty(1023)
#     IN1.value(1)
#     IN2.value(0)
#     ENB.duty(1023)
#     IN3.value(0)
#     IN4.value(1)

#--------------------------Prueba sensor y motores
# from DCmotor import DCMotor
# from machine import Pin, PWM
# from utime  import sleep
# 
# freq = 15000
# ENA = PWM(Pin(13), freq)
# IN1 = Pin(12, Pin.OUT)
# IN2 = Pin(14, Pin.OUT)
# ENB = PWM(Pin(25), freq)
# IN3 = Pin(27, Pin.OUT)
# IN4 = Pin(26, Pin.OUT)
# 
# dc_motor = DCMotor(IN1, IN2, ENA, IN3, IN4, ENB, min_duty=0, max_duty=1023)
# 
# SD = Pin(4, Pin.IN, Pin.PULL_DOWN)
# SI = Pin(16, Pin.IN, Pin.PULL_DOWN)
#  
# while True:
#     if (SD.value() == 1 and SI.value() == 1):
#         dc_motor.forward(75)
#         sleep(1)
#     else:
#         dc_motor.stop()

#----------------------------------------------------------
# from DCmotor import DCMotor
# from machine import Pin, PWM
# from utime  import sleep
# 
# freq = 15000
# ENA = PWM(Pin(13), freq)
# IN1 = Pin(12, Pin.OUT)
# IN2 = Pin(14, Pin.OUT)
# ENB = PWM(Pin(25), freq)
# IN3 = Pin(27, Pin.OUT)
# IN4 = Pin(26, Pin.OUT)
# 
# dc_motor = DCMotor(IN1, IN2, ENA, IN3, IN4, ENB, min_duty=0, max_duty=1023)
# 
# dc_motor.forward(100)
# sleep(2)
# dc_motor.stop()
# sleep(3)
# dc_motor.backwards(100)
# sleep(2)
# dc_motor.stop()
# sleep(3)
# dc_motor.right(100)
# sleep(2)
# dc_motor.stop()
# sleep(3)
# dc_motor.left(100)
# sleep(2)
# dc_motor.stop()
# sleep(3)

#---------------Main
from machine import Pin, PWM
from utime import sleep_ms
from DCmotor import DCMotor

freq = 15000
ENA = PWM(Pin(13), freq)
IN1 = Pin(12, Pin.OUT)
IN2 = Pin(14, Pin.OUT)
ENB = PWM(Pin(25), freq)
IN3 = Pin(27, Pin.OUT)
IN4 = Pin(26, Pin.OUT)

dc_motor = DCMotor(IN1, IN2, ENA, IN3, IN4, ENB, min_duty=0, max_duty=1023)

SD = Pin(4, Pin.IN, Pin.PULL_DOWN)
SI = Pin(16, Pin.IN, Pin.PULL_DOWN)

# SD_V = SD.value()
# SI_V = SI.value()

PB = Pin(18, Pin.IN, Pin.PULL_DOWN)
PI = Pin(2, Pin.OUT)
PB_S = 0
arr = Pin(15, Pin.IN, Pin.PULL_DOWN)

#Probar con sensor de linea
def Forwards(SD,SI):
    if SI.value() == 0 and SD.value() == 1:
        dc_motor.right(100)
    elif SI.value() == 1 and SD.value() == 0:
        dc_motor.left(100)
    elif SI.value() == 1 and SD.value() == 1:
        dc_motor.forward(100)
    else:
        dc_motor.forward(100)        

def HandR(SD,SI):
    if SI.value() == 0 and SD.value() == 1:
        dc_motor.right(100)
    elif SI.value() == 1 and SD.value() == 0:
        dc_motor.left(100)
    elif SI.value() == 1 and SD.value() == 1:
        dc_motor.forward(100)
    else:
        dc_motor.right(100)
        
def HandL(SD,SI):
    if SI.value() == 0 and SD.value() == 1:
        dc_motor.right(100)
    elif SI.value() == 1 and SD.value() == 0:
        dc_motor.left(100)
    elif SI.value() == 1 and SD.value() == 1:
        dc_motor.forward(100)
    else:
        dc_motor.left(100)

def Strategy_One(SD,SI):
    if SI.value() == 0 and SD.value() == 1:
        dc_motor.right(100)
    elif SI.value() == 1 and SD.value() == 0:
        dc_motor.left(100)
    elif SI.value() == 1 and SD.value() == 1:
        dc_motor.forward(100)
    else:
        count = 0
        while count <= 2:
            dc_motor.forward(100)
            sleep_ms(300)
            dc_motor.stop()
            sleep_ms(10)
            dc_motor.right(100)
            sleep_ms(100)
            dc_motor.right(100)
            sleep_ms(100)
            dc_motor.stop()
            sleep_ms(10)
            dc_motor.forward(100)
            sleep_ms(10)
            if count == 1:
                break
            count += 1
    

def Strategy_Two(SD,SI):
    if SI.value() == 0 and SD.value() == 1:
        dc_motor.right(100)
    elif SI.value() == 1 and SD.value() == 0:
        dc_motor.left(100)
    elif SI.value() == 1 and SD.value() == 1:
        dc_motor.forward(100)
    else:
        count = 0
        while count <= 2:
            dc_motor.forward(100)
            sleep_ms(300)
            dc_motor.stop()
            sleep_ms(10)
            dc_motor.left(100)
            sleep_ms(100)
            dc_motor.left(100)
            sleep_ms(100)
            dc_motor.stop()
            sleep_ms(10)
            dc_motor.forward(100)
            sleep_ms(10)
            if count == 1:
                break
            count += 1
            
while True:
    while(arr.value() == 0):
        if(PB.value() == 1):
            PI.value(1)
            PB_S = PB_S+1
            sleep_ms(300)
            PI.value(0)
            #print(str(PB_S))
            dc_motor.stop()

    while(arr.value() == 1):
        for i in range (180000):
            if PB_S == 0:
                Forwards(SD,SI)
                if(arr.value() == 0):
                    break
            elif PB_S == 1:
                HandR(SD,SI)
                if(arr.value() == 0):
                    break
            elif PB_S == 2:
                HandL(SD,SI)
                if(arr.value() == 0):
                    break
            elif PB_S == 3:
                Strategy_One(SD,SI)
                if(arr.value() == 0):
                    break
            elif PB_S == 4:
                Strategy_Two(SD,SI)
                if(arr.value() == 0):
                    break
            elif PB_S >= 5:
                PB_S = 0
            sleep_ms(1)
        dc_motor.stop()
        PB_S = 0
