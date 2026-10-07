tt=float(input("vnesi svojo tezo (kg)"))
visina=float(input("vnesi svojo visino (m)"))
visina= visina**2
itm=(tt/visina)
print(f"tvoj indeks telesne mase je {itm:.2f}")

if itm<18.5:
    print(" premajhna telesna teza")
elif 18.5<itm<24.9:
    print("its okey")
elif 25.0<itm>29.9:
    print("mal rabs shujsat")
elif 30.0<itm>34.9:
    print("debel")
elif 35.0<itm>39.9:
    print("debel")
else:
    print("pretezek za zemljo")
