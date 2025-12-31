temperature = int(input("Enter the temperature in °C: "))

if temperature >= 25:
    print("Wear light and soft clothes like a T-shirt or cotton shirt.")
elif temperature >= 15:
    print("Wear a light sweater or full-sleeve shirt.")
elif temperature >= 5:
    print("Wear a pullover.")
else:
    print("Wear a jacket or heavy winter clothes.")
