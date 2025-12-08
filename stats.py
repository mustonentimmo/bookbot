from typing import TypedDict

Character = TypedDict('Character', {"char": str, "num": int})

def get_sorted_characters(dictionary: dict[str, int]) -> list[Character]:
    sorted_characters_list: list[Character] = []

    def sort_by_num(items):
        return items["num"]

    for key, value in dictionary.items():
        sorted_characters_list.append({"char": key, "num": value})

    sorted_characters_list.sort(key=sort_by_num, reverse=True)

    return sorted_characters_list

def get_num_words(text: str) -> int:
    return len(text.split())

def get_characters_count(text: str) -> dict[str, int]:
    characters = {}

    for char in text:
        char = char.lower()

        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    return characters

