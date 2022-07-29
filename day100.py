# Solución Python la Paz
def dia100():
    try:
        mensaje = "Llegaste al último día"
        print(mensaje[len(mensaje)])
    except Exception as e:
        print("Error: {}".format(e))
    finally:
        print("Muchas gracias por participar")

dia100()