#!/user/bin/env python3

import csv
import pprint

ch_stat = {}
stat= input("Which stat? HP, Attack, Defense, SP Atk, SP Def, or Speed?: ")

with open("pokedex.txt", "r") as dexfile:

        pokedata= csv.DictReader(dexfile)

        for line in pokedata:
            try:

                newdict= {line["Name"]: line[stat]}

                ch_stat.update(newdict)
            except:
                pass

    
sorted_stat = (sorted( ((v,k) for k,v in ch_stat.items())))
pprint.pprint(sorted_stat)

with open("sorteddex.txt", "w") as text_file:
    pprint.pprint(sorted_stat, text_file)
