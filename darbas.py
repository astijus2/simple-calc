"""
a = int(input("Įveskite a: "))
if a > 0:
    pass
else:
    print("a turi būti teigiamas skaičius")

b = int(input("Įveskite b: "))
if b > 0:
    pass
else:
    print("b turi būti teigiamas skaičius")

if a > 0 and b > 0:
    suma = a + b
    print ("Suma: ", suma)
"""


"""
a = int(input("Įveskite a: "))
if a > 5:
    print("√a =", math.sqrt(a))
else:
    print("a turi būti didesnis už 5")
"""

"""
amzius = int(input("Įveskite amžių: "))
pajamos = int(input("Įveskite pajamas: "))
if amzius > 18:
    if pajamos > 1500:
        print("Jums suteikiama paskola.")
    else:
        print("Jūs esate suaugęs, bet turite per mažas pajamas.")
else:
    print("Jūs esate nepilnametis.")
"""




sk = int(input("iveskite skaiciu: "))
if sk > 0:
    if sk % 2 == 0: 
        print("Dalyba is dvieju: ", sk / 2)
    else:
        print("Dalyba is triju: ", sk / 3)
else:
    print("Originalus skaicius: ", sk)
