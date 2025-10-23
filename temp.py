temperature = float(input("Enter the temperature in °C: "))

if temperature < 20:
    status = "Cold"
elif 20 <= temperature <= 30:
    status = "Normal"
else:
    status = "Hot"

fahrenheit = (temperature * 9/5) + 32

print(f"Temperature: {temperature}°C")
print(f"Status: {status}")
print(f"Temperature in Fahrenheit: {fahrenheit}°F")