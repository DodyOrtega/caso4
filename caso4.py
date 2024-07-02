import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    attempts = 0

    print("¡Bienvenido al Juego de Adivinar el Número!")
    print("He seleccionado un número entre 1 y 100. Intenta adivinarlo.")

    while True:
        user_guess = int(input("Ingresa tu suposición: "))
        attempts += 1
        if user_guess == number_to_guess:
            print(f"¡Felicidades! Adivinaste el número en {attempts} intentos.")
            break
        print("¡Demasiado bajo!" if user_guess < number_to_guess else "¡Demasiado alto! Intenta de nuevo.")

# Uso del ejemplo
guess_the_number()
