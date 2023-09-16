reikalingas lygis9


komanda nupieškSprogimą(x,y):
    sprogimas.atsirask(x,y)


komanda susprogdinkBlogietį(x,y):
    nupieškSprogimą(x,y)
    blogietis.mirk()


sprogimas = lygis9.sprogimas
fonas = lygis9.fonas
blogietis = lygis9.sukurkBlogietį(x=20, y=400)

blogietis.pelęPaspaudus( susprogdinkBlogietį )
fonas.pelęPaspaudus( nupieškSprogimą )
