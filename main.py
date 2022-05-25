# # from machine import Pin, PWM
# # import utime
# # 
# # freq = 15000
# # ENA = PWM(Pin(13), freq)
# # IN1 = Pin(12, Pin.OUT)
# # IN2 = Pin(14, Pin.OUT)
# # ENB = PWM(Pin(25), freq)
# # IN3 = Pin(27, Pin.OUT)
# # IN4 = Pin(26, Pin.OUT)
# # 
# # while True:
# #     utime.sleep(1)
# #     ENA.duty(1023)
# #     IN1.value(1)
# #     IN2.value(0)
# #     ENB.duty(1023)
# #     IN3.value(0)
# #     IN4.value(1)
# #     
#     
# # from DCmotor import DCMotor
# # from machine import Pin, PWM
# # from utime  import sleep
# # 
# # freq = 15000
# # ENA = PWM(Pin(13), freq)
# # IN1 = Pin(12, Pin.OUT)
# # IN2 = Pin(14, Pin.OUT)
# # ENB = PWM(Pin(25), freq)
# # IN3 = Pin(27, Pin.OUT)
# # IN4 = Pin(26, Pin.OUT)
# # 
# # dc_motor = DCMotor(IN1, IN2, ENA, IN3, IN4, ENB, min_duty=0, max_duty=1023)
# # 
# # dc_motor.forward(100)
# # sleep(2)
# # dc_motor.stop()
# # sleep(3)
# # dc_motor.backwards(100)
# # sleep(2)
# # dc_motor.stop()
# # sleep(3)
# # dc_motor.right(100)
# # sleep(2)
# # dc_motor.stop()
# # sleep(3)
# # dc_motor.left(100)
# # sleep(2)
# # dc_motor.stop()
# # sleep(3)
# 
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

SD_V = SD.value()
SI_V = SI.value()

PB = Pin(18, Pin.IN, Pin.PULL_DOWN)
PB_I = Pin(2, Pin.OUT)
PB_S = 0

#Probar con sensor de linea
def Forwards(SD_V,SI_V):
    if SI_V == 0 and SD_V == 1:
        dc_motor.right(100)
    elif SI_V == 1 and SD_V == 0:
        dc_motor.left(100)
    elif SI_V == 1 and SD_V == 1:
        dc_motor.forward(100)
    else:
        dc_motor.forward(100)        

def HandR(SD_V,SI_V):
    if SI_V == 0 and SD_V == 1:
        dc_motor.right(100)
    elif SI_V == 1 and SD_V == 0:
        dc_motor.left(100)
    elif SI_V == 1 and SD_V == 1:
        dc_motor.forward(100)
    else:
        dc_motor.right(100)
        
def HandL(SD_V,SI_V):
    if SI_V == 0 and SD_V == 1:
        dc_motor.right(100)
    elif SI_V == 1 and SD_V == 0:
        dc_motor.left(100)
    elif SI_V == 1 and SD_V == 1:
        dc_motor.forward(100)
    else:
        dc_motor.left(100)

def Strategy_One():
    dc_motor.forward(100)
    sleep_ms(300)
    dc_motor.stop()
    sleep_ms(10)
    dc_motor.rigth(100)
    sleep_ms(100)
    dc_motor.rigth(100)
    sleep_ms(100)
    dc_motor.stop()
    sleep_ms(10)
    dc_motor.forward(100)
    sleep_ms(10)
    HandR(SD_V,SI_I)

def Strategy_Two():
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
    HandL(SD_V,SI_I)
    
while True:
    while (PB.value() == 1):
        PB_I.value(1)
        PB_S = PB_S+1
        utime.sleep_ms(300)
        
