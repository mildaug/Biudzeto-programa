# UZDUOTIS

# Irasas (abstraktus)

# savybė suma
# savybė komentaras
# Islaidos(Irasas)

# savybė gavejas
# Pajamos(Irasas)

# savybė siuntejas
# Biudzetas

# savybe zurnalas: sąrašas įrašų
# Biudzetas turi turėti metodus:

# ataskaitai
# balansas
# pajamų įrašo sukūrimas ir įtraukimui į žurnalą
# išlaidų įrašo sukūrimas ir įtraukimui į žurnalą
# Programos meniu ir funkcionalumą galite įgyvendinti tiek per klasę, tiek pagrindinėje programoje.



class Irasas:
    def __init__(self, suma, komentaras):
        self.suma = suma
        self.komentaras = komentaras


class Islaidos(Irasas):
    def __init__(self, suma, komentaras, gavejas):
        super().__init__(suma, komentaras)
        self.gavejas = gavejas


class Pajamos(Irasas):
    def __init__(self, suma, komentaras, siuntejas):
        super().__init__(suma, komentaras)
        self.siuntejas = siuntejas


class Biudzetas:
    zurnalas = []

    def ataskaita(self):
        for irasas in self.zurnalas:
            print(f'Ataskaita: Suma: {irasas.suma}, komentaras: {irasas.komentaras}')

    def balansas(self):
        pajamos = sum([irasas.suma for irasas in self.zurnalas if isinstance(irasas, Pajamos)])
        islaidos = sum([irasas.suma for irasas in self.zurnalas if isinstance(irasas, Islaidos)])
        return pajamos - islaidos
    
    def itraukti_irasa(self, irasas):
        self.zurnalas.append(irasas)

biudzetas = Biudzetas()

#nera klases metodai
def ivesti_pajamas(biudzetas):
    pass

def ivesti_islaidas(biudzetas):
    pass


while True:
    print('------------Biudzetas------------')
    print("\nPasirinkite veiksma:")
    print("1. Sukurti pajamų irasa")
    print("2. Sukurti islaidu irasa")
    print("3. Ataskaita")
    print(" ")
    print("0. Baigti programa")
    print(" ")
    print(" ")
    meniu = int(input('Jusu pasirinkimas'))  




    


