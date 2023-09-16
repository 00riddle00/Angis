reikalingas lygis13

fėja = lygis13.fėja

burtųLentyna = [
    lygis13.expectoPatronum,
    lygis13.lumos,
    lygis13.accio,
    lygis13.alohomora,
    lygis13.obliviate,
    lygis13.aberto,
    lygis13.expelliarmus,
    lygis13.impedimenta
]

burtoNumeris = fėja.paklauskSkaičiaus('kelintą burtą išbandom? Įvesk jo numerį 0-7')

burtas = burtųLentyna[ burtoNumeris ]

burtas.vykdyk()
