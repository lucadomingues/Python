print('=' * 20)
print('TERMOS DE UMA P.A.')
print('=' * 20)
first = int(input('Primeiro termo: '))
reason = int(input('Razão: '))
tenth = first + 10 * reason
for c in range(first, tenth, reason):
    print(c, end=' - ')
print('ACABOU')