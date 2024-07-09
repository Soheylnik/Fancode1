# calculator
number1 = int(input("Enter number one :"))
while True:

    amlayat = input("enter: + , - , *, / ,%, **:")

    if amlayat != '+' or '-' or '*' or '/' or '**' or '%':

        number2 = int(input("enter number tow :"))
    break

    
if amlayat == '+':
    print(f"sum: {number1 + number2}")
elif amlayat == '-':
    print(f"menha: {number1 - number2}")
elif amlayat == '*':
    print(f"zarb: {number1 * number2}")
elif amlayat == '/':
    print(f"taghsim: {number1 / number2}")
elif amlayat == '**':
    print(f"tavan: {number1 ** number2}")
elif amlayat == '%':
    print(f"maghsom: {number1 % number2}")
