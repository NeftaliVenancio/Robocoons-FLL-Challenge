from setup import *

hub.light.on(Color.MAGENTA)
hub.display.char("1")

#herramienta4 = Instrumento(h4,0,0) #Herramienta

#herramienta4.calibra_Auto(True,150,50) #Calibrar arriba y abajo herramienta

#Corrida 1 - Misón pulpo
robot.movimiento.settings(straight_speed= 600) #Configura velocidad de desplazamiento a 300 mm/s

robot.wait_button(Button.LEFT) # Espera a que se presione el boton izquierdo para inciar la rutina

robot.movimiento.straight(300)
robot.girar(-35,600,True)

robot.wait_button(Button.LEFT)

robot.girar(65,300,True)
robot.movimiento.straight(200)
robot.girar(-35,600,True)
robot.movimiento.straight(100)
robot.girar(48,600,True)
robot.movimiento.straight(125) #Recoge los elementos del tablero
robot.girar(-190,600,True)
robot.movimiento.straight(300)
robot.girar(-50,600,True)
robot.movimiento.straight(400)
robot.movimiento.stop()
