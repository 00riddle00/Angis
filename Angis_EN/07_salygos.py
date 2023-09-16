import zaidimas

scena = zaidimas.duokScena()

scena.naudokPaveiksliuka("milzinas_gynejas.png")

atsakymas = input("koks slaptažodis?")

if atsakymas == "abcd":
    scena.naudokPaveiksliuka("sveiki_atvyke.png")
