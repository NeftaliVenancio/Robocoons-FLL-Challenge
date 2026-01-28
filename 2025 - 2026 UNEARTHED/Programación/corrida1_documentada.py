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

robot.straight(720)      # Avanza 72cm
robot.turn(-46)           # Gira 46 grados a la izquierda
hd.run_angle(100, 70)     # Mueve herramienta derecha 70 grados
robot.straight(80)        # Avanza 8cm
hd.run_angle(100, 25)     # Mueve herramienta 25 grados más
robot.straight(110)       # Avanza 11cm
hd.run_angle(100, -50)    # Retrocede herramienta 50 grados
robot.straight(-50)       # Retrocede 5cm
hd.run_angle(100, -100)   # Retrae herramienta por completo
robot.straight(-150)      # Retrocede 15cm
robot.turn(50)            # Gira para alinearse al retorno

# Aumento de potencia para volver a la base rápido
robot.settings(straight_speed=370, straight_acceleration=300, turn_rate=50, turn_acceleration=100)
robot.straight(-720)      # Regreso a base

print("Misión finalizada. Heading final:", hub.imu.heading())