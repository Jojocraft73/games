from random import randint
tenta = 0
juste_prix = randint(1 , 100)
running = True
while running:
    utilisateur_prix = int(input("Enter a number between 1 and 100 : " ))
    if utilisateur_prix < juste_prix:
        print("Bigger ")
        tenta += 1
    if utilisateur_prix > juste_prix:
        print("Smaller ")
        tenta += 1
    if utilisateur_prix == juste_prix:
        tenta += 1
        print(f"Good ! You win in {tenta} try  ☺ ")
        running = False