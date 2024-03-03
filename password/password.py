import random, string

length=int(input("Length of password :"))
random.randint(0,36)
letters=string.ascii_letters
numbers=string.digits
symbols=string.punctuation

joiner=''
lin=letters+symbols+numbers


for _ in range(length):
    joiner+=joiner.join(random.choice(lin))
print(joiner)