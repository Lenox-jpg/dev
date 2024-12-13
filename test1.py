import random
random = random.randint(1, 100)
zahl = str(input("Gib deinen Tipp ein: "))
versuche = 0
while random != zahl:
    versuche = versuche + 1
    if random < zahl:
        print("Zu hoch!")
    else:
        print("Zu niedrig!")
    zahl = str(input("Gib deinen Tipp ein: "))
print((f"Herzlichen Glückwunsch! Du hast die Zahl") + random + ("in") + versuche + ("Versuchen erraten."))