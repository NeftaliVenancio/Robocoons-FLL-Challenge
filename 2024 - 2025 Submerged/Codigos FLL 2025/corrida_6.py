from setup import *

hub.light.on(Color.ORANGE)
hub.display.char("6")

#herramienta4 = Instrumento(h4,0,0) #Herramienta

#herramienta4.calibra_Auto(True,150,50) #Calibrar arriba y abajo herramienta

#Corrida 1 - Misón pulpo
robot.movimiento.settings(straight_speed= 200) #Configura velocidad de desplazamiento a 300 mm/s

robot.wait_button(Button.LEFT) # Espera a que se presione el boton izquierdo para inciar la rutina

robot.movimiento.straight(150)
robot.girar(88,600,True)
robot.movimiento.straight(1080)
robot.movimiento.straight(-200)
robot.girar(-25,600,True)
robot.movimiento.straight(400)
robot.girar(80,600,True)
robot.movimiento.straight(500)

robot.movimiento.stop()