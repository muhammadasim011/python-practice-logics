def inch_into_cms(inch):
    return inch * 2.54

n = int(input("Please input the length in inches: "))
print(f"The equivalent value in centimeters is: {inch_into_cms(n)}")