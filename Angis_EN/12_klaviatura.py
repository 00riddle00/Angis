import lygis12
import zaidimas

princas = lygis12.princas
princas.rodykVektoriu()


def pirmyn(mygtukas):
    princas.pirmyn()


def atgal(mygtukas):
    princas.atgal()


def kairen(mygtukas):
    princas.kairen()


def desinen(mygtukas):
    princas.desinen()


def kirsk(mygtukas):
    princas.kirsk()


def stok(mygtukas):
    princas.stok()


zaidimas.mygtukaPaspaudus('w', pirmyn)
zaidimas.mygtukaPaspaudus('s', atgal)
zaidimas.mygtukaPaspaudus('a', kairen)
zaidimas.mygtukaPaspaudus('d', desinen)
zaidimas.mygtukaPaspaudus(' ', kirsk)

zaidimas.mygtukaAtleidus('w', stok)
zaidimas.mygtukaAtleidus('s', stok)
zaidimas.mygtukaAtleidus('a', stok)
zaidimas.mygtukaAtleidus('d', stok)
