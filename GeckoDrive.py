import RPi.GPIO as GPIO
from time import sleep
class Servo:
    def _init_(self,pinconfig):
        self.pinmode=pinconfig
        print("Setting Up pins Done!")
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pinconfig, GPIO.OUT)
        self.pwm=GPIO.PWM(pinconfig, 50)
        self.pwm.start(0)
    def Rotate(self,Angle):
        print("Turning to {} angle".format(Angle))
        duty = Angle/ 18 + 2
        GPIO.output(self.pinmode, True)
        self.pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(self.pinmode, False)
        self.pwm.ChangeDutyCycle(0)
    def Close(self):
        print("Closing Servo...")
        self.pwm.stop()
        GPIO.cleanup()