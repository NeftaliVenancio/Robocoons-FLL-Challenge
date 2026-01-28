from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

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

robot.straight(180)
robot.turn(90)
robot.straight(960)
robot.straight(-75)
robot.turn(45)


print(hub.imu.heading())
