# Creación del Entorno

# Importar librerías
import numpy as np

# Construir el entorno en una clase
class Environment(object):
    # Introducir e inicializar los parametros y variables del entorno
    def __init__(self,optimal_temperature=(18.0,24.0),initial_month = 0,initial_number_users = 10, initial_rate_data=60):
        self.monthly_atmospheric_temperature = [1.0,5.0,7.0,10.0,11.0,20.0,23.0,24.0,22.0,10.0,5.0,1.0]
        self.initial_month = initial_month
        self.atmospheric_temperature = self.monthly_atmospheric_temperature[initial_month]
        self.optimal_temperature = optimal_temperature
        self.min_temperature = -20
        self.max_temperature=80
        self.min_number_users=10
        self.max_number_users=100
        self.max_update_users=5
        self.min_rate_data=20
        self.max_rate_data=300
        self.max_update_data=10
        self.initial_number_users= initial_number_users
        self.current_number_users=initial_number_users
        self.initial_rate_data=initial_rate_data
        self.current_rate_data=initial_rate_data
        self.intrinsec_temperature=self.atmospheric_temperature + 1.25*self.current_number_users + 1.25*self.current_rate_data
        self.temperature_ai=self.intrinsec_temperature
        self.temperature_no_ai=(self.optimal_temperature[0] + self.optimal_temperature[1])/2.0 #temperatura del servidor
        self.total_energy_ai=0.0
        self.total_energy_no_ai=0.0
        self.reward=0.0
        self.game_over=0 #será 1 cuando termine 
        self.train=1 #modo entrenamiento=1 #modo simulación=0
        
    # Crear un método que actualice justo después de que la ia ejecute una acción
    #direction =1 si calienta el server; direction=-1 si se enfria el server
    #energy_ai= energia que ha necesitado para enfriar o calentar el server

    def update_env(self, direction, energy_ai, month):
        #OBTENCIÓN DE LA RECOMPENSA

        #calcular la energia gastada por el sistema de refrigeración del server sin AI.
        energy_no_ai = 0

        if (self.temperature_no_ai<self.optimal_temperature[0]):
            energy_no_ai=self.optimal_temperature[0]-self.temperature_no_ai
        #calcular la recompensa

        #escalar la recompensa

        #OBTENCION DEL SIGUIENTE ESTADO

        # actualizar la temperatura atmosferica

        #OBTENCION DEL GAMEOVER
    
    # Crear un método que reinicie el entorno
    
    # Crear un método que nos de en cualquier instante el estado actual, la última recompensa y el game over