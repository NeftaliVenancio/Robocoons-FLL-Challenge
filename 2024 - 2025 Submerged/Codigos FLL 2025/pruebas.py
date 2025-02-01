#from pybricks.hubs import PrimeHub
#from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
#from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
#from pybricks.robotics import DriveBase
#from pybricks.tools import wait, StopWatch


from setup import *

while True:

    robot.girar(90,300,True)

robot.wait_button(Button.LEFT)

robot.girar(180)

robot.wait_button(Button.LEFT)

pescar = Instrumento(h1,0,100)

elevador = Instrumento(h3,0,100)


#pescar.calibra_Auto(True,200,50)

elevador.calibra_Auto(True,200,50)

elevador.print_limites()


while True:
    if robot.button_pressed(Button.LEFT):

        elevador.bajar(100)

    if robot.button_pressed(Button.RIGHT):
        
        elevador.subir(100)

while True:
    if robot.button_pressed(Button.LEFT):
        elevador.abajo(300)
        print(pescar.actuador.angle())

    if robot.button_pressed(Button.RIGHT):
        elevador.arriba(300)
        print(pescar.actuador.angle())
