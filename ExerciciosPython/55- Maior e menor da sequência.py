bigger = 0
minor = 0
for c in range(1,6):
    weight = float(input('Weight of {}ª people (Kg): '.format(c)))
    if c == 1:
        bigger = weight
        minor = weight
    else:
        if weight > bigger:
            bigger = weight
        if weight < minor:
            minor = weight
print('The bigger weight read was: {:.2f} Kg'.format(bigger))
print('The smaller weight read was: {:.2f} Kg'.format(minor))