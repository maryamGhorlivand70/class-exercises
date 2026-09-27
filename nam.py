
names = []
while True:
    name = input("Enter a name(Enter exit to quite): ")
    if name == "exit":
        break
    names.append(name)
vowels = "aeiouAEIOU"
names.sort(key= lambda name:
    sum(letter in vowels for letter in name)

for name in names:
    print(name)


