

new_names = input("Youer name:")

my_file = open("names.txt", "a")
my_file.write(new_names + "\n")
my_file.close()

my_file = open("names.txt", "r")
for name in my_file.readlines():
    print(f"Hi {name}")
    my_file.close()

