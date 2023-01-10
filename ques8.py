#Program to convert Celsius to Fahrenheit

celsius = float(input("Enter the temperature in Celsius: "))
fah = celsius*(9/5) + 32
print(celsius, "C =", round(fah,2), "F")