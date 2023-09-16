reikalinga angis
reikalingas žaidimas
reikalinga burtai
reikalinga herojai

# šitaip sukuriam veiksmo sceną (atitinkamo dydžio) ir nurodom, kokį foną naudoti:
žaidimas.duokSceną().nustatykDydį(plotis=1500, aukštis=1500)
žaidimas.naudokFoną('finalas.png')

# dabar scenoje išdėliojame pirmojo sezono herojus:
fėja = herojai.fėja
fėja.atsirask(x = 100, y = 100)
fėja.žiūrėk(laipsniai = 315)

princas = herojai.princas
princas.atsirask(x = 1300, y = 100)
princas.žiūrėk(laipsniai = 205)

slibinas = herojai.slibinas
slibinas.atsirask(x = 450, y = 1000)
slibinas.žiūrėk(laipsniai = 45)

pelkiųValdovas = herojai.pelkiųValdovas
pelkiųValdovas.atsirask(x = 1300, y = 1000)
pelkiųValdovas.žiūrėk(laipsniai = 135)


# paspaudus pelę, slibinas turi atsisukti į pelės koordinates ir eiti į tą pusę
komanda slibinasEinaLinkPelės(pelėsX, pelėsY):
    slibinas.keliaukĮ(pelėsX, pelėsY)


žaidimas.duokSceną(slibinasEinaLinkPelės)


# spaudinėjant mygtukus w-a-s-d , princas turi vaikščioti (kaip ir 12 lygyje)
komanda princasEinaPirmyn(mygtukas):
    princas.pirmyn()


komanda princasEinaAtgal(mygtukas):
    princas.atgal()


komanda princasSukasiKairėn(mygtukas):
    princas.kairėn()


komanda princasSukasiDešinėn(mygtukas):
    princas.dešinėn()


komanda princasStoja(mygtukas):
    princas.stok()


komanda princasKerta(mygtukas):
    princas.kirsk()


žaidimas.mygtukąPaspaudus('w', princasEinaPirmyn)
žaidimas.mygtukąPaspaudus('s', princasEinaAtgal)
žaidimas.mygtukąPaspaudus('a', princasSukasiKairėn)
žaidimas.mygtukąPaspaudus('d', princasSukasiDešinėn)
žaidimas.mygtukąPaspaudus(' ', princasKerta)
žaidimas.mygtukąAtleidus('<betKuris>', princasStoja)

# tai burtų masyvas, kaip 13 lygyje
burtųLentyna = [
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
komanda paspaustasSkaitmensMygtukas(mygtukas):
    # čia tokiu būdu iš tekstinio kintamojo padaromas skaitmeninis kintamasis, pvz., iš '4' paverčiama į 4
    burtoNumeris = int(mygtukas)
    # šioje vietoje fėja turi parinkti burtą pagal burto numerį
    atrinktasBurtas = burtųLentyna[ burtoNumeris ]
    fėja.burk(burtas = atrinktasBurtas, taikinys=pelkiųValdovas)


# spaudinėjant mygtukus '0' ... '7', fėja turi burti atitinkamą burtą iš masyvo (kaip ir 13 lygyje)
komanda paspaustasSkaitmensMygtukas(mygtukas):
    # čia tokiu būdu iš tekstinio kintamojo padaromas skaitmeninis kintamasis, pvz., iš '4' paverčiama į 4
    burtoNumeris = int(mygtukas)
    # šioje vietoje fėja turi parinkti burtą pagal burto numerį
    atrinktasBurtas = burtųLentyna[ burtoNumeris ]
    fėja.burk(burtas = atrinktasBurtas, taikinys=pelkiųValdovas)


žaidimas.mygtukąPaspaudus('0', paspaustasSkaitmensMygtukas)
žaidimas.mygtukąPaspaudus('1', paspaustasSkaitmensMygtukas)
žaidimas.mygtukąPaspaudus('2', paspaustasSkaitmensMygtukas)
žaidimas.mygtukąPaspaudus('3', paspaustasSkaitmensMygtukas)
žaidimas.mygtukąPaspaudus('4', paspaustasSkaitmensMygtukas)
žaidimas.mygtukąPaspaudus('5', paspaustasSkaitmensMygtukas)
žaidimas.mygtukąPaspaudus('6', paspaustasSkaitmensMygtukas)
žaidimas.mygtukąPaspaudus('7', paspaustasSkaitmensMygtukas)

žaidimas.pelęPaspaudus( slibinasEinaLinkPelės )

fėjosGyvybė   = 10
slibinoGyvybė = 10
princoGyvybė  = 10
pelkiųValdovoGyvybė = 270

# šis daiktas rodys žaidimo rezultatą
švieslentė = žaidimas.Tekstas(x= 0, y=1400, spalva=0xFFFFFF, dydis=50)

# ši komanda nurodo pelkių valdovui puldinėti artimiausią veikėją
pelkiųValdovas.pulk()

# pagrindinis žaidimo ciklas
žaidimasBaigtas = 'ne'

kol žaidimasBaigtas == 'ne':

    jei pelkiųValdovas.arSužeidė(fėja):
        fėjosGyvybė = fėjosGyvybė - 3

    jei pelkiųValdovas.arSužeidė(slibinas):
        slibinoGyvybė = slibinoGyvybė - 3

    jei pelkiųValdovas.arSužeidė(princas):
        princoGyvybė = princoGyvybė - 1

    jei princas.arSužeidė(pelkiųValdovas):
        pelkiųValdovoGyvybė = pelkiųValdovoGyvybė - 10

    jei fėja.arSužeidė(pelkiųValdovas):
        pelkiųValdovoGyvybė = pelkiųValdovoGyvybė - 30

    jei fėjosGyvybė < 0:
        fėja.mirk()
        žaidimasBaigtas = 'taip'

    jei slibinoGyvybė < 0:
        slibinas.mirk()
        žaidimasBaigtas = 'taip'

    jei princoGyvybė < 0:
        princas.mirk()
        žaidimasBaigtas = 'taip'

    jei pelkiųValdovoGyvybė < 0:
        pelkiųValdovas.mirk()
        žaidimasBaigtas = 'taip'

    švieslentė.rodykTekstą("s:", slibinoGyvybė, " p:", princoGyvybė, " f:", fėjosGyvybė, " PV:", pelkiųValdovoGyvybė)


# žaidimo pabaigos užrašai
angis.taikykFiltrą(contrast = 1.5, sepia =1, vintage = 1)

žaidimas.Tekstas("žaidimas baigtas!", x=300, y=350, spalva=0xFFFFFF, dydis=100)

jei pelkiųValdovoGyvybė > 0:
    žaidimas.Tekstas("Pelkių Valdovas laimėjo :(", x=200, y=550, spalva=0xFFFFFF, dydis=110)

jei pelkiųValdovoGyvybė <= 0:
    žaidimas.Tekstas("PERGALĖ", x=200, y=550, spalva=0xFFFFFF, dydis=110)
