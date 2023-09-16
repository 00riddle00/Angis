import lygis2

# gali įsikelti kokią tik nori nuotrauką!
lygis2.naudokFona('feja_slibinas_selfie.jpg')

# galimi filtro nustatymai:

# šviesumas - nuo 0 iki 2.0
lygis2.brightness = 0.5

# nespalvotos nuotraukos efektas. 0 - spalvota nuotrauka, 1 - nespalvota
lygis2.greyscale = 1

# blur - nuo 0 iki 10
lygis2.blur = 0

# triukšmingumas - nuo 0 iki 4
lygis2.noise = 0

# sepia efektas: 0 - nėra, 1 - yra
lygis2.sepia = 0

# kontrastas - nuo 0 iki 4.0
lygis2.contrast = 0

# alpha - nuo 0 iki 10.0
lygis2.alpha = 1.0

# saturacija: 0 iki 10.0
lygis2.saturation = 0


lygis2.filtras()
