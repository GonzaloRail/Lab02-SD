import time
import random

def servidor_hora():
    """Simula un servidor que devuelve su hora actual."""
    return time.time()

def algoritmo_cristian():
    """Cliente que sincroniza su reloj usando el Algoritmo de Cristian."""
    
    # Cliente registra tiempo antes de enviar solicitud
    t0 = time.time()
    
    # Simulamos un retardo de red (ida)
    retardo_ida = random.uniform(0.01, 0.1)  # entre 10ms y 100ms
    time.sleep(retardo_ida)
    
    # El cliente pide la hora al servidor
    hora_servidor = servidor_hora()
    
    # Simulamos un retardo de red (vuelta)
    retardo_vuelta = random.uniform(0.01, 0.1)
    time.sleep(retardo_vuelta)
    
    # Cliente registra tiempo después de recibir respuesta
    t1 = time.time()
    
    # Tiempo total de ida y vuelta
    rtt = t1 - t0
    
    # Se estima el tiempo actual como:
    hora_estimada = hora_servidor + (rtt / 2)
    
    print(f"Hora local antes de sincronizar: {t0:.6f}")
    print(f"Hora recibida del servidor: {hora_servidor:.6f}")
    print(f"Hora local después de sincronizar: {hora_estimada:.6f}")

# Ejecutamos el algoritmo
algoritmo_cristian()
