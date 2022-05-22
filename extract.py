


with open('test-memaslap', 'r') as f:
  ll = f.readlines()

  for l in ll:
    if l.startswith('[') and '(' in l and l.split('(')[1].split(',')[0] == '27':
      print(l.strip())

  # print(ll[0])