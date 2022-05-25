
class DCMotor:
    def __init__(self, IN1, IN2, ENA, IN3, IN4, ENB, min_duty=0, max_duty=1023):
        self.IN1 = IN1
        self.IN2 = IN2
        self.ENA = ENA
        self.IN3 = IN3
        self.IN4 = IN4
        self.ENB = ENB
        self.min_duty = min_duty
        self.max_duty = max_duty
    
    def forward(self, speed):
        self.speed = speed
        self.ENA.duty(self.duty_cycle(self.speed)) #DERECHO
        self.IN1.value(1)
        self.IN2.value(0)
        self.ENB.duty(self.duty_cycle(self.speed)) #IZQUIERDO
        self.IN3.value(0)
        self.IN4.value(1)
    
    def backwards(self, speed):
        self.speed = speed
        self.ENA.duty(self.duty_cycle(self.speed)) #DERECHO
        self.IN1.value(0)
        self.IN2.value(1)
        self.ENB.duty(self.duty_cycle(self.speed)) #IZQUIERDO
        self.IN3.value(1)
        self.IN4.value(0)
    
    def right(self, speed):
        self.speed = speed
        self.ENA.duty(self.duty_cycle(self.speed)) #DERECHO
        self.IN1.value(0)
        self.IN2.value(1)
        self.ENB.duty(self.duty_cycle(self.speed)) #IZQUIERDO
        self.IN3.value(0)
        self.IN4.value(1)
        
    def left(self, speed):
        self.speed = speed
        self.ENA.duty(self.duty_cycle(self.speed)) #DERECHO
        self.IN1.value(1)
        self.IN2.value(0)
        self.ENB.duty(self.duty_cycle(self.speed)) #IZQUIERDO
        self.IN3.value(1)
        self.IN4.value(0)
    
    def stop(self):
        self.ENA.duty(0) #DERECHO
        self.IN1.value(0)
        self.IN2.value(0)
        self.ENB.duty(0) #IZQUIERDO
        self.IN3.value(0)
        self.IN4.value(0)
    
    def duty_cycle(self, speed):
        if self.speed <= 0 or self.speed > 100:
          duty_cycle = 0
        else:
          duty_cycle = int(self.min_duty + (self.max_duty - self.min_duty)*((self.speed - 1)/(100-1)))
        return duty_cycle
