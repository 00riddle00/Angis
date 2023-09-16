reikalingas žaidimas

scena = žaidimas.duokSceną()

scena.naudokPaveiksliuką("milzinas_gynejas.png")

atsakymas = žaidimas.paklauskTeksto("koks slaptažodis?")

jeigu atsakymas == "abcd":
    scena.naudokPaveiksliuką("sveiki_atvyke.png")
