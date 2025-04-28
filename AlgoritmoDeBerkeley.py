import random
import time
from datetime import datetime

def formato_hora_con_milisegundos(segundos):
    """Convierte un timestamp en formato HH:MM:SS.mmm"""
    dt = datetime.fromtimestamp(segundos)
    return dt.strftime('%H:%M:%S.%f')[:-3]  # corta a milisegundos

def nodos_simulados(n):
    """Genera una lista de tiempos actuales de n nodos con diferencias simuladas."""
    reloj_referencia = time.time()
    relojes = []
    for _ in range(n):
        # Cada nodo puede tener un error entre -5 y +5 segundos
        desvio = random.uniform(-5, 5)
        relojes.append(reloj_referencia + desvio)
    return relojes

def algoritmo_berkeley():
    """Implementa el algoritmo de Berkeley para sincronizar relojes."""
    
    # Paso 1: El coordinador consulta los relojes de los nodos
    nodos = nodos_simulados(5)  # 5 nodos
    print("Tiempos originales de los nodos:")
    for i, reloj in enumerate(nodos):
        print(f"Nodo {i+1}: {formato_hora_con_milisegundos(reloj)}")
    
    # El coordinador también tiene su propio reloj
    reloj_coordinador = time.time()
    print(f"Coordinador: {formato_hora_con_milisegundos(reloj_coordinador)}")
    
    # Paso 2: Calcula la diferencia entre cada reloj y el suyo
    diferencias = []
    for reloj in nodos:
        diferencias.append(reloj - reloj_coordinador)
    
    # Paso 3: Calcula el promedio de las diferencias
    promedio = sum(diferencias) / (len(diferencias) + 1)  # +1 por el coordinador mismo

    print(f"\nPromedio de diferencias: {promedio:.6f} segundos")
    
    # Paso 4: Cada nodo (y el coordinador) debe ajustar su reloj
    print("\nTiempos ajustados:")
    for i, reloj in enumerate(nodos):
        nuevo_reloj = reloj - promedio
        print(f"Nodo {i+1}: {formato_hora_con_milisegundos(nuevo_reloj)}")
    
    nuevo_reloj_coordinador = reloj_coordinador - promedio
    print(f"Coordinador: {formato_hora_con_milisegundos(nuevo_reloj_coordinador)}")

# Ejecutamos el algoritmo
algoritmo_berkeley()
