from setup import *

hub.light.on(Color.MAGENTA)

#herramienta4 = Instrumento(h4,0,0) #Herramienta

#herramienta4.calibra_Auto(True,150,50) #Calibrar arriba y abajo herramienta

#Corrida 1 - Misón pulpo
robot.movimiento.settings(straight_speed= 600) #Configura velocidad de desplazamiento a 300 mm/s

robot.wait_button(Button.LEFT) # Espera a que se presione el boton izquierdo para inciar la rutina
robot.movimiento.straight(50)
robot.girar(-45,600,True) 
robot.movimiento.straight(500) #Complets misión pulpo
robot.movimiento.straight(-400)
robot.movimiento.stop()


import corrida_2

