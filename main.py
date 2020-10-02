from itertools import permutations 
def to_int(s): 
  return ‘’.join(s) 
S = [ to_int(s) for s in permutations('0123456789', 4) if s[0] != '0' ] 
print(len(S)) 
