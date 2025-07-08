import math
import sys

# Coordenadas conocidas (latitud, longitud) para algunas ciudades de Chile y Argentina
ciudades = {
    "santiago": (-33.4489, -70.6693),
    "valparaiso": (-33.0472, -71.6127),
    "concepcion": (-36.8201, -73.0444),
    "buenos aires": (-34.6037, -58.3816),
    "cordoba": (-31.4201, -64.1888),
    "mendoza": (-32.8908, -68.8272)
}

# Velocidades promedio (km/h) por medio de transporte
velocidades = {
    "auto": 90,
    "bicicleta": 15,
    "caminando": 5
}

def haversine(coord1, coord2):
    R = 6371  # radio Tierra en km
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

def convertir_millas(km):
    return km * 0.621371

def calcular_duracion(distancia_km, velocidad_kmh):
    return distancia_km / velocidad_kmh

print("✈️ Bienvenido al calculador de rutas entre Chile y Argentina\n")

while True:
    origen = input("Ingrese la Ciudad de Origen (o 's' para salir): ").strip().lower()
    if origen == 's':
        print("Saliendo del programa. 👋")
        sys.exit()

    destino = input("Ingrese la Ciudad de Destino (o 's' para salir): ").strip().lower()
    if destino == 's':
        print("Saliendo del programa. 👋")
        sys.exit()

    if origen not in ciudades or destino not in ciudades:
        print("⚠️ Ciudad no encontrada. Por favor ingrese una ciudad válida de Chile o Argentina.\n")
        continue

    print("\nSeleccione el medio de transporte:")
    print("  1. Auto")
    print("  2. Bicicleta")
    print("  3. Caminando")
    opcion = input("Ingrese el número del medio: ").strip()

    if opcion == "1":
        medio = "auto"
    elif opcion == "2":
        medio = "bicicleta"
    elif opcion == "3":
        medio = "caminando"
    else:
        print("⚠️ Opción no válida.\n")
        continue

    distancia_km = haversine(ciudades[origen], ciudades[destino])
    distancia_millas = convertir_millas(distancia_km)
    duracion_horas = calcular_duracion(distancia_km, velocidades[medio])

    print("\n🧭 Detalles del viaje:")
    print(f"• De {origen.title()} a {destino.title()} en {medio}")
    print(f"• Distancia: {distancia_km:.2f} km / {distancia_millas:.2f} millas")
    print(f"• Duración estimada: {duracion_horas:.2f} horas")
    print("• Narrativa del viaje:")
    print(f"  - Salga desde {origen.title()}, y siga la ruta más directa hacia {destino.title()}.\n")
    print("🔁 Puede realizar otra búsqueda o salir con 's'\n")