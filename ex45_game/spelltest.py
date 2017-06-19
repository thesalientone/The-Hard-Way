spells = ['cure', 'cure2', 'cure3']

y = enumerate(spells , 1)

spells_numbered = list(y)
display_text = []

for x in spells_numbered:

    display_text.append("%d. %s" %(x[0] , x[1]))
extend_amount = (4 - ((len(spells) + 4) % 4))
for x in range(extend_amount):
    display_text.append(" ")
print display_text


x = range(10)

print x[0:4]
print x[4:8]

b = "5"

if int(b) == int():
    print 'yes'
