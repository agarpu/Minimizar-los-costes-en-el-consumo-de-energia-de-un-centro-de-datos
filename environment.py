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
        
    # Crear un método que actualice justo después de que la IA ejecute una acción
    #direction =1 si calienta el server; direction=-1 si se enfria el server
    #energy_ai= energia que ha necesitado para enfriar o calentar el server

    def update_env(self, direction, energy_ai, month):
        #OBTENCIÓN DE LA RECOMPENSA
        # Calcular la energía gastada por el sistema de refrigeración del server sin AI.
        energy_no_ai = 0

        if (self.temperature_no_ai<self.optimal_temperature[0]):
            energy_no_ai=self.optimal_temperature[0]-self.temperature_no_ai
            self.temperature_no_ai=self.optimal_temperature[0]
        elif(self.temperature_no_ai>self.optimal_temperature[1])
            energy_no_ai=self.temperature_no_ai-self.optimal_temperature[1]
            self.temperature_no_ai=self.optimal_temperature[1]

        # Calcular la recompensa
        self.reward = energy_no_ai - energy_ai

        # Escalar la recompensa
        self.reward = 1e-3*self.reward

        #OBTENCIÓN DEL SIGUIENTE ESTADO
        # actualizar la temperatura atmosferica
        self.atmospheric_temperature=self.monthly_atmospheric_temperature[month]
        
        #actualizar el número de usuarios
        self.current_number_users += np.random.randint(-self.max_number_users,self.max_number_users)
        if(self.current_number_users<self.min_number_users):
            self.current_number_users=self.min_number_users
        elif(self.current_number_users>self.max_number_users)
            self.current_number_users=self.max_number_users
        #actualizar la tasa de transferencia
        self.current_rate_data += np.random.randint(-self.max_number_rate,self.max_number_rate)
        if(self.current_rate_data<self.min_rate_data):
            self.current_rate_data=self.min_rate_data
        elif(self.current_rate_data>self.max_rate_data)
            self.current_rate_data=self.max_rate_data
        # Actualizar la variación de temperatura intrínseca
        past_intrinsic_temperature= self.intrinsec_temperature
        self.intrinsec_temperature=self.atmospheric_temperature + 1.25*self.current_number_users + 1.25*self.current_rate_data
        delta_intrinsec_temperature=self.intrinsec_temperature-past_intrinsic_temperature

        # Calcular la variación de temperatura causada por la IA
        if(direction==-1):
            delta_temperature_ai = -energy_ai
        elif(direction==1):
            delta_temperature_ai=energy_ai

        #calcular la nueva temperatura del server cuando hay IA
        self.temperature_ai += delta_intrinsec_temperature+delta_temperature_ai

        #calcular la nueva temperatura del server cuando no hay IA
        self.temperature_no_ai += delta_intrinsec_temperature

        #OBTENCION DEL GAME_OVER
        if(self.temperature_ai<self.min_temperature):
            if(self.train==1):
                self.game_over=1
            else:
                self.total_energy_ai += self.optimal_temperature[0]-self.temperature_ai
                self.temperature_ai=self.optimal_temperature[0]
        if(self.temperature_ai>self.max_temperature)
            if(self.train==1):
                self.game_over=1
            else:
                self.total_energy_ai += self.temperature_ai-self.optimal_temperature[1]
                self.temperature_ai=self.optimal_temperature[1]

        # ACTUALIZAR LOS SCORES

        #  Calcular la energía total gastada por la IA


        # DEVOLVER EL SIGUIENTE ESTADO, RECOMPENSA Y GAME OVER

