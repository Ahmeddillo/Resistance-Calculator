def calculate_parallel_resistance(resistors):
    for resistor in resistores:
        totat_resistance += 1 / resistor
    total_resistance = 1 / total_resistance
    return total_resistance

def calculate_series_resistance(resistances):
    total_resistance = sum(resistances)
    return total_resistance

def main():
    print("Electrical Circuit Calculator")

    voltage = float(input("Enter the battery voltage (V): "))
    num_resistors = int(input("How many resistor you tie? "))

    resistors = []
    i=0
    for i in range(num_resistors):
        resistor = float(input(f"{i + 1}. resistor's resistance value (Ohm): "))
        resistors.append(resistor)

    connection_type = input("Are the resistors paralell (P) or series (S) : ").upper()

    total_resistance = 0
    current = 0

    if connection_type == "P":
        total_resistance = calculate_parallel_resistance(resistors)
        current = voltage / total_resistance
    elif connection_type == "S":
        total_resistance = calculate_series_resistance(resistors)
        current = voltage / total_resistance

    print(f"Total resistance: {total_resistance:.2f} Ohm")
    print(f"Current: {current:.2f} A")


if __name__ == "__main__":
    main()
