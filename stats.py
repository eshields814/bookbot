
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character = {}

    lower_char = text.lower()

    for char in lower_char:
        if char in character:
            character[char] += 1
        else:
            character[char] = 1

    return character


def sort_characters(character):
    return character["num"]


def sort_characters_dict(character):

    character_list = []

    for key, value in character.items():
        character_list.append({"char": key, "num": value})
    
    character_list.sort(key=sort_characters, reverse=True)
    return character_list


