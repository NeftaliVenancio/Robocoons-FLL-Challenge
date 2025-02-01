from setup import *

hub.light.on(Color.RED)
hub.display.char("5")

#herramienta4 = Instrumento(h4,0,0) #Herramienta

#herramienta4.calibra_Auto(True,150,50) #Calibrar arriba y abajo herramienta

#Corrida 1 - Misón pulpo
robot.movimiento.settings(straight_speed= 150) #Configura velocidad de desplazamiento a 300 mm/s

robot.wait_button(Button.LEFT) # Espera a que se presione el boton izquierdo para inciar la rutina
robot.movimiento.straight(200)
robot.girar(88,70,True)
robot.movimiento.straight(605)
robot.movimiento.settings(straight_speed= 600)
robot.movimiento.straight(-800)

robot.movimiento.stop()

import corrida_6
