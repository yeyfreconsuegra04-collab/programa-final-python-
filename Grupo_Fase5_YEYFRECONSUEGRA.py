# =============================================================================
# CURSO: FUNDAMENTOS DE PROGRAMACIÓN (213022)
# FASE 5: EVALUACIÓN FINAL POA - PROBLEMA 1
# ESTUDIANTE: YESID
# PROGRAMA: INGENIERÍA DE SISTEMAS
# =============================================================================

def clasificar_compromiso(duracion, clics):
    """
    Módulo encargado de evaluar la clasificación de compromiso de una sesión
    basándose exclusivamente en las reglas de negocio establecidas.
    """
    # Regra 1: Clasificar como "Alto" si Duración > 180s y Clics > 8
    if duracion > 180 and clics > 8:
        return "Alto"
    
    # Regla 2: Clasificar como "Bajo" si Duración < 60s o Clics < 3
    elif duracion < 60 or clics < 3:
        return "Bajo"
    
    # Regla 3: Clasificar como "Medio" en todos los demás casos
    else:
        return "Medio"


def generar_informe_sesiones(matriz_datos):
    """
    Módulo principal que recorre la matriz de datos, invoca el cálculo
    de compromiso por cada registro e imprime el reporte final en consola.
    """
    print("=" * 55)
    print(f"{'INFORME DE COMPROMISO DE CLIENTES':^55}")
    print("=" * 55)
    print(f"{'ID Cliente':<15} | {'Duración (s)':<14} | {'Clics':<8} | {'Clasificación':<12}")
    print("-" * 55)
    
    # Recorrido estructurado de la matriz (Arreglo bidimensional)
    for fila in matriz_datos:
        id_cliente = fila[0]
        duracion = fila[1]
        clics = fila[2]
        
        # Llamado al módulo de clasificación
        clasificacion = clasificar_compromiso(duracion, clics)
        
        # Formateo de salida para el usuario final
        print(f"{id_cliente:<15} | {duracion:<14} | {clics:<8} | {clasificacion:<12}")
        
    print("=" * 55)


# Bloque Principal de Ejecución
if __name__ == "__main__":
    # Datos Iniciales: Matriz con 6 filas de datos (mínimo solicitado: 5)
    # Formato de cada fila: [ID Cliente, Duración (segundos), Eventos Clics]
    sesiones_clientes = [
        ["CLI-101", 240, 12],  # Esperado: Alto (>180 y >8)
        ["CLI-102", 45,  5],   # Esperado: Bajo (<60)
        ["CLI-103", 120, 2],   # Esperado: Bajo (<3)
        ["CLI-104", 150, 6],   # Esperado: Medio (Casos restantes)
        ["CLI-105", 300, 15],  # Esperado: Alto (>180 y >8)
        ["CLI-106", 60,  3]    # Esperado: Medio (Límite exacto)
    ]
    
    # Ejecución del programa
    generar_informe_sesiones(sesiones_clientes)