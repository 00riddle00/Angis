import angis
import zaidimas

scena = zaidimas.Scena(plotis=800, aukstis=800)
scena.naudokFona('pav/pilis/fejos_mene.png')

veidrodis = zaidimas.Dekoracija('pav/pilis/veidrodis.png', x=0, y=510)
langas = zaidimas.Dekoracija('pav/pilis/langas.png', x=180, y=410)
lempa = zaidimas.Dekoracija('pav/pilis/lempa.png', x=300, y=510)
skrynia = zaidimas.Dekoracija('pav/pilis/skrynia.png', x=420, y=510)
herbas = zaidimas.Dekoracija('pav/pilis/herbas.png', x=430, y=630)
paveikslas = zaidimas.Dekoracija('pav/pilis/paveikslas.png', x=530, y=630)
uzuolaidos = zaidimas.Dekoracija('pav/pilis/uzuolaidos.png', x=670, y=510)


# Veidrodis
def prikabinkVeidrodi(pelesX, pelesY):
    veidrodis.prisikabinkPriePeles()


def atkabinkVeidrodi(pelesX, pelesY):
    veidrodis.atsikabinkNuoPeles()


# Langas
def prikabinkLanga(pelesX, pelesY):
    langas.prisikabinkPriePeles()


def atkabinkLanga(pelesX, pelesY):
    langas.atsikabinkNuoPeles()


# Lempa
def prikabinkLempa(pelesX, pelesY):
    lempa.prisikabinkPriePeles()


def atkabinkLempa(pelesX, pelesY):
    lempa.atsikabinkNuoPeles()


# Skrynia
def prikabinkSkrynia(pelesX, pelesY):
    skrynia.prisikabinkPriePeles()


def atkabinkSkrynia(pelesX, pelesY):
    skrynia.atsikabinkNuoPeles()


# Herbas
def prikabinkHerba(pelesX, pelesY):
    herbas.prisikabinkPriePeles()


def atkabinkHerba(pelesX, pelesY):
    herbas.atsikabinkNuoPeles()


# Paveikslas
def prikabinkPaveiksla(pelesX, pelesY):
    paveikslas.prisikabinkPriePeles()


def atkabinkPaveiksla(pelesX, pelesY):
    paveikslas.atsikabinkNuoPeles()


# Užuolaidos
def prikabinkUzuolaidas(pelesX, pelesY):
    uzuolaidos.prisikabinkPriePeles()


def atkabinkUzuolaidas(pelesX, pelesY):
    uzuolaidos.atsikabinkNuoPeles()


# Funkcijų kvietimas pelę paspaudus ir atleidus
veidrodis.pelePaspaudus(veiksmas=prikabinkVeidrodi)
veidrodis.peleAtleidus(veiksmas=atkabinkVeidrodi)

langas.pelePaspaudus(veiksmas=prikabinkLanga)
langas.peleAtleidus(veiksmas=atkabinkLanga)

lempa.pelePaspaudus(veiksmas=prikabinkLempa)
lempa.peleAtleidus(veiksmas=atkabinkLempa)

skrynia.pelePaspaudus(veiksmas=prikabinkSkrynia)
skrynia.peleAtleidus(veiksmas=atkabinkSkrynia)

herbas.pelePaspaudus(veiksmas=prikabinkHerba)
herbas.peleAtleidus(veiksmas=atkabinkHerba)

paveikslas.pelePaspaudus(veiksmas=prikabinkPaveiksla)
paveikslas.peleAtleidus(veiksmas=atkabinkPaveiksla)

uzuolaidos.pelePaspaudus(veiksmas=prikabinkUzuolaidas)
uzuolaidos.peleAtleidus(veiksmas=atkabinkUzuolaidas)
