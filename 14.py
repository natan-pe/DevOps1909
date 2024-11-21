current_name = input ("Enter your current name: ")

my_file = open('names.txt' ,'a')
my_file.write(current_name + '\n')
my_file.close()

my_file = open('names.txt', 'r')
for name in my_file.readlines():
    print(f"Hello, {name}")
my_file.close()
print("natanTest01")

