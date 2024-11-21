from tkinter.font import names

e = [1, 2, 3, 4, 5]
f = []
names = ["natan", "avi", "eli"]
if "natan" in names:
    print("natan in list")
if len(e) > 444:
    print("enough items")
if e:
    print("e is not empte")
print(type(e))
if type(e) is list:
    print("e is list")
if isinstance(e, list):
    print("e is list!")

if not f:
    print("f is empty")
