import time
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
start_time = time.time()
# Definir las variables de entrada
temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')

# Definir la variable de salida
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

# Definir las funciones de pertenencia para temperatura
temperature['cold'] = fuzz.trimf(temperature.universe, [0, 0, 10])
temperature['warm'] = fuzz.trimf(temperature.universe, [5, 20, 30])
temperature['hot'] = fuzz.trimf(temperature.universe, [25, 40, 40])

# Definir las funciones para humedad
humidity['low'] = fuzz.trimf(humidity.universe, [0, 0, 20])
humidity['medium'] = fuzz.trimf(humidity.universe, [10, 50, 90])
humidity['high'] = fuzz.trimf(humidity.universe, [70, 100, 100])

# Definir las funciones para velocidad del ventilador
fan_speed['slow'] = fuzz.trimf(fan_speed.universe, [0, 0, 30])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [20, 50, 80])
fan_speed['fast'] = fuzz.trimf(fan_speed.universe, [60, 100, 100])

# Definir las reglas difusas
rule1 = ctrl.Rule(temperature['cold'] & humidity['low'], fan_speed['slow'])
rule2 = ctrl.Rule(temperature['warm'] & humidity['medium'], fan_speed['medium'])
rule3 = ctrl.Rule(temperature['hot'] & humidity['high'], fan_speed['fast'])

# Crear el sistema de control
fan_control = ctrl.ControlSystem([rule1, rule2, rule3])
fan_simulation = ctrl.ControlSystemSimulation(fan_control)

# Establecer valores de entrada y calcular la salida
fan_simulation.input['temperature'] = 15
fan_simulation.input['humidity'] = 40


# Mostrar el resultado

fan_simulation.compute()
end_time = time.time()
print(f"Hora inicial del proceso de ejecución: {start_time}")
print(f"Velocidad del ventilador: {fan_simulation.output['fan_speed']}")
print(f"Hora final del proceso de ejecución: {end_time}")
print(f"Duración: {(end_time - start_time )* 1000 } milisegundos")