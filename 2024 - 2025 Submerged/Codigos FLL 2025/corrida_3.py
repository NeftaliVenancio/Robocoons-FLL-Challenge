from setup import *

hub.light.on(Color.GREEN)
hub.display.char("3")

#Corrida 2 - Misón pulpo
robot.movimiento.settings(straight_speed= 600) #Configura velocidad de desplazamiento a 300 mm/s

robot.wait_button(Button.LEFT) # Espera a que se presione el boton izquierdo para inciar la rutina

robot.movimiento.straight(200)
robot.girar(30,600,True)
robot.movimiento.straight(230)
robot.girar(50,600,True)
robot.movimiento.straight(255)
robot.movimiento.straight(-200)
robot.girar(135,600,True)
robot.movimiento.straight(430)

robot.movimiento.stop()


import corrida_4