# Importieren von zusätzlichen Modulen
import random
import math

# Ausgabe von Text
print("Hallo, Welt! Ich bin ein Python-Programm.")

# Variablen und Datentypen
name = "John"
age = 30
print(f"{name} ist {age} Jahre alt. Alt genug, um besser zu wissen, aber jung genug, um es trotzdem zu tun.")

# Bedingungen
if age > 18:
    print("Du bist erwachsen. Zumindest theoretisch.")
else:
    print("Du bist noch ein Kind. Genieße es!")

# Schleifen
for i in range(3):
    print(f"Schleifeniteration {i+1}: Ich liebe Schleifen!")

# Listen
fruits = ["Apfel", "Banane", "Kirsche"]
print(f"Früchte im Korb: {', '.join(fruits)}. Lecker!")

# Zufallszahl
random_number = random.randint(1, 10)
print(f"Zufallszahl des Tages: {random_number}. Spiele Lotto!")

# Mathematische Funktionen
sqrt_result = math.sqrt(random_number)
print(f"Die Quadratwurzel der Zufallszahl ist: {sqrt_result:.2f}. Beeindruckend, oder?")

# Funktionen
def greet(name):
    return f"Hallo, {name}! Wie geht's?"

print(greet("Alice"))

# Ende
print("Das ist das Ende des Programms. Tschüss!")
