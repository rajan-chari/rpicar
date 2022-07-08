from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from time import sleep

# Hardware PWM pins
# gpio 18 - pin 12
# gpio 19 - pin 36
# gpio 12 - pin 32
# gpio 13 - pin 33
# gpio 14 - pin 8
# gpio 15 - pin 10

# Reference
# https://c2plabs.com/blog/2019/06/22/dc-motor-control-using-tb6612fng-driver-and-raspberry-pi-gpiozero-lib/
# https://www.raspberrypi.com/documentation/computers/os.html#gpio-and-the-40-pin-header
# https://toshiba.semicon-storage.com/info/docget.jsp?did=10660&prodName=TB6612FNG

PWM_A_PIN = 12
A_IN1_PIN = 14
A_IN2_PIN = 15

pwm_a = PWMOutputDevice (PWM_A_PIN,True, 0, 80000)
cw_a = DigitalOutputDevice(A_IN1_PIN, True, 0)
ccw_a = DigitalOutputDevice(A_IN2_PIN, True, 0)

def RotateMotorCW(val):
    print(f"RotateMotor_CW: {val}")
    pwm_a.value = val/100.0
    cw_a.value = 1
    ccw_a.value = 0


def RotateMotorCCW(val):
    print(f"RotateMotor_CCW: {val}")
    pwm_a.value = val/100.0
    cw_a.value = 0
    ccw_a.value = 1

def StopMotor():
    print(f"StopMotor")
    pwm_a.value = 0
    cw_a.value = 0
    ccw_a.value = 0

def main():
    speed_increment = .10
    try:
        while True:
            for speed in range (10, 60, 10):
                RotateMotorCW(speed)
                sleep(3)
            for speed in range (40, 0, -10):
                RotateMotorCW(speed)
                sleep(3)
            StopMotor()
            sleep(3)
            for speed in range (10, 60, 10):
                RotateMotorCCW(speed)
                sleep(3)
            for speed in range (40, 0, -10):
                RotateMotorCCW(speed)
                sleep(3)
            StopMotor()
            sleep(3)
    except KeyboardInterrupt:
            print ('Interrupted')
    StopMotor()

if __name__ == "__main__":
        main()