current_name = input("what is your name? ")
while current_name != "quit":
    if current_name == "eden":
        continue
    if current_name == "ronen":
        break
    print(f" hello {current_name}")
    current_name = input("what is yor name: ")

else:
    print("Thnx for you")
