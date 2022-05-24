#If elif
flavour = "strawberry milkshake"
if flavour == "strawberry":
    print("PASS")
elif flavour == "Milkshake":
    print("FAIL")
else:
    print("The flavour is:", flavour)

#For
for i in range(len(flavour)):
    print(flavour[i])

#While
i = 0
while i < 5:
    print("While loop:", flavour[i])
    i += 1
