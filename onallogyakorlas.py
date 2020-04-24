marka = "addidas"
ara = 3000
tipus = "nadrág"
print("A ma nap akciós az {} márkájú {} ami {} Ft.".format(marka,tipus,ara))
print("A ma nap akciós az {0} márkájú {1} ami {2} Ft.".format(marka,tipus,ara))
print("A ma nap akciós az {0} márkájú {1} ami %d Ft.".format(marka,tipus)%ara)
print("A ma nap akciós az %s márkájú %s ami %d Ft."%(marka,tipus,ara))
print("A ma nap akciós az %s márkájú %s ami "%(marka,tipus) + str(ara) +" Ft.")
print(f"A ma nap akciós az {marka} márkájú {tipus} ami {ara} Ft.")

szöveg = "feketebikapatakopogapatikapepitafeketekövén"

#irjuk ki azt hogy fekete bikapata
print(szöveg[:14:])
print(szöveg[:14-43])
print(szöveg[-1:])
print(szöveg[:1])
print(szöveg[::-1])
print(szöveg[13::-1])


if 'fekete' in szöveg:
    print("A szöveg tartalmazza a fekete szót!")
else:
    print("A szöveg nem tartalmazza a fekete szót")







