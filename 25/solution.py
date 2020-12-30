import sys

mod = 20201227
key1,key2 = map(int,sys.stdin.readlines())




import sympy

print(pow(key1,sympy.discrete_log(mod,key2,7),mod))




import cypari2

#print((f'lift(Mod({key1},{mod})^znlog(Mod({key2},{mod}),Mod(7,{mod})))'))
print(cypari2.Pari()(f'lift(Mod({key1},{mod})^znlog(Mod({key2},{mod}),Mod(7,{mod})))'))




from itertools import count

prod = 1
for i in count():
    if prod == key1: break
    prod = (prod*7)%mod
print(pow(key2,i,mod))
