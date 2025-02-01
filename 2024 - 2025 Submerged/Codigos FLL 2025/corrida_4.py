from setup import *

hub.light.on(Color.YELLOW)
hub.display.char("4")

pescar = Instrumento(h3,300,0)
#Corrida 2 - Misón pulpo
robot.movimiento.settings(straight_speed= 600) #Configura velocidad de desplazamiento a 300 mm/s
robot.wait_button(Button.LEFT) # Espera a que se presione el boton izquierdo para inciar la rutina


pescar.calibra_Auto(False,50,100,100)

pescar.actuador.track_target(15) #Arriba


robot.movimiento.straight(200)
robot.girar(25,600,True)
robot.movimiento.straight(520)
pescar.actuador.run_target(600,95) #abajo
pescar.actuador.run_target(600,45) #Arriba
robot.girar(-80,600,True)
robot.movimiento.straight(70)
pescar.actuador.run_target(600,75) #abajo
pescar.actuador.run_target(600,110) #Arriba
robot.girar(-40,600,True)
robot.movimiento.straight(100)
pescar.actuador.run_target(600,10) #Arriba

robot.movimiento.straight(-170)

robot.movimiento.stop()


import corrida_5
#robot.girar(190,600,True)
#robot.movimiento.straight(500)