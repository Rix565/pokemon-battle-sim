from pokemon import Pokemon, IV, EV, Nature, Type

print("Pokemon Battle Simulator")

#create pokémon
ivs = IV(0,0,0,0,0,0)
evs = EV(0,0,0,0,0,0)
nature = Nature(21)
poke = Pokemon(0, 100, ivs, evs, nature)
print(poke.stat)
poison = Type(13)
print("Vulnerabilities of type "+poison.name)
string = ""
for vuln in poison.vulnerability:
  string += Type(vuln).name+", "
print(string)
print("Resistances of type "+poison.name)
string = ""
for vuln in poison.resistance:
  string += Type(vuln).name+", "
print(string)
print(poison.getEffectiveness(poke))