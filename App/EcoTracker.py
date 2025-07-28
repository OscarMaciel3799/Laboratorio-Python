
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
from typing import Dict, Tuple, List


RUTA_ACTIVIDADES = "../docs/actividades.txt"
RUTA_METAS = "../docs/metas.txt"
RUTA_DISPOSITIVOS = "../docs/dispositivos.txt"
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
        
def mostrar_dispositivos(dispositivos: Dict):
    """Muestra la lista de dispositivos disponibles"""
    print("\n📱 Dispositivos disponibles:")
    print("-"*71)
    if not dispositivos:
        print("No hay dispositivos disponibles")
        return
    
    print(f"{'Código':12} | {'Nombre':18} | {'Consumo Watts (W)':<15} | {'Categoria':<15}")
    print("-" * 71)  # Línea separadora
    for codigo, info in dispositivos.items():
        print(f"{codigo:12} | {info['nombre']:18} | {info['consumo_watts']:<15}   | {info['categoria']}")
    
    print("-"*71)

def calcular_consumo(dispositivos: Dict, dispositivo: str, tiempo_minutos: int) -> Tuple[float, float]:
    """Calcula el consumo energético y emisiones CO2"""
    if dispositivo not in dispositivos:
        raise ValueError(f"Dispositivo '{dispositivo}' no encontrado")
    
    consumo_watts = dispositivos[dispositivo]["consumo_watts"]
    
    # Convertir a kWh
    consumo_kwh = (consumo_watts * tiempo_minutos) / (1000 * 60)
    
    # Calcular CO2 equivalente
    co2_kg = consumo_kwh * FACTOR_CO2_KWH
    
    return consumo_kwh, co2_kg

def registrar_actividad(dispositivos: Dict, actividades: List[Dict], dispositivo: str, tiempo_minutos: int) -> bool:
    """Registra una nueva actividad de uso"""
    try:
        consumo_kwh, co2_kg = calcular_consumo(dispositivos, dispositivo, tiempo_minutos)
        
        fecha_actual = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print(fecha_actual)
        # Guardar en memoria
        actividad = {
            'fecha': fecha_actual,
            'dispositivo': dispositivo,
            'tiempo_minutos': tiempo_minutos,
            'consumo_kwh': consumo_kwh,
            'co2_kg': co2_kg
        }
        actividades.append(actividad)
        
        # Guardar en archivo
        with open(RUTA_ACTIVIDADES, 'a', encoding='utf-8') as f:
            linea = f"{fecha_actual}|{dispositivo}|{tiempo_minutos}|{consumo_kwh:.6f}|{co2_kg:.6f}\n"
            f.write(linea)
        
        print(f"✅ Actividad registrada exitosamente!")
        print(f"   Dispositivo: {dispositivos[dispositivo]['nombre']}")
        print(f"   Tiempo: {tiempo_minutos} minutos")
        print(f"   Consumo: {consumo_kwh:.3f} kWh")
        print(f"   CO2 equivalente: {co2_kg:.3f} kg")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al registrar actividad: {e}")
        return False

#_-------------------------------------------------------------
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

def cargar_actividades() -> List[Dict]:
    """Carga el historial de actividades desde archivo existente"""
    actividades = []
    
    try:
        with open(RUTA_ACTIVIDADES, 'r', encoding='utf-8') as f:
            for linea in f:
                linea = linea.strip()
                if linea and not linea.startswith('#'):
                    try:
                        # Formato: fecha|dispositivo|tiempo_minutos|consumo_kwh|co2_kg
                        partes = linea.split('|')
                        if len(partes) >= 5:
                            actividad = {
                                'fecha': partes[0],
                                'dispositivo': partes[1],
                                'tiempo_minutos': int(partes[2]),
                                'consumo_kwh': float(partes[3]),
                                'co2_kg': float(partes[4])
                            }
                            actividades.append(actividad)
                    except (ValueError, IndexError):
                        continue
    except FileNotFoundError:
        print(f"❌ Archivo {RUTA_ACTIVIDADES} no encontrado")
    except Exception as e:
        print(f"❌ Error al cargar actividades: {e}")
    
    return actividades

def cargar_metas() -> Dict:
    """Carga las metas de reducción de consumo desde archivo existente"""
    try:
        with open(RUTA_METAS, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.strip():
                return json.loads(content)
            else:
                print(f"❌ El archivo {RUTA_METAS} está vacío")
                return {}
    except FileNotFoundError:
        print(f"❌ Archivo {RUTA_METAS} no encontrado")
        return {}
    except json.JSONDecodeError as e:
        print(f"❌ Error al leer JSON en {RUTA_METAS}: {e}")
        return {}
    except Exception as e:
        print(f"❌ Error al cargar metas: {e}")
        return {}
                  
def mostrar_reporte_diario_interfaz(actividades: List[Dict], metas: Dict, dispositivos: Dict):
    """Muestra el reporte diario de consumo - Interfaz"""
    print("\n📊 Reporte Diario de Consumo")
    print("-"*40)
    
    fecha_input = input("Ingrese fecha (DD-MM-YYYY) o Enter para hoy: ").strip()
    fecha = fecha_input if fecha_input else None
    
    reporte = generar_reporte_diario(actividades, metas, fecha)
    
    print(f"\n📅 Fecha: {reporte['fecha']}")
    print(f"⏱️  Actividades registradas: {reporte['actividades']}")
    print(f"🕐 Tiempo total: {reporte['tiempo_total']} minutos")
    print(f"⚡ Consumo total: {reporte['consumo_total']:.3f} kWh")
    print(f"🌍 CO2 equivalente: {reporte['co2_total']:.3f} kg")
    print(f"🎯 Meta diaria: {reporte['meta_diaria']:.3f} kWh")
    
    if reporte['cumple_meta']:
        print("✅ ¡Meta diaria cumplida!")
    else:
        print("❌ Meta diaria no cumplida")
    
    if reporte['consumo_dispositivo']:
        print("\n📱 Consumo por dispositivo:")
        for dispositivo, datos in reporte['consumo_dispositivo'].items():
            nombre = dispositivos.get(dispositivo, {}).get('nombre', dispositivo)
            print(f"   {nombre}: {datos['consumo']:.3f} kWh ({datos['tiempo']} min)")

    

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
                mostrar_dispositivos(dispositivos)
                codigo = input("\nIngrese codigo del dispositivo: ").strip().lower()
                # Leer el archivo y cargar el contenido JSON
                with open(RUTA_DISPOSITIVOS, 'r', encoding='utf-8') as f:
                    dispositivos = json.load(f)
                    
                # Buscar el dispositivo por código
                if codigo in dispositivos:
                    try:
                        tiempo = int(input("Ingrese tiempo de uso (minutos): "))
                        if tiempo > 0:
                            registrar_actividad(dispositivos, actividades, codigo, tiempo)
                        else:
                            print("❌ El tiempo debe ser positivo")
                    except ValueError:
                        print("❌ Tiempo inválido")
                else:
                    print("❌ Dispositivo no encontrado")
            case 2: 
                mostrar_dispositivos(dispositivos)
            case 3: 
                mostrar_reporte_diario_interfaz(actividades, metas, dispositivos)
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