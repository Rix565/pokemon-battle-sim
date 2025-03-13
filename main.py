from pokemon import Pokemon, IV, EV, Nature

print("Pokemon Battle Simulator")

#create pokémon
ivs = IV(31,31,31,31,31,31)
evs = EV(0,0,0,0,0,0)
nature = Nature(1)
poke = Pokemon(0, 100, ivs, evs, nature)
print(poke.stat)