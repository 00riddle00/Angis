reikalinga angis
reikalingas žaidimas

scena = žaidimas.Scena(plotis=800, aukštis=800)
scena.naudokFoną('pav/pilis/fejos_mene.png')

veidrodis  = žaidimas.Dekoracija('pav/pilis/veidrodis.png',     x=0,  y=510)
langas     = žaidimas.Dekoracija('pav/pilis/langas.png',      x=180,  y=410)
lempa      = žaidimas.Dekoracija('pav/pilis/lempa.png',       x=300,  y=510)
skrynia    = žaidimas.Dekoracija('pav/pilis/skrynia.png',     x=420,  y=510)
herbas     = žaidimas.Dekoracija('pav/pilis/herbas.png',      x=430,  y=630)
paveikslas = žaidimas.Dekoracija('pav/pilis/paveikslas.png',  x=530,  y=630)
užuolaidos = žaidimas.Dekoracija('pav/pilis/uzuolaidos.png',  x=670,  y=510)


# Veidrodis
def prikabinkVeidrodį(pelėsX, pelėsY):
    veidrodis.prisikabinkPriePelės()


def atkabinkVeidrodį(pelėsX, pelėsY):
    veidrodis.atsikabinkNuoPelės()


# Langas
def prikabinkLangą(pelėsX, pelėsY):
    langas.prisikabinkPriePelės()


def atkabinkLangą(pelėsX, pelėsY):
    langas.atsikabinkNuoPelės()


# Lempa
def prikabinkLempą(pelėsX, pelėsY):
    lempa.prisikabinkPriePelės()


def atkabinkLempą(pelėsX, pelėsY):
    lempa.atsikabinkNuoPelės()


# Skrynia
def prikabinkSkrynią(pelėsX, pelėsY):
    skrynia.prisikabinkPriePelės()


def atkabinkSkrynią(pelėsX, pelėsY):
    skrynia.atsikabinkNuoPelės()


# Herbas
def prikabinkHerbą(pelėsX, pelėsY):
    herbas.prisikabinkPriePelės()


def atkabinkHerbą(pelėsX, pelėsY):
    herbas.atsikabinkNuoPelės()


# Paveikslas
def prikabinkPaveikslą(pelėsX, pelėsY):
    paveikslas.prisikabinkPriePelės()


def atkabinkPaveikslą(pelėsX, pelėsY):
    paveikslas.atsikabinkNuoPelės()


# Užuolaidos
def prikabinkUžuolaidas(pelėsX, pelėsY):
    užuolaidos.prisikabinkPriePelės()


def atkabinkUžuolaidas(pelėsX, pelėsY):
    užuolaidos.atsikabinkNuoPelės()


# Funkcijų kvietimas pelę paspaudus ir atleidus
veidrodis.pelęPaspaudus(veiksmas = prikabinkVeidrodį)
veidrodis.pelęAtleidus(veiksmas = atkabinkVeidrodį)

langas.pelęPaspaudus(veiksmas = prikabinkLangą)
langas.pelęAtleidus(veiksmas = atkabinkLangą)

lempa.pelęPaspaudus(veiksmas = prikabinkLempą)
lempa.pelęAtleidus(veiksmas = atkabinkLempą)

skrynia.pelęPaspaudus(veiksmas = prikabinkSkrynią)
skrynia.pelęAtleidus(veiksmas = atkabinkSkrynią)

herbas.pelęPaspaudus(veiksmas = prikabinkHerbą)
herbas.pelęAtleidus(veiksmas = atkabinkHerbą)

paveikslas.pelęPaspaudus(veiksmas = prikabinkPaveikslą)
paveikslas.pelęAtleidus(veiksmas = atkabinkPaveikslą)

užuolaidos.pelęPaspaudus(veiksmas = prikabinkUžuolaidas)
užuolaidos.pelęAtleidus(veiksmas = atkabinkUžuolaidas)
