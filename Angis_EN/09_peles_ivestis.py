import lygis9


def nupieskSprogima(x, y):
    sprogimas.atsirask(x, y)


def susprogdinkBlogieti(x, y):
    nupieskSprogima(x, y)
    blogietis.mirk()


sprogimas = lygis9.sprogimas
fonas = lygis9.fonas
blogietis = lygis9.sukurkBlogieti(x=20, y=400)

blogietis.pelePaspaudus(susprogdinkBlogieti)
fonas.pelePaspaudus(nupieskSprogima)
