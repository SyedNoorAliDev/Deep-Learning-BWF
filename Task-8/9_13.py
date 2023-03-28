from collections import OrderedDict

glossary = OrderedDict()
glossary['variable'] = 'a name that refers to a value'
glossary['function'] = 'a block of code that can be called and executed'
glossary['class'] = 'a blueprint for creating objects'
glossary['method'] = 'a function defined inside a class'
glossary['loop'] = 'a way to repeat a block of code'

# print each word and its meaning in the order they were added
for word, meaning in glossary.items():
    print(word + ":")
    print(meaning + "\n")
