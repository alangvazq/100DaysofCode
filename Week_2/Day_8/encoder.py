alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar (direction, text, shift):
  cipher = ''

  if direction == 'encode':
    alphabet = alphabet[::-1]

  for letter in text:
    index = alphabet.index(letter)
    position = index + shift
    alphabet_len = len(alphabet) - 1

    if position > alphabet_len:
      while position >= len(alphabet):
            position -= len(alphabet)
      cipher += alphabet[position]
    else:
      cipher += alphabet[position]

  print(cipher)