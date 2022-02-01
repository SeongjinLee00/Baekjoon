s=input()

letters=len(s)

letters-=s.count('c=')
letters-=s.count('c-')
letters-=(s.count('dz=')*2)
letters-=s.count('d-')
letters-=s.count('lj')
letters-=s.count('nj')
letters-=s.count('s=')
letters-=(s.count('z=')-s.count('dz='))

print(letters)