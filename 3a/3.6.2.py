def lone_sum(a, b, c):
  sumi = 0
  sumi += a if a not in [b,c] else 0
  sumi += b if b not in [a,c] else 0
  sumi += c if c not in [a,b] else 0
  return sumi