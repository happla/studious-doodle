class Kilpailija:
	def eka(self):
		vari = "sininen"
		pisteet = 10
		return "Kilpailijalla {} on  {} pistettä!".format(vari,pisteet)
	
kilpailija = Kilpailija()
print(kilpailija.eka())
