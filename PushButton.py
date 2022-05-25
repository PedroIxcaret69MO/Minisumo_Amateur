from machine import Pin, PWM
import utime 

PB = Pin(18, Pin.IN, Pin.PULL_DOWN)
P2 = Pin(2, Pin.OUT)
PB_S = 0

last_time = 0
show = 300

while True:
    while (PB.value() == 1):
        P2.value(1)
        PB_S = PB_S+1
        utime.sleep_ms(300)
        P2.value(0)
    timer_elapsed = utime.ticks_diff(utime.ticks_ms(), last_time)
    if PB_S == 0:
        if (timer_elapsed > show):
            print("Default")
            last_time = utime.ticks_ms()
    elif PB_S == 1:
        if (timer_elapsed > show):
            print("HandD")
            last_time = utime.ticks_ms()
    elif PB_S == 2:
        if (timer_elapsed > show):
            print("HandI")
            last_time = utime.ticks_ms()
    elif PB_S == 3:
        if (timer_elapsed > show):
            print("S1")
            last_time = utime.ticks_ms()
    elif PB_S == 4:
        if (timer_elapsed > show):
            print("S2")
            last_time = utime.ticks_ms()
    elif PB_S >= 5:
        PB_S = 0
