def notas(*nts):
    r = dict()
    r['total'] = len(nts)
    r['maior'] = max(nts)
    r['menor'] = min(nts)
    r['media'] = sum(nts) / len(nts)
    if r['media'] >= 7:
        r['situação'] = 'Boa'
    elif r ['media'] < 5:
        r['situação'] = 'Ruim'
    else:
        r['situação'] = 'Razoavel'
    return r

nts = notas(8.8, 8.5, 9.8, 10, 10)
print(nts)