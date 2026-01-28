from Robot import *
from Instrumento import *

hub = PrimeHub()

hub.system.set_stop_button(Button.BLUETOOTH)

md = Motor(Port.B,Direction.CLOCKWISE)
mi = Motor(Port.A,Direction.COUNTERCLOCKWISE)

h1 = Motor(Port.C,Direction.CLOCKWISE)
h2 = Motor(Port.D,Direction.CLOCKWISE)
h3 = Motor(Port.F,Direction.COUNTERCLOCKWISE)
h4 = Motor(Port.E,Direction.COUNTERCLOCKWISE)

BOT_TURN_RATE=150
BOT_TURN_RATE_FAST=350

robot = Robot(hub,mi,md) #Construccion del objeto robot del modulo Robocoons

#drive = DriveBase(mi,md,42,110)

#drive.settings(straight_speed=200+300, straight_acceleration=250, turn_rate=BOT_TURN_RATE, turn_acceleration=600)

#drive_set = drive.settings()

#drive.use_gyro(True)

#drive.heading_control.target_tolerances(position=8)

#drive.distance_control.target_tolerances(position=8)





