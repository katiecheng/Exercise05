from sys import argv

def main():

	filename = argv[1]

	input_file = open(filename)
	file_contents = input_file.read()

	counter = [0]*26

	for character in file_contents:
		if ord(str(character)) >= 65 and ord(str(character)) <= 90:
			counter[ord(character.lower()) - 97] += 1
		elif ord(str(character)) >= 97 and ord(character) <= 122:
			counter[ord(character) - 97] += 1
		else:
			pass

	for count in counter:
		print count

if __name__ == "__main__":
	main()