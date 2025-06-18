#asks user their name
name = input("what is your name? ") .strip().title()

#Split user's name into first and last (I couldnt figure out how to get it to work if the user only put in one name; this is what copilot gave me and I have less then no understanding as to why/how it works)
parts = name.split(" ")
if len(parts) == 1:
    First = parts[0]
    last = ""
else:
    First, last = parts[0], parts[1]

#Asks what title the user wants to use
while True:
    Title = input(f"Hello {name}, what title would you like to use? (Mr/Ms/Other) ").strip().lower()
    if Title in ["mr", "ms"]:
        print("lame but moving on")
        break
    elif Title in "other":
        Title = input(f"Fuck yah {name}, what would you like to be called? ").strip().lower()
        break
    else:
        print("Please enter a valid title (Mr, Ms, or Other).")

#Asks if they want to use the calculator or something else
response = input(f"hello {Title} {First}! Would you like to use the calculator? (yes/no) ").strip().lower()
if "yes" in response or "y" in response:
    print(f"Im glad to hear that")
if "no" in response or "n" in response:
    print(f'Well shit {Title} thats really the only thing I can code right now, maybe in a year or two this bitch will play tic tac toe or something equally as trivial but I wouldnt hold my breath waiting on such lofty achievements')

#starts the calculator function
## 'Int" vs "Float" int or integer isa  whole number with out any decimal but float values allow for decimal points

#Additive calc function
x = float(input("What's X? "))
y = float(input("What's Y? "))
z = round(x + y)
print (f"{z:,}")

#Subtractive calc function
x = float(input("What's X? "))
y = float(input("What's Y? "))
z = round(x - y)
print (f"{z:,}")

#Multiplicative calc function
x = float(input("What's X? "))
y = float(input("What's Y? "))
z = round(x  y)
print (f"{z:,}")

#Divisional calc function
x = float(input("What's X? "))
y = float(input("What's Y? "))
z = round(x / y)
print (f"{z:.2f}")