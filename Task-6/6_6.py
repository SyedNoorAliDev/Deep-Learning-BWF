favorite_languages = {
    'Ali': 'python',
    'sarah': 'c',
    'ed': 'ruby',
    'Ahmed': 'python',
}

people_to_poll = ['Ali', 'sarah', 'ed', 'Ahmed', 'mike', 'john', 'alice']

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to the poll!")
    else:
        print(f"{person.title()}, what's your favorite programming language? Please take the poll!")
