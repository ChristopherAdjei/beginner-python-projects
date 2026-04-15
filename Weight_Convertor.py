Weight = float(input("Enter your weight: "))
unit = input("Specify if in Lbs or Kg (L/K): ").upper()

if unit == "K":
    Weight = Weight * 2.21
    print(f"You are {Weight} pounds")
else:
    Weight = Weight * 0.45
    print(F"You are {Weight} kilos")