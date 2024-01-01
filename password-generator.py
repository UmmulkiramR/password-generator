import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))




# manual
passwordlength = nr_letters+nr_symbols+nr_numbers
print(f"password length: {passwordlength}")

passString=""
countS=0
countN=0
countL=0

while passString.__len__()<passwordlength:
    let = ""
    num = ""
    sym = ""
    for l in range(1,2):
        if(countL<nr_letters):
            let = let + random.choice(letters)
            countL = countL +1
    for n in range(1, 2):
        if(countN < nr_numbers):
            num = num + random.choice(numbers)
            countN =+ 1
    for s in range(1, 2):
        if (countS < nr_symbols):
            sym = sym + random.choice(symbols)
            countS = countS+ 1

    passString=passString+let+num+sym
    let = ""
    num = ""
    sym = ""

    for l in range(1,3):
        if (countL < nr_letters):
            let= let + random.choice(letters)
            countL = countL +1
    for n in range(1, 3):
        if (countN < nr_numbers):
            num = num + random.choice(numbers)
            countN = countN + 1
    for s in range(1, 3):
        if (countS < nr_symbols):
            sym = sym + random.choice(symbols)
            countS = countS+ 1

    passString=passString+let+num+sym
    let = ""
    num = ""
    sym = ""

    for l in range(1,4):
        if (countL < nr_letters):
            let = let + random.choice(letters)
            countL = countL +1
    for n in range(1, 4):
        if (countN < nr_numbers):
            num = num + random.choice(numbers)
            countN = countN + 1
    for s in range(1, 4):
        if (countS < nr_symbols):
            sym = sym + random.choice(symbols)
            countS = countS+ 1

    passString=passString+let+num+sym
    let = ""
    num = ""
    sym = ""

print(f"password is :, {passString}")

#using python built in shuffle method

passwordList = []
for l in range(1, nr_letters+1):
    passwordList.append(random.choice(letters))
for n in range(1, nr_numbers+1):
    passwordList.append(random.choice(numbers))
for s in range(1, nr_symbols+1):
    passwordList.append(random.choice(symbols))

random.shuffle(passwordList)

password=""
for p in passwordList:
    password= password+p
print(f"password with built-in function: {password}")