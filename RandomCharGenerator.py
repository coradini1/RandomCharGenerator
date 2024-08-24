import re
import random
import string

def count_characters(text):
    characters = len(text)
    numbers = sum(c.isdigit() for c in text)
    dots = text.count('.')
    others = len(re.findall(r'[^a-zA-Z0-9.]', text))
    return characters, numbers, dots, others

def replace_with_random(text, total_characters):
    random_characters = ''.join(random.choices(string.ascii_letters + string.digits + '.', k=len(text)))
    while random_characters == text:
        random_characters = ''.join(random.choices(string.ascii_letters + string.digits + '.', k=len(text)))
    return random_characters

def main():
    while True:
        text = input("Enter a word or phrase (or 'exit' to quit): ")
        if text.lower() == 'exit':
            break

        total_characters, total_numbers, total_dots, total_others = count_characters(text)

        total = total_characters

        replaced_text = replace_with_random(text, total)
        print("Text with total number replaced by random characters:")
        print(f"Total overall: {total}")
        print(replaced_text)
        

if __name__ == "__main__":
    main()
