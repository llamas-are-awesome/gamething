#!/user/bin/env python3

import csv
import pprint

ch_stat = {}
stat= input("Which stat? HP, Attack, Defense, SP Atk, SP Def, or Speed?: ")
with open("pokedex.txt", "r") as dexfile:


        if stat.lower() == "hp":
            try:
                for line in dexfile:
                    (key, value) = line.split(",")[1],int(line.split(",")[5])
                    ch_stat[key] = value
            except ValueError:
                pass
        #print(ch_stat)
            #print(line.split(",")[1],line.split(",")[5])
        elif stat.lower() == "attack":
            for line in dexfile:
                (key, value) = line.split(",")[1],line.split(",")[6]
                ch_stat[key] = value
        #print(ch_stat)

        elif stat.lower() == "defense":
            for line in dexfile:
                (key, value) = line.split(",")[1],line.split(",")[7]
                ch_stat[key] = value
        #print(ch_stat)

        elif stat.lower() == "sp attack" or "sp atk":
            for line in dexfile:
                (key, value) = line.split(",")[1],line.split(",")[8]
                ch_stat[key] = value
        #print(ch_stat)

        elif stat.lower() == "sp def" or "sp defense":
            for line in dexfile:
                (key, value) = line.split(",")[1],line.split(",")[9]
                ch_stat[key] = value
        #print(ch_stat)

        elif stat.lower() == "speed":
            for line in dexfile:
                (key, value) = line.split(",")[1],line.split(",")[10]
                ch_stat[key] = value
        #print(ch_stats)

        else:
            print("learn to read")


sorted_stat = (sorted( ((v,k) for k,v in ch_stat.items())))
pprint.pprint(sorted_stat)

with open("sorteddex.txt", "w") as text_file:
    pprint.pprint(sorted_stat)
