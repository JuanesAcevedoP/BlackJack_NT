import random

def jugar_ruleta():
    # Generar un número aleatorio del 1 al 50
    numero_ganador = random.randint(1, 50)
    
    # Generar un número aleatorio del 1 al 100 para determinar el resultado
    resultado = random.randint(1, 100)
    
    # Si el resultado está dentro del 30%, el jugador gana
    if resultado <= 30:
        return numero_ganador, True
    else:
        return numero_ganador, False

def main():
    saldo_inicial = 1000  # Puedes ajustar el saldo inicial como desees
    saldo = saldo_inicial
    
    while saldo > 0:
        print(f"Tu saldo actual es: ${saldo}")
        apuesta = int(input("¿Cuánto quieres apostar? (0 para salir): "))
        
        if apuesta == 0:
            break
        
        if apuesta > saldo:
            print("No puedes apostar más de tu saldo actual.")
            continue
        
        numero_apostado = int(input("Elige un número del 1 al 50 en el que apostar: "))
        
        if numero_apostado < 1 or numero_apostado > 50:
            print("Por favor, elige un número entre 1 y 50.")
            continue
        
        saldo -= apuesta
        numero_ganador, ganador = jugar_ruleta()
        
        if ganador:
            saldo += apuesta * 2  # Si gana, el jugador recibe el doble de su apuesta
            print(f"Ganaste ${apuesta * 2}! El número ganador fue {numero_ganador}.")
        else:
            print(f"Perdiste ${apuesta}. El número ganador fue {numero_ganador}.")
    
    print("Gracias por jugar. Tu saldo final es: ${saldo}")
    
if __name__ == "__main__":
    main()
