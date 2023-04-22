class Kilpailija:
    """Kilpailija: sisältää pisteet ja värin"""
    def __init__(self):
        self.vari = input("Anna minulle väri: ")
        self.pisteet = 0
    
    def tilanne(self):
        return "Olen {} ja minulla on {} pistettä!".format(self.vari, self.pisteet)
    
def main():
    kilpailija1 = Kilpailija()
    kilpailija2 = Kilpailija()
    print(kilpailija1.tilanne())
    print(kilpailija2.tilanne())
    print(Kilpailija.__doc__)
    
if __name__ == "__main__":
    main()