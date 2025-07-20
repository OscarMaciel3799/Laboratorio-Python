
"""
EcoTracker - Monitor de Consumo Energético Digital
Trabajo Final - Algoritmos y Estructuras de Datos
Principios de Green Software aplicados

Autores: [Nombres del grupo]
Fecha: Julio 2025
"""

# Constantes globales
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

def main():
    """Función principal del programa"""
    print("🌱 Iniciando EcoTracker...")
    print("💚 Promoviendo el Green Software desde 2025")
    # AGREGAR UNA WHILE
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción (1-8): "))
        print(opcion)
        
        match opcion:
            case 1: 
                print(1)
            case 2: 
                print(2)
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
                break
                
if __name__ == "__main__":
    main()