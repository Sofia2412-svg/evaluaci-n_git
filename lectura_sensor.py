import random  
import time  

def leer_sensor() :  
    """Simula la lectura de un sensor I2C en un sistema embebido"""  
    valor = round(random.uniform(15.0, 35.0) , 2)  
    return valor  
if --name-- == "__main__" :  
    print("--- Sistema de monitoreo e Temperatura---")  
    for i in rage(5) :  
        temp = leer_sensor()  
        print(f"muestra [{i+1}/5 : {temp} °C")  
        time.sleep(1)  
    print("Muestreo finalizado con exito.")
