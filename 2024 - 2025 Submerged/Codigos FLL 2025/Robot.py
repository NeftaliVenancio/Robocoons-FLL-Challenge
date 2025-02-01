from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

class Robot:
    """
    Clase Robot diseñada para interactuar con el LEGO® SPIKE™ Prime.
    Proporciona funcionalidades para controlar motores y sensores, así como para realizar movimientos básicos.
    
    Atributos:
        brick (PrimeHub): El hub central de LEGO® SPIKE™ Prime.
        mI (Motor): Motor izquierdo.
        mD (Motor): Motor derecho.
        sI (ColorSensor): Sensor de color izquierdo.
        sD (ColorSensor): Sensor de color derecho.
        db (DriveBase): Base de manejo para controlar los movimientos del robot.
        
    Métodos:
        __init__: Inicializa una nueva instancia de la clase Robot.
        button_pressed: Verifica si un botón específico está presionado.
        wait_button: Espera hasta que un botón específico sea presionado.
        buttopn_program_stop: Establece un botón para detener el programa (Nombre del método parece tener un typo).
        girar: Gira el robot un ángulo específico a una velocidad dada.
    """

    d_rueda = 40 #Diametro de la rueda en mm
    d_eje =  108#Distancia entre las ruedas en mm (eje)
        
    def __init__(self, HUB=PrimeHub, MotorI=Motor, MotorD=Motor):
        """
        Inicializa el robot con los motores y sensores especificados.
        
        Parámetros:
            HUB (PrimeHub): El hub central de LEGO® SPIKE™ Prime.
            MotorI (Motor): Motor conectado al puerto izquierdo.
            MotorD (Motor): Motor conectado al puerto derecho.
            SensorColorI (ColorSensor): Sensor de color conectado a un puerto izquierdo.
            SensorColorD (ColorSensor): Sensor de color conectado a un puerto derecho.
        """
        self._brick = HUB

        self._mI = MotorI
        self._mD = MotorD

        self._db = DriveBase(self._mI, self._mD, self.d_rueda, self.d_eje)

        self.movimiento = self._db

        self._db.use_gyro(True)
    def button_pressed(self, button=Button):
        """
        Verifica si un botón específico está presionado.
        
        Parámetros:
            button (Button): El botón a verificar.
            
        Retorna:
            bool: True si el botón está presionado, False en caso contrario.
        """
        presed = self._brick.buttons.pressed()
        return button in presed

    def wait_button(self, button=Button):
        """
        Espera hasta que un botón específico sea presionado.
        
        Parámetros:
            button (Button): El botón a esperar.
        """
        while True:
            presed = self._brick.buttons.pressed()
            if button in presed:
                print(button)
                break

        while any(self._brick.buttons.pressed()):
            wait(10)

    def buttopn_program_stop(self, button=Button):
        """
        Establece un botón para detener el programa. (Revisar el nombre del método para corrección de typo)
        
        Parámetros:
            button (Button): El botón para detener el programa.
        """
        self._brick.system.set_stop_button(button)

    def girar(self, angulo, velocidad=150, esperar = False):
        """
        Gira el robot un ángulo específico a una velocidad dada.
        
        Parámetros:
            angulo (int): El ángulo de giro en grados.
            velocidad (int): La velocidad de giro.
        """
        
        self._db.reset()
        self._db.settings(turn_rate=velocidad)
        self._db.turn(angulo,Stop.HOLD,wait = esperar)

    def angulo_actual(self):
        """
        Retorna el ángulo actual del robot.
        
        Retorna:
            int: El ángulo actual del robot.
        """
        return self._db.angle()

    def align(speed=200, ms=2000, turn=0):
        self._db.use_gyro(False)
        self._db.drive(speed, turn)
        sw = StopWatch()
        # while sw.time()<ms and not (me.stalled() and mf.stalled()):
        #     pass
        # wait(100)
        wait(ms)
        self._db.stop()
        # while not hub.imu.stationary(): pass
        self._db.use_gyro(True)
        wait(100)
    