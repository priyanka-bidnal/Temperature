temperature = float(input("Enter the temperature in °C: "))

if temperature < 20:
    print(f"Temperature: {temperature}°C")
    print("Status: Cold")
elif 20 <= temperature <= 30:
    print(f"Temperature: {temperature}°C")
    print("Status: Normal")
else:
    print(f"Temperature: {temperature}°C")


    print("Status: Hot")