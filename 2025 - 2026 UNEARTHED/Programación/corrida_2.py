from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
hub.system.set_stop_button(Button.BLUETOOTH)

mi = Motor(Port.A, positive_direction= Direction. COUNTERCLOCKWISE)
md = Motor(Port.E,positive_direction= Direction. CLOCKWISE)
sensorc = ColorSensor(Port.D)


hi = Motor(Port.B,positive_direction= Direction.CLOCKWISE)
hd = Motor(Port.F,positive_direction= Direction.COUNTERCLOCKWISE)

robot = DriveBase(mi,md,43.2,161) #Configuración de la base motriz

print(robot.settings())

robot.settings(straight_speed=300, straight_acceleration= 200, turn_rate= 50, turn_acceleration=100)

print(robot.settings())

print(hub.imu.heading())
robot.use_gyro(True);
print(hub.imu.heading())

hi.reset_angle(0)
hd.reset_angle(0)

robot.straight(720)
robot.turn(-46)
hd.run_angle(100,120)
robot.straight(80)
hd.run_angle(100,50)
robot.straight(110)
hd.run_angle(100,-50)
robot.straight(-50)
hd.run_angle(100,-100)
robot.straight(-150)
robot.turn(50)
robot.settings(straight_speed=370, straight_acceleration= 300, turn_rate= 50, turn_acceleration=100)
robot.straight(-720)
#robot.straight(-780)

print(hub.imu.heading())
