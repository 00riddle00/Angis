import angis
import zaidimas
import burtai
import herojai

# šitaip sukuriam veiksmo sceną (atitinkamo dydžio) ir nurodom, kokį foną naudoti:
zaidimas.duokScena().nustatykDydi(plotis=1500, aukštis=1500)
zaidimas.naudokFona('finalas.png')

# dabar scenoje išdėliojame pirmojo sezono herojus:
feja = herojai.feja
feja.atsirask(x=100, y=100)
feja.ziurek(laipsniai=315)

princas = herojai.princas
princas.atsirask(x=1300, y=100)
princas.ziurek(laipsniai=205)

slibinas = herojai.slibinas
slibinas.atsirask(x=450, y=1000)
slibinas.ziurek(laipsniai=45)

pelkiuValdovas = herojai.pelkiuValdovas
pelkiuValdovas.atsirask(x=1300, y=1000)
pelkiuValdovas.ziurek(laipsniai=135)


# paspaudus pelę, slibinas turi atsisukti į pelės koordinates ir eiti į tą pusę
def slibinasEinaLinkPeles(pelesX, pelesY):
    slibinas.keliaukI(pelesX, pelesY)


zaidimas.duokScena(slibinasEinaLinkPeles)


# spaudinėjant mygtukus w-a-s-d , princas turi vaikščioti (kaip ir 12 lygyje)
def princasEinaPirmyn(mygtukas):
    princas.pirmyn()


def princasEinaAtgal(mygtukas):
    princas.atgal()


def princasSukasiKairen(mygtukas):
    princas.kairen()


def princasSukasiDesinen(mygtukas):
    princas.desinen()


def princasStoja(mygtukas):
    princas.stok()


def princasKerta(mygtukas):
    princas.kirsk()


zaidimas.mygtukaPaspaudus('w', princasEinaPirmyn)
zaidimas.mygtukaPaspaudus('s', princasEinaAtgal)
zaidimas.mygtukaPaspaudus('a', princasSukasiKairen)
zaidimas.mygtukaPaspaudus('d', princasSukasiDesinen)
zaidimas.mygtukaPaspaudus(' ', princasKerta)
zaidimas.mygtukaAtleidus('<betKuris>', princasStoja)

# tai burtų masyvas, kaip 13 lygyje
burtuLentyna = [
    burtai.expectoPatronum,
    burtai.lumos,
    burtai.accio,
    burtai.alohomora,
    burtai.obliviate,
    burtai.aberto,
    burtai.expelliarmus,
    burtai.impedimenta
]


# spaudinėjant mygtukus '0' ... '7', fėja turi burti atitinkamą burtą iš masyvo (kaip ir 13 lygyje)
def paspaustasSkaitmensMygtukas(mygtukas):
    # čia tokiu būdu iš tekstinio kintamojo padaromas skaitmeninis kintamasis, pvz., iš '4' paverčiama į 4
    burtoNumeris = int(mygtukas)
    # šioje vietoje fėja turi parinkti burtą pagal burto numerį
    atrinktasBurtas = burtuLentyna[burtoNumeris]
    feja.burk(burtas=atrinktasBurtas, taikinys=pelkiuValdovas)


# spaudinėjant mygtukus '0' ... '7', fėja turi burti atitinkamą burtą iš masyvo (kaip ir 13 lygyje)
def paspaustasSkaitmensMygtukas(mygtukas):
    # čia tokiu būdu iš tekstinio kintamojo padaromas skaitmeninis kintamasis, pvz., iš '4' paverčiama į 4
    burtoNumeris = int(mygtukas)
    # šioje vietoje fėja turi parinkti burtą pagal burto numerį
    atrinktasBurtas = burtuLentyna[burtoNumeris]
    feja.burk(burtas=atrinktasBurtas, taikinys=pelkiuValdovas)


zaidimas.mygtukaPaspaudus('0', paspaustasSkaitmensMygtukas)
zaidimas.mygtukaPaspaudus('1', paspaustasSkaitmensMygtukas)
zaidimas.mygtukaPaspaudus('2', paspaustasSkaitmensMygtukas)
zaidimas.mygtukaPaspaudus('3', paspaustasSkaitmensMygtukas)
zaidimas.mygtukaPaspaudus('4', paspaustasSkaitmensMygtukas)
zaidimas.mygtukaPaspaudus('5', paspaustasSkaitmensMygtukas)
zaidimas.mygtukaPaspaudus('6', paspaustasSkaitmensMygtukas)
zaidimas.mygtukaPaspaudus('7', paspaustasSkaitmensMygtukas)

zaidimas.pelePaspaudus(slibinasEinaLinkPeles)

fejosGyvybe = 10
slibinoGyvybe = 10
princoGyvybe = 10
pelkiuValdovoGyvybe = 270

# šis daiktas rodys žaidimo rezultatą
svieslente = zaidimas.Tekstas(x=0, y=1400, spalva=0xFFFFFF, dydis=50)

# ši komanda nurodo pelkių valdovui puldinėti artimiausią veikėją
pelkiuValdovas.pulk()

# pagrindinis žaidimo ciklas
zaidimasBaigtas = 'ne'

while zaidimasBaigtas == 'ne':
    if pelkiuValdovas.arSuzeide(feja):
        fejosGyvybe = fejosGyvybe - 3

    if pelkiuValdovas.arSuzeide(slibinas):
        slibinoGyvybe = slibinoGyvybe - 3

    if pelkiuValdovas.arSuzeide(princas):
        princoGyvybe = princoGyvybe - 1

    if princas.arSuzeide(pelkiuValdovas):
        pelkiuValdovoGyvybe = pelkiuValdovoGyvybe - 10

    if feja.arSuzeide(pelkiuValdovas):
        pelkiuValdovoGyvybe = pelkiuValdovoGyvybe - 30

    if fejosGyvybe < 0:
        feja.mirk()
        zaidimasBaigtas = 'taip'

    if slibinoGyvybe < 0:
        slibinas.mirk()
        zaidimasBaigtas = 'taip'

    if princoGyvybe < 0:
        princas.mirk()
        zaidimasBaigtas = 'taip'

    if pelkiuValdovoGyvybe < 0:
        pelkiuValdovas.mirk()
        zaidimasBaigtas = 'taip'

    svieslente.rodykTeksta("s:", slibinoGyvybe, " p:", princoGyvybe, " f:", fejosGyvybe, " PV:", pelkiuValdovoGyvybe)

# žaidimo pabaigos užrašai
angis.taikykFiltra(contrast=1.5, sepia=1, vintage=1)

zaidimas.Tekstas("žaidimas baigtas!", x=300, y=350, spalva=0xFFFFFF, dydis=100)

if pelkiuValdovoGyvybe > 0:
    zaidimas.Tekstas("Pelkių Valdovas laimėjo :(", x=200, y=550, spalva=0xFFFFFF, dydis=110)
elif pelkiuValdovoGyvybe <= 0:
    zaidimas.Tekstas("PERGALĖ", x=200, y=550, spalva=0xFFFFFF, dydis=110)
