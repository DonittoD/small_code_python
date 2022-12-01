import string
from random import randint
tab=list(string.ascii_letters)
tabchiffre=(string.digits)
tabspecial=list(string.punctuation)

for i in range(len(tabchiffre)):
    tab.append(tabchiffre[i])

passsize=8
mdp=""
a, b=randint(0,passsize-1) , 0
c=True
while b==a or c!=False:
    b=randint(0,passsize-1)
    c=False

for i in range (passsize):
    if i == a or i == b:
        mdp+=tabspecial[randint(0,len(tabspecial)-1)]
    else:
        mdp+=tab[randint(0,len(tab)-1)]
print(mdp)