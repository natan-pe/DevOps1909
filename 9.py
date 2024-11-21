from tkinter.font import names

for i in range(1, 101):
    if i % 7 != 0 and "7" not in str(i):
        print(i)

names = ["natan", "shay", "avi", "noa"]
result = [name.upper() for name in names if "n" in name]
print(result)