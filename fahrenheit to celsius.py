def f_into_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in f: "))

c = f_into_c(f)
print(f"{round(c, 2)}°C")