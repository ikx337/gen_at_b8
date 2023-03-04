def conv(a, base):
    result = []
    if(a == 0):
        result.append(0)
    else:
        # Calcul of pounds
        nbOfDigits = 0
        pounds = []
        while(a >= base**nbOfDigits):
            pounds.append(base**nbOfDigits)
            nbOfDigits += 1
        pounds.reverse()

        # Conversion
        for i in range(len(pounds)):
            result.append(divmod(a, pounds[i])[0])
            a = divmod(a, pounds[i])[1]
    return(result)

base = 8
print("\n")
print("Table of addition to base 8 for carry = 0 is :")
for a in range(base):
    ligne = []
    for b in range(base):
        ligne.append(conv(a+b, base))
    print(ligne)
print("\n")
print("Table of addition to base 8 for carry = 1 is :")
for a in range(base):
    ligne = []
    for b in range(base):
        ligne.append(conv(a+b+1, base))
    print(ligne)