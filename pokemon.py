import json

class Pokemon:
    def __init__(self, id, lvl, iv, ev):
        with open("pokemon.json", "r") as f:
            pokedb = json.load(f)
            try:
                pokemon = pokedb["pokemon"][id]
            except IndexError:
                raise IndexError("Pokémon Not Found")
            self.id = id
            self.name = pokemon['name']
            self.stat = pokemon['base']
            self.type1 = pokemon['type1']
            self.type2 = pokemon['type2']
            self.weight = pokemon['weight']
            f.close()
        if lvl > 100 or lvl < 1:
            raise ValueError("Level out of range")
        self.lvl = lvl
        # we consider we always start by pv and the IV variable is always IV class
        index = 1
        ivs = iv.getIVs()
        evs = ev.getStats()
        for currentStat in ivs:
            # https://www.pokepedia.fr/Statistique#D%C3%A9termination_des_statistiques
            if currentStat == "pv":
                self.stat[currentStat] = round(((2*self.stat[currentStat]+ivs.get(currentStat)+evs.get(currentStat)*self.lvl)/100)+lvl+10)
            index += 1
            
class IV:
    def __init__(self, pv, atk, defense, atkSpe, defSpe, speed):
        if pv < 0 or pv > 31 or atk < 0 or atk > 31 or defense < 0 or defense > 31 or atkSpe < 0 or atkSpe > 31 or defSpe < 0 or defSpe > 31 or speed < 0 or speed > 31:
            raise ValueError("IVs out of range")
        self.pv = pv
        self.atk = atk
        self.defense = defense
        self.atkSpe = atkSpe
        self.defSpe = defSpe
        self.speed = speed
    def getIVs(self):
        return {"pv": self.pv, "atk": self.atk, "def": self.defense, "atkSpe": self.atkSpe, "defSpe": self.defSpe, "speed": self.speed}

class EV:
    def __init__(self, pv, atk, defense, atkSpe, defSpe, speed):
        if pv+atk+defense+atkSpe+defSpe+speed > 510:
            raise ValueError("EVs out of limits")
        self.pv = pv
        self.atk = atk
        self.defense = defense
        self.atkSpe = atkSpe
        self.defSpe = defSpe
        self.speed = speed
    def getStats(self):
        self.pv = round(self.pv / 4)
        self.atk = round(self.atk / 4)
        self.defense = round(self.defense / 4)
        self.atkSpe = round(self.atkSpe / 4)
        self.defSpe = round(self.defSpe / 4)
        self.speed = round(self.speed / 4)
        return {"pv": self.pv, "atk": self.atk, "def": self.defense, "atkSpe": self.atkSpe, "defSpe": self.defSpe, "speed": self.speed}