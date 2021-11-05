class Varasto:
    def __init__(self, tilavuus, alku_saldo = 0):
        if tilavuus > 0.0:
            self.tilavuus = tilavuus

        else:
            # virheellinen, nollataan
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
            if alku_saldo < 5.0:
                print('tosi negatiivinen')
                if alku_saldo < 7.0:
                    print('siis ihan liian negatiivinen')
    
        elif alku_saldo <= tilavuus:
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = tilavuus

    # huom: ominaisuus voidaan myös laskea jotenkin hienolla ja mahtavalla tavalla. Ei tarvita erillistä kenttää viela_tilaa tms.
    def paljonko_mahtuu(self):
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        # liikaa lauseita samassa funktiossa

        if self.saldo == 0.0:
            print('saldo tyhjä')
        if self.saldo > 0.0:
            print('vielä tilaa')

        aku = 'ankka'
        lista = []

        [lista.append(aku) for x in range(0, 6)]

        print(lista)

        pituus = len(lista)

        print(pituus)

        beku = 'ankka'
        lista = []

        [lista.append(beku) for x in range(0, 6)]

        print(lista)

        pituus = len(lista)

        print(pituus)

        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
