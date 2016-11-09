
vowel=['abacus','election','tubet','organization']

def only_vowels(list):
    for string in list:
      if list[0] in ['a','e','i','o','u']:
          print(list)

print(only_vowels(vowel))
print(only_vowels(('equal','tacos','broken')))