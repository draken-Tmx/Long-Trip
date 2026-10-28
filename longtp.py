from backend import viaje,descarga_viaje
while True:
    print("1. medir tiempo")
    print("2. descargar playlist viajera")
    print("3. salir")
    op=input("> ")
    if op == "1":
        viaje()
    elif op == "2":
        descarga_viaje()
    elif op == "3":
        break
    else:
        print("incorrecto")