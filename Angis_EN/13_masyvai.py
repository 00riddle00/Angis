import lygis13

feja = lygis13.feja

burtuLentyna = [
    lygis13.expectoPatronum,
    lygis13.lumos,
    lygis13.accio,
    lygis13.alohomora,
    lygis13.obliviate,
    lygis13.aberto,
    lygis13.expelliarmus,
    lygis13.impedimenta
]

burtoNumeris = feja.paklauskSkaiciaus('kelintą burtą išbandom? Įvesk jo numerį 0-7')

burtas = burtuLentyna[burtoNumeris]

burtas.vykdyk()
