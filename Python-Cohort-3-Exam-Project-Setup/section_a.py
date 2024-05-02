#(a)(i)
def calculate_grade(score):
    if score >= 90:
        return "Grade is A"
    elif score >= 80:
        return "Grade is B"
    elif score >= 70:
        return "Grade is C"
    elif score >= 60:
        return "Grade is D"
    elif score >=50:
        return "Grade is E"
    else:
        return "Fail"
        
      
def main():
        score = float(input("Enter marks: "))
        if score < 0 or score > 100:
            print("Invalid marks. Must be 0-100")
        else:
            grade = calculate_grade(score)
            print(f"Grade: {grade}")
 

if __name__ == "__main__":
    main()





#(ii)
def celsius_to_fahrenheit(celsius):
    return (9/5 * celsius) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (5/9) * (fahrenheit - 32)

def main():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter your choice (1 or 2): ")
     

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C is {celsius_to_fahrenheit(celsius)}°F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit)}°C")

if __name__ == "__main__":
    main()

#(b)(i)
base = 2
height = 3
Area = 1/2 * base * height
print(Area)




#(b)(ii)
def sum_list(numbers):
    return sum(numbers)

sample = [9, 2, 3, 5, 8]
result = sum_list(sample)
print(result)
















