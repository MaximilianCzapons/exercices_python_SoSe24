import matplotlib.pyplot as plt 

spar_funktion = []

AK = 10000
SR = 1000
i = 0.01
lz = 10
summe = 0

for k in range (1, lz+1):
    summe += (AK + SR) * (1+i)
    spar_funktion.append(summe)

print(spar_funktion)
plt.bar(range(1,11), spar_funktion)