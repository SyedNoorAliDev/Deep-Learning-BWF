filename = "example_text.txt"

with open(filename, "r") as file:
    contents = file.read()

the_count = contents.lower().count("the")

print(f"The word 'the' appears {the_count} times in the file {filename}.")
