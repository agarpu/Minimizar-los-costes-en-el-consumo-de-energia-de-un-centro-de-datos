# Creación de la red Deep Q-Learning
# Creación del Entorno

# Importar librerías
import numpy as np

# Construir el entorno en una clase
class Environment(object):
    # Introducir e inicializar los parametros y variables del entorno
    def __init__(self,optimal_temperature=(18.9,24.0),initial_month = 0,initial_number_users = 10, initial_rate_data=60):
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
        
    # Crear un método que actualice justo después de que la ia ejecute una acción
    
    
    # Crear un método que reinicie el entorno
    
    # Crear un método que nos de en cualquier instante el estado actual, la última recompensa y el game over