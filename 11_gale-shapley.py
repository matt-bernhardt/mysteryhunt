# Pairing cows and bulls...
def func(rankings, M):
  unengaged = M[:]
  proposals = {m:-1 for m in M}
  matches = {}
  while len(unengaged) > 0:
    m = unengaged.pop()
    proposal = proposals[m] + 1
    proposals[m] = proposal
    w = rankings[m][proposal]
    if not w in matches:
      matches[w] = 0 
    else:
      m2 = matches[w]
      if rankings[w].index(m) < rankings[w].index(m2):
        matches[w] = m
        unengaged.append(m2)
      else:
        unengaged.append(m)
  result = {(m,w) for w,m in matches.items()}
  return sorted(result)
