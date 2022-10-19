import pandas as pd


class Pokemon:

    def __init__(self, name, gen, type1, type2, stats):
        self.name = name
        self.gen = gen
        self.type1 = type1
        self.type2 = type2
        self.stats = stats


df = pd.read_csv('pokemon.csv', usecols=['pokedex_number', 'name', 'generation', 'type1', 'type2', 'base_total'])
df.fillna('None', inplace=True)
df['name'] = df['name'].str.lower()
df = df
print(df)

listOfPokemon = list()
for i in range(801):
    listOfPokemon.append(Pokemon(name=df.iloc[i]['name'],
                                 gen=df.iloc[i]['generation'],
                                 type1=df.iloc[i]['type1'],
                                 type2=df.iloc[i]['type2'],
                                 stats=df.iloc[i]['base_total']))

dictOfPokemon = {}
for i in range(801):
    dictOfPokemon.update({listOfPokemon[i].name: listOfPokemon[i]})

print(dictOfPokemon)
