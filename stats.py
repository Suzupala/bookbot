
def count_words(filepath):
	with open(filepath) as f:
		file_contents = f.read()
		word_count = len(file_contents.split())
	return word_count


def count_letters(filepath):
	letter_count= {}
	alphabet = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
	with open(filepath) as f:
		file_contents = str.lower(f.read())
	for a in alphabet:
		letter_count[a] = file_contents.count(a)
	return letter_count



def sort_on(items):
	return items["num"]

def sorting_most_common(letter_count):
	keylist = []
	for letter in letter_count:
		char_dict = {"char": letter, "num": letter_count[letter]}
		keylist.append(char_dict)
	#list of dictionaries created: sorting to be done
	keylist.sort(reverse=True, key=sort_on)
	return keylist



def count_letters2(filepath):
	letter_count = {}
	with open(filepath) as f:
		file_contents = str.lower(f.read())
	for char in file_contents:
		if char .isalpha():
			if char not in letter_count:
				letter_count[char] = 1
			else:
				letter_count[char] += 1
	return letter_count

