from pokemon import Pokemon, IV, EV

print("Pokemon Battle Simulator")

#create pokémon
ivs = IV(31,31,31,31,31,31)
evs = EV(0,252,252,0,6,0)
poke = Pokemon(0, 100, ivs, evs)
print(poke.stat)