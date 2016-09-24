def remove_diacritic(s):
   return normalize('NFKD', s).encode('ascii', 'ignore')
