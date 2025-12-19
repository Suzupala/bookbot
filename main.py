
import sys
from stats import sorting_most_common
from stats import count_letters2
from stats import count_words
def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		book_path = sys.argv[1]
		#get_book_text(book_path)
		word_count = count_words(book_path)
		#print(f"Found {word_count} total words")
		letter_count = count_letters2(book_path)
		most_common = sorting_most_common(letter_count)

		print ("============ BOOKBOT ============")
		print (f"Analyzing book found at {book_path}...")
		print ("----------- Word Count ----------")
		print (f"Found {word_count} total words")
		print ("--------- Character Count -------")
		for i in most_common:
			character = i["char"]
			number = i["num"]
			print(f"{character}: {number}")
		print("============= END ===============")


main()
