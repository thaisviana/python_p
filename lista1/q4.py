import unicodedata

def normalize(data):
  """ Normalise (normalize) unicode data in Python to remove umlauts, accents etc. """
  return unicodedata.normalize('NFKD', data).encode('ASCII', 'ignore')

def limpa_texto(texto):
    texto = texto.casefold()
    texto_limpo = texto.replace(" ","")
    texto_limpo = texto_limpo.replace("-","").replace(",","").replace(".","").replace("/","")
    texto_limpo = normalize(texto_limpo)
    return texto_limpo

texto_limpo = limpa_texto("anana")
print(texto_limpo[:len(texto_limpo)//2], texto_limpo[len(texto_limpo)//2:])
if texto_limpo == texto_limpo[::-1]:
    print("palíndromo")
else:
    print("não é palíndromo")