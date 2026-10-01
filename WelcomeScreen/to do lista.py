zadaci=[]
while True:
    print("--ODABERI ZADTAK--")
    print("(zadtak se bira upsivajuci brojeve 1-3)")
    print("1. Dodaj zadatak")
    print("2. prikazi zadatak")
    print("3. zavrsi")
    a=int(input())
    if a==1:
       zadatak=input("upisi zeljeni zadtak:")
       zadaci.append(zadatak)
       print("zadtak je dodan")

    elif a==2:
        print("prikazi zadtak")
        for i, zadatak in enumerate(zadaci,1):
            print(zadatak)

    elif a==3:
        print("bok")
        break

