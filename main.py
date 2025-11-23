"""
Sistema Biométrico de Detección de Fraude
Verifica identidad mediante firma digital
"""

from graphics import Canvas

ANCHO = 600
ALTO = 400
COLOR_FIRMA = "#00ff88"

# Variables globales para almacenar datos
firma_registrada = []
cedula_registrada = ""
nombre_registrado = ""

def main():
    print("=== SISTEMA BIOMÉTRICO DE DETECCIÓN DE FRAUDE ===")
    print()
    
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar identidad")
        print("2. Verificar identidad")
        print("3. Salir")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            verificar_usuario()
        elif opcion == "3":
            print("\n¡Gracias por usar el sistema!")
            break
        else:
            print("⚠️ Opción inválida")

def registrar_usuario():
    global firma_registrada, cedula_registrada, nombre_registrado
    
    print("\n--- REGISTRO DE IDENTIDAD ---")
    
    # Solicitar datos
    nombre = input("Nombre completo: ")
    cedula = input("Cédula (10 dígitos): ")
    
    # Validar cédula
    if len(cedula) != 10 or not cedula.isdigit():
        print("🚨 ALERTA DE FRAUDE: Cédula inválida")
        return
    
    # Capturar firma
    print("\nDibuja tu firma en el canvas (haz clic y arrastra)")
    canvas = Canvas(ANCHO, ALTO)
    canvas.set_canvas_title("Dibuja tu firma - Presiona Enter cuando termines")
    canvas.set_canvas_background_color("#1a0a2e")
    
    # Título
    titulo = canvas.create_text(ANCHO//2, 30, "REGISTRO - Dibuja tu firma")
    canvas.set_color(titulo, "#00ffff")
    
    firma = []
    
    def capturar_firma(event):
        if firma:
            ultimo = firma[-1]
            linea = canvas.create_line(ultimo[0], ultimo[1], event.x, event.y, COLOR_FIRMA)
        firma.append((event.x, event.y))
    
    canvas.on_mouse_drag(capturar_firma)
    
    input("\nPresiona Enter cuando termines de dibujar...")
    
    # Validar firma
    if len(firma) < 15:
        print("⚠️ Firma muy simple - posible fraude")
        return
    
    # Guardar datos
    firma_registrada = list(firma)
    cedula_registrada = cedula
    nombre_registrado = nombre
    
    print(f"\n✅ Usuario {nombre} registrado exitosamente")
    print(f"   Puntos de firma capturados: {len(firma)}")

def verificar_usuario():
    print("\n--- VERIFICACIÓN DE IDENTIDAD ---")
    
    if not firma_registrada:
        print("❌ ERROR: No hay usuarios registrados")
        return
    
    # Solicitar cédula
    cedula = input("Ingresa tu cédula: ")
    
    # Verificar cédula
    if cedula != cedula_registrada:
        print("\n🚨 ALERTA DE FRAUDE 🚨")
        print("❌ CÉDULA NO COINCIDE - POSIBLE SUPLANTACIÓN")
        return
    
    # Capturar firma para verificar
    print("\nDibuja tu firma en el canvas para verificar")
    canvas = Canvas(ANCHO, ALTO)
    canvas.set_canvas_title("Dibuja tu firma - Presiona Enter cuando termines")
    canvas.set_canvas_background_color("#1a0a2e")
    
    titulo = canvas.create_text(ANCHO//2, 30, "VERIFICACIÓN - Dibuja tu firma")
    canvas.set_color(titulo, "#ff00ff")
    
    firma_actual = []
    
    def capturar_firma(event):
        if firma_actual:
            ultimo = firma_actual[-1]
            linea = canvas.create_line(ultimo[0], ultimo[1], event.x, event.y, "#ff00ff")
        firma_actual.append((event.x, event.y))
    
    canvas.on_mouse_drag(capturar_firma)
    
    input("\nPresiona Enter cuando termines de dibujar...")
    
    # Calcular similitud
    similitud = calcular_similitud(firma_registrada, firma_actual)
    
    print(f"\nAnalizando biometría...")
    print(f"Similitud: {similitud}%")
    
    if similitud > 35:
        print("\n✅ VERIFICACIÓN EXITOSA")
        print(f"   Identidad confirmada")
        print(f"   Bienvenido {nombre_registrado}")
    else:
        print("\n🚨 ALERTA DE FRAUDE 🚨")
        print("❌ FIRMA FALSIFICADA DETECTADA")
        print("   Acceso denegado")

def calcular_similitud(firma1, firma2):
    if not firma1 or not firma2:
        return 0
    
    # Diferencia en número de puntos
    diff_puntos = abs(len(firma1) - len(firma2)) / max(len(firma1), len(firma2))
    
    # Calcular dimensiones
    xs1 = [p[0] for p in firma1]
    ys1 = [p[1] for p in firma1]
    ancho1 = max(xs1) - min(xs1)
    alto1 = max(ys1) - min(ys1)
    
    xs2 = [p[0] for p in firma2]
    ys2 = [p[1] for p in firma2]
    ancho2 = max(xs2) - min(xs2)
    alto2 = max(ys2) - min(ys2)
    
    # Diferencias en dimensiones
    diff_ancho = abs(ancho1 - ancho2) / max(ancho1, 1)
    diff_alto = abs(alto1 - alto2) / max(alto1, 1)
    
    # Calcular similitud
    similitud = 100 - (diff_puntos * 40 + diff_ancho * 30 + diff_alto * 30)
    return max(0, round(similitud))

if __name__ == '__main__':
    main()
