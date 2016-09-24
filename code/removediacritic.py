from unicodedata import normalize

def remove_diacritic(s):
   return (normalize('NFKD', s)
           .encode('ascii', 'ignore')
           .decode('ascii'))