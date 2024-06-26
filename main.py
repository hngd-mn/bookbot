def main():
    import sys
    file=sys.argv[1] #using launch parameter
    import argparse

    parser=argparse.ArgumentParser(description='''Help for wordcounter: ''')
    parser.add_argument('path/file.txt', nargs='*', default=[1, 2, 3], help='Path to a file that needs to have its words and letters counted')
    args=parser.parse_args()

    with open(file) as book:
        file_contents = book.read()
        word_count = file_contents.split()
        print("--- Begin report of", book.name, " ---")
        print(len(word_count), " - Words found in the book")
 
        lowered_text = file_contents.lower() #converts txt to small letters
        dict_of_letters = {}
        for character in lowered_text:
            letter = character.isalpha() #checks if character is a letter
            if character not in dict_of_letters and letter == True:
                dict_of_letters[character] = 1
            elif character in dict_of_letters and letter == True:
                dict_of_letters[character] += 1

        list_of_letters = []
        for letter in dict_of_letters:
            list_of_letters.append({"Name":letter, "Count": dict_of_letters[letter]})
        def sort_on(d):
            return d["Count"]

        list_of_letters.sort(reverse=True, key=sort_on)

        for let_in_list in list_of_letters:
                print("The letter", let_in_list['Name'], "was found", let_in_list['Count'], "times")
        print("--- End report ---")


main()