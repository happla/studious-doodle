with open("sanoja.txt", "r") as file:
    text = file.read()
words = sorted(text.split())

print("Sanat laitettuna aakkosjärjestykseen:")
for word in words:
	print(word)