import lygis11
import zaidimas

zmogausTaskai = 0
slibinoTaskai = 0

zmogus = zaidimas.Dekoracija('pav/zmogus1.png', 1, 100)
slibinas = zaidimas.Dekoracija('pav/slibinas1.png', 400, 100)

zmogausPasirinkimas = zaidimas.paklauskTeksto("a - akmuo \n ž - žirklės \n p - popierius")

if zmogausPasirinkimas == 'a':
    zmogus.naudokPaveiksliuka('pav/zmogus_akmuo.png')
    slibinoPasirinkimas = 'p'
    slibinas.naudokPaveiksliuka('pav/slibinas_popierius.png')
elif zmogausPasirinkimas == 'ž':
    zmogus.naudokPaveiksliuka('pav/zmogus_zirkles.png')
    slibinoPasirinkimas = 'a'
    slibinas.naudokPaveiksliuka('pav/slibinas_akmuo.png')
elif zmogausPasirinkimas == 'p':
    zmogus.naudokPaveiksliuka('pav/zmogus_popierius.png')
    slibinoPasirinkimas = 'ž'
    slibinas.naudokPaveiksliuka('pav/slibinas_zirkles.png')

slibinoTaskai = slibinoTaskai + 1
zaidimas.sakyk("Slibinas ", slibinoTaskai, ": Žmogus ", zmogausTaskai)
