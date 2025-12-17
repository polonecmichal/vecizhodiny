vstup = input("zadaj mi co idem heslovat:")
kluc ="abc"
novy_kluc = kluc * (len(vstup)//len(kluc)) + kluc[:len(vstup)%len(kluc):]
print(len(novy_kluc)), len(vstup)
vystup = " "
for i in range(len(vstup)):
    znak = chr(ord(vstup[i]))
    if 97 <= ord(vstup[i]) and ord(vstup[i]) <= 122 :
        posun = ord(novy_kluc[i])-96
        ord(vstup[i]) - 97 + posun % 26 + 97
        vystup += chr((ord(vstup[i]) - 97 + posun) % 26 + 97)
    else:
        vystup += vstup[i]
print(vystup)
