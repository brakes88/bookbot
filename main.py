def main(file_path):
    with open(file_path) as f:
        file_contents=f.read()

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(file_contents.split())} words found in the document")
        print("")
        
        characters=list(file_contents)

        count_char={}
        for character in characters:
            if character.isalpha():
                lowered_character=character.lower()
                if not lowered_character in count_char:
                    count_char[lowered_character] = 0

                count_char[lowered_character] += 1

        

        for key in sorted(count_char,key=count_char.get,reverse=True):
            print(f"The '{key}' character was found {count_char[key]} times")

        print("--- End report ---")



main("books/frankestein.txt")
