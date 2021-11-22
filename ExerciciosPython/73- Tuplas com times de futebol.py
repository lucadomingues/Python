times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')
print('-='*15)
print(f'teams list: {times}')
print('-='*15)
print(f'The first 5 teams: {times[0:5]}')
print('-='*15)
print(f'the last 4 teams: {times[-4:]}')
print('-='*15)
print(f'Teams in order alphabetic: {sorted(times)}')
print('-='*15)
print(f'Chapecoense is in {times.index("Chapecoense")+1}ª position')