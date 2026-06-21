print("-" * 28)
print("        BMI REPORT")
print("-" * 28)

try:
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))

    if weight <= 0 or height <= 0:
        print("Weight and Height must be greater than 0.")

    else:
        bmi = weight / (height * height)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        
        print("\nYour Results:")
        print("-" * 28)
        print("Your BMI is:", round(bmi,2))
        print("You fall under (Category):", category)
        
except ValueError:
    print("Please enter numbers only.")
    
    
