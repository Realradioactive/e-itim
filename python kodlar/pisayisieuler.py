from math import sqrt

n=int(input("denklemdeki i sayısı ne kadar olsun(ne kadar yüksekse o kadar iyi hesaplar):"))
t = 0

for i in range(1,n):
    t = t + (1 / i ** 2)
    pi = sqrt(6 * t)
print(pi)