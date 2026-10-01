a=1

kontakti=[]

b=1
while a==b :
    c=int(input("odaber sto zelis pomocu brojeva od 1-do 3 \n 1 upisi kontakt \n 2.pokazi sve kontakte kontakt\n 3 kraj kontaktne liste\n"))
    if c == 1:
        kontakt=input("upisi kopntakt")
        kontakti.append(kontakt)
    elif c == 2:
        print(kontakti)

    elif c == 3:
        break





