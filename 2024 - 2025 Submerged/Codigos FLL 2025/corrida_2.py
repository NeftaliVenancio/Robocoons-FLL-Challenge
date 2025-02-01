from setup import *

hub.light.on(Color.CYAN)
hub.display.char("2")

#Corrida 2 - Misón pulpo
robot.movimiento.settings(straight_speed= 600) #Configura velocidad de desplazamiento a 300 mm/s

robot.wait_button(Button.LEFT) # Espera a que se presione el boton izquierdo para inciar la rutina

robot.movimiento.straight(250)
robot.girar(-90,600,True)
robot.movimiento.straight(620)
robot.girar(90,600,True)
robot.movimiento.straight(250)
robot.movimiento.straight(-150)
robot.girar(-40,600,True)
robot.movimiento.straight(250)
robot.girar(-13,600,True)
robot.movimiento.straight(250)
robot.girar(-53,600,True)
robot.movimiento.straight(350)
robot.girar(-60,600,True)
robot.movimiento.straight(600)

robot.movimiento.stop()


import corrida_3