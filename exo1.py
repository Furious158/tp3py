def replace_all(s, o, r):
    
    return r.join(s.split(o))

# Exemple d'utilisation
texte = "bonjour tout le monde"
ancien = "o"
nouveau = "a"
resultat = replace_all(texte, ancien, nouveau)
print(resultat)  # Résultat : "banjaur taut le mande"
