
"""
EcoTracker - Monitor de Consumo Energético Digital
Trabajo Final - Algoritmos y Estructuras de Datos
Principios de Green Software aplicados

Autores: [Nombres del grupo]
Fecha: Julio 2025
"""

# Constantes globales
import json
from pathlib import Path


ARCHIVO_ACTIVIDADES = "actividades.txt"
ARCHIVO_METAS = "metas.txt"
ARCHIVO_DISPOSITIVOS = "dispositivos.txt"
FACTOR_CO2_KWH = 0.4  # kg CO2 por kWh (promedio mundial)

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*50)
    print("🌱 EcoTracker - Monitor de Consumo Energético")
    print("="*50)
    print("1. Registrar actividad")
    print("2. Ver dispositivos disponibles")
    print("3. Reporte diario")
    print("4. Reporte semanal")
    print("5. Establecer metas")
    print("6. Ver recomendaciones")
    print("7. Estadísticas generales")
    print("8. Salir")
    print("-"*50)

def inicializar_app():
    print("hola")

def obtener_ruta_dispositivos():
    # Obtiene la ruta del directorio donde está este script
    directorio_actual = Path(__file__).parent
    # Construye la ruta completa al archivo dispositivos.txt
    return directorio_actual / "dispositivos.txt"
        
def mostrar_dispositivos():
    """Muestra la lista de dispositivos disponibles"""
    print("\n📱 Dispositivos disponibles:")
    print("-"*71)
    
    ruta = obtener_ruta_dispositivos()
    with open(ruta, 'r', encoding='utf-8') as f:
        dispositivos = json.load(f)
    
    print(f"{'Código':12} | {'Nombre':18} | {'Consumo Watts (W)':<15} | {'Categoria':<15}")
    print("-" * 71)  # Línea separadora
    for codigo, info in dispositivos.items():
        print(f"{codigo:12} | {info['nombre']:18} | {info['consumo_watts']:<15}   | {info['categoria']}")
    
    print("-"*71)
def registrar_actividad(dispositivo: str, tiempo_minutos: int):
    """
    Calculamos el consumo
    Obtenemos la fecha actual
    Definimos el formato de la actividad
    Guardamos la actividad en el archivo de actividad
    
    Mostramos mensajes    
    """
    print("Funcion registrar actividad")
                  
def main():
    """Función principal del programa"""
    print("🌱 Iniciando EcoTracker...")
    print("💚 Promoviendo el Green Software desde 2025")
    
    inicializar_app()
    # AGREGAR UNA WHILE
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción (1-8): "))
        print(opcion)
        
        match opcion:
            case 1: 
                mostrar_dispositivos()
                codigo = input("\nIngrese nombre del dispositivo: ").strip().lower()
                ruta = obtener_ruta_dispositivos()
                # Leer el archivo y cargar el contenido JSON
                with open(ruta, 'r', encoding='utf-8') as f:
                    dispositivos = json.load(f)
                    
                # Buscar el dispositivo por código
                if codigo in dispositivos:
                    tiempo = int(input("Ingrese tiempo de uso (minutos): "))
                    if tiempo > 0:
                        registrar_actividad(codigo, tiempo)
                    else:
                        print("❌ El tiempo debe ser positivo")
                else:
                    print("❌ Dispositivo no encontrado")
            case 2: 
                mostrar_dispositivos()
            case 3: 
                print(3)
            case 4: 
                print(4)
            case 5: 
                print(5)
            case 6: 
                print(6)
            case 7: 
                print(7)
            case 8:
                print("\n\n🌱 Saliendo de EcoTracker...") 
                break
            case _:
                print("❌ Opción inválida. Seleccione 1-8")
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()