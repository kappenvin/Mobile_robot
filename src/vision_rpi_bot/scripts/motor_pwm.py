import RPi.GPIO as GPIO
import time 

right_motor_a = 24 
right_motor_b =23
right_motor_en =25

left_motor_a = 14
left_motor_b = 15
left_motor_en = 4

GPIO.setmode(GPIO.BCM)

GPIO.setup(right_motor_a, GPIO.OUT)
GPIO.setup(right_motor_b, GPIO.OUT)
GPIO.setup(right_motor_en, GPIO.OUT)

GPIO.setup(left_motor_a, GPIO.OUT)
GPIO.setup(left_motor_b, GPIO.OUT)
GPIO.setup(left_motor_en, GPIO.OUT)

pwm_r = GPIO.PWM(right_motor_en, 1000)
pwm_l = GPIO.PWM(left_motor_en, 1000)

pwm_r.start(25)
pwm_l.start(25)

def forward (seconds):
    print("moving forward")
    GPIO.output(right_motor_a,GPIO.HIGH)
    GPIO.output(right_motor_b,GPIO.LOW)
    GPIO.output(left_motor_a,GPIO.HIGH)
    GPIO.output(left_motor_b,GPIO.LOW)
    time.sleep(2)

def exit_gpio():
    GPIO.cleanup()

def stop ():
    print("stop motor")
    pwm_l.ChangeDutyCycle(0)
    pwm_l.ChangeDutyCycle(0)

def main():
    forward(2)
    stop()
    exit_gpio()

if __name__ == "__main__":
    main()


