
"""
EcoTracker - Monitor de Consumo Energético Digital
Trabajo Final - Algoritmos y Estructuras de Datos
Principios de Green Software aplicados

Autores: [Nombres del grupo]
Fecha: Julio 2025
"""

# Constantes globales
import datetime
import json
from pathlib import Path
from typing import Dict, Tuple


RUTA_ACTIVIDADES = "actividades.txt"
RUTA_METAS = "metas.txt"
RUTA_DISPOSITIVOS = "dispositivos.txt"
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

def calcular_consumo(codigo: str, tiempo_minutos: int) -> Tuple[float, float]:
    """Calcula el consumo energético y emisiones CO2"""
    ruta = obtener_ruta_dispositivos()
    with open(ruta, 'r', encoding='utf-8') as f:
        dispositivos = json.load(f)
    if codigo not in dispositivos:
        raise ValueError(f"Dispositivo '{codigo}' no encontrado")
    
    consumo_watts = dispositivos[codigo]["consumo_watts"]
    
    # Convertir a kWh
    consumo_kwh = (consumo_watts * tiempo_minutos) / (1000 * 60)
    
    # Calcular CO2 equivalente
    co2_kg = consumo_kwh * FACTOR_CO2_KWH
    
    return consumo_kwh, co2_kg

def registrar_actividad(dispositivo: str, tiempo_minutos: int):
    """
    Calculamos el consumo
    Obtenemos la fecha actual
    Definimos el formato de la actividad
    Guardamos la actividad en el archivo de actividad
    
    Mostramos mensajes    
    """
    consumo_kwh, co2_kg = calcular_consumo(dispositivo, tiempo_minutos)
        
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Funcion registrar actividad")

def cargar_dispositivos() -> Dict[str, Dict]:
    """Carga la base de datos de dispositivos desde archivo existente"""
    try:
        with open(RUTA_DISPOSITIVOS, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.strip():
                return json.loads(content)
            else:
                print(f"❌ El archivo {RUTA_DISPOSITIVOS} está vacío")
                return {}
    except FileNotFoundError:
        print(f"❌ Archivo {RUTA_DISPOSITIVOS} no encontrado")
        return {}
    except json.JSONDecodeError as e:
        print(f"❌ Error al leer JSON en {RUTA_DISPOSITIVOS}: {e}")
        return {}
    except Exception as e:
        print(f"❌ Error al cargar dispositivos: {e}")
        return {}
                      
def main():
    """Función principal del programa"""
    print("🌱 Iniciando EcoTracker...")
    print("💚 Promoviendo el Green Software desde 2025")
    
    # Cargar datos iniciales
    dispositivos = cargar_dispositivos()
    actividades = cargar_actividades()
    metas = cargar_metas()
    
    inicializar_app()
    # AGREGAR UNA WHILE
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción (1-8): "))
        print(opcion)
        
        match opcion:
            case 1: 
                mostrar_dispositivos()
                codigo = input("\nIngrese codigo del dispositivo: ").strip().lower()
                ruta = obtener_ruta_dispositivos()
                # Leer el archivo y cargar el contenido JSON
                with open(ruta, 'r', encoding='utf-8') as f:
                    dispositivos = json.load(f)
                    
                # Buscar el dispositivo por código
                if codigo in dispositivos:
                    try:
                        tiempo = int(input("Ingrese tiempo de uso (minutos): "))
                        if tiempo > 0:
                            registrar_actividad(codigo, tiempo)
                        else:
                            print("❌ El tiempo debe ser positivo")
                    except ValueError:
                        print("❌ Tiempo inválido")
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