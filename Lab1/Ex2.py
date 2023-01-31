string = input()
nlower = 0
nupper = 0
for i in string :
    nlower += i.islower()
    nupper += i.isupper()
print(nlower)
print(nupper)
