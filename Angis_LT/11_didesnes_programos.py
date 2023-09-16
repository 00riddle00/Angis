reikalingas lygis11
reikalingas žaidimas

žmogausTaškai = 0
slibinoTaškai = 0

žmogus = žaidimas.Dekoracija('pav/zmogus1.png', 1, 100)
slibinas = žaidimas.Dekoracija('pav/slibinas1.png', 400, 100)

žmogausPasirinkimas = žaidimas.paklauskTeksto("a - akmuo \n ž - žirklės \n p - popierius")

jei žmogausPasirinkimas == 'a':
    žmogus.naudokPaveiksliuką('pav/zmogus_akmuo.png')
    slibinoPasirinkimas = 'p'
    slibinas.naudokPaveiksliuką('pav/slibinas_popierius.png')
jei žmogausPasirinkimas == 'ž':
    žmogus.naudokPaveiksliuką('pav/zmogus_zirkles.png')
    slibinoPasirinkimas = 'a'
    slibinas.naudokPaveiksliuką('pav/slibinas_akmuo.png')
jei žmogausPasirinkimas == 'p':
    žmogus.naudokPaveiksliuką('pav/zmogus_popierius.png')
    slibinoPasirinkimas = 'ž'
    slibinas.naudokPaveiksliuką('pav/slibinas_zirkles.png')

slibinoTaškai = slibinoTaškai + 1
žaidimas.sakyk("Slibinas ", slibinoTaškai, ": Žmogus ", žmogausTaškai)
