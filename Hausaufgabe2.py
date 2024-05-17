def buchstabe_ändern(string,buchstabe):
    
    vokale = "aeiou"
    ergebnis = []
    
    vokal_index = 0

    for char in string:
        if char.lower() == buchstabe.lower():
            ergebnis.extend(vokale[vokal_index])
            vokal_index = (vokal_index +1) % len(vokale)
        else:
            ergebnis.append(char)
    
    return "".join(ergebnis)

text = "wie geht es ihnen?"
buchstabe = "a"
print(buchstabe_ändern(text, buchstabe))