print(f"---------- Menú ----------")
print(f"1. TOTAL ARTICULOS VENDIDOS: {cantidad_total}")
print(f"2. INGRESOS TOTALES: {ingresos_totales:.2f} €")
print(f"3. PROMEDIO ARTICULOS VENDIDOS POR PERSONA: {promedio_articulos:.2f}")
print(f"4. GANANCIA TOTAL: {ganancia_total:.2f} €")
print("--------------------------")
 
while True:
    print(f"---------- Menú ----------")
    print(f"1. TOTAL ARTICULOS VENDIDOS: {cantidad_total}")
    print(f"2. INGRESOS TOTALES: {ingresos_totales:.2f} €")
    print(f"3. PROMEDIO ARTICULOS VENDIDOS POR PERSONA: {promedio_articulos:.2f}")
    print(f"4. GANANCIA TOTAL: {ganancia_total:.2f} €")
    print(f"5. Salir")
    print(f"--------------------------")
 
    eleccion = input("Selecciona una opción (1-5): ")
   
    match eleccion:
        case '1':
            print(f"Has seleccionado la Opción 1. TOTAL ARTICULOS VENDIDOS: {cantidad_total}")
        case '2':
            print(f"Has seleccionado la Opción 2. INGRESOS TOTALES: {ingresos_totales:.2f} €")
        case '3':
            print(f"Has seleccionado la Opción 3. PROMEDIO ARTICULOS VENDIDOS POR PERSONA: {promedio_articulos:.2f}")
        case '4':
            print(f"Has seleccionado la Opción 4. GANANCIA TOTAL: {ganancia_total:.2f} €")
        case '5':
            print("Saliendo del programa...")
            break  # Sale del bucle y finaliza el programa
        case _:
            print("Opción no válida. Por favor, intenta de nuevo.")