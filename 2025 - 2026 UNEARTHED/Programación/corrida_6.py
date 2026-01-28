from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Inicialización del Hub y Dispositivos
hub = PrimeHub()

# Configuración de motores de tracción
mi = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
md = Motor(Port.E, positive_direction=Direction.CLOCKWISE)
sensorc = ColorSensor(Port.D)

# Configuración de motores para herramientas (attachments)
hi = Motor(Port.B, positive_direction=Direction.CLOCKWISE)
hd = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)

# Configuración de la base motriz (Ruedas: 43.2mm, Entre-eje: 161mm)
robot = DriveBase(mi, md, 43.2, 161)

# Configuración de rendimiento inicial (Velocidad, Aceleración, Giro)
# robot.settings(velocidad_recta, aceleracion_recta, vel_giro, acel_giro)
robot.settings(straight_speed=300, straight_acceleration=200, turn_rate=50, turn_acceleration=100)

# Activación del Giroscopio para mayor precisión en giros
robot.use_gyro(True)

# Reinicio de posición de herramientas
hi.reset_angle(0)
hd.reset_angle(0)

# --- INICIO DE LA MISIÓN ---

robot.straight(100)      # Avanza 72cm
robot.turn(-55)

hi.run_angle(500,-350)
robot.straight(320)
robot.turn(10)

hd.run_angle(500,-350)
robot.settings(straight_speed=100, straight_acceleration=200, turn_rate=50, turn_acceleration=100)
robot.straight(-250)
robot.straight(100)
robot.turn(-10)
hd.run_angle(500,300)
robot.settings(straight_speed=300, straight_acceleration=200, turn_rate=50, turn_acceleration=100)
robot.turn(2)
robot.straight(150)
robot.turn(-20)
robot.straight(-600)
print("Misión finalizada. Heading final:", hub.imu.heading())