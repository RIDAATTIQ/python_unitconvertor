def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print("Welcome to Unit Converter! 💫")
print("1. Kilometers to Miles")
print("2. Celsius to Fahrenheit")

choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    km = float(input("Enter distance in kilometers: "))
    miles = km_to_miles(km)
    print(f"{km} km is equal to {miles} miles")

elif choice == '2':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")

else:
    print("Invalid choice! Please select 1 or 2.")
