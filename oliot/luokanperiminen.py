class Emo:
    arvo = 0
    tila = "Toiminnassa"
    def nimi(self):
        return "Minä olen emoluokka."
    
class Lapsi(Emo):
    def nimi(self):
        return "Minä olen lapsiluokka."
    
emo = Emo()
lapsi = Lapsi()


print(emo.tila)
print(emo.nimi())

print(lapsi.tila)
print(lapsi.nimi())
