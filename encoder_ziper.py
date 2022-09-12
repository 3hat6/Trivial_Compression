'''
this is a unique encoding program, that allows the user to choose a method from 99
 (sum of common characters) valid options for encoding and also shortens the text with unique way
call for first users_alphabet()
call encoding() after users_alphabet() (after creating encoding option)
and finally rate my work calling decoding_()
'''

import ast
import random
import string


def generating_chars():
    # This function shuffle alphabet for every let and char it chose random char from alphabet and chars
    # And finally we have some special and unique dict
    all_chars = string.ascii_letters + string.digits + string.punctuation[:-1] + string.whitespace
    dct, rand_nums, i = {}, [], 0
    while len(dct.keys()) != 99:
        rand_num = random.randint(0, 98)
        if rand_num not in rand_nums:
            dct[all_chars[i]] = all_chars[rand_num]
            rand_nums.append(rand_num)
            i += 1
    return dct


def users_alphabet():
    # This function let user chose his own encoding option with interesting way
    alphabet_name = input('Choose name for your alphabet its important (endswith .txt): ')
    while True:
        shuffled = generating_chars()
        print(shuffled)
        user_wish = input('do you wanna shuffle it one more time? (Yes/No) ')
        if user_wish.lower() == 'no':
            break
    with open(alphabet_name, 'w') as file:
        file.write(str(shuffled))


def encoding():
    alp_name = input('Which alphabet you prefer for encoding? type file name: ')
    file_path = input('and what`s your text? put file path here: ')
    encoding_file = open(file_path).read()
    with open(alp_name) as f:
        read_alp = f.read()
    enc_alp = ast.literal_eval(read_alp)
    f.close()
    encoded_file = input('write finally name for your encoded text (endswith .txt): ')
    encoded_file = open(encoded_file, 'w')
    word = ''
    for char in encoding_file:
        word += char
        if char in (string.whitespace + '.?!,'):
            if encoding_file.count(word) >= 3 and len(word) > 3:
                if word not in enc_alp.keys():
                    spec_char = list(enc_alp)[random.randint(0, 98)] + list(enc_alp)[random.randint(0, 98)]
                    while spec_char in enc_alp.values():
                        spec_char = list(enc_alp)[random.randint(0, 98)] + list(enc_alp)[random.randint(0, 98)]
                    enc_alp[word] = '~' + spec_char
                    encoded_file.write(enc_alp[word] and enc_alp[' '])
                    word = ''
                else:
                    encoded_file.write(enc_alp[word] and enc_alp[' '])
                    word = ''

            else:
                for elem in word:
                    encoded_file.write(enc_alp[elem])
                encoded_file.write(enc_alp[' '])
                word = ''
    with open(alp_name, 'w') as file:
        file.write(str(enc_alp))
        f.close()


def decoding_():
    alp_name = input('Which alphabet you used for encoding? type file name: ')
    file_path = input('and what text you encoded genius? put file path here: ')
    decoding_file = open(file_path).read()
    with open(alp_name) as f:
        alp_name = f.read()
    enc_alp = ast.literal_eval(alp_name)
    dec_alp = {v: k for k, v in enc_alp.items()}
    decoded_file = input('write finally name for your decoded text and never do it (endswith .txt)! ')
    decoded_file = open(decoded_file, 'w')
    text = ''
    for elem in decoding_file:
        text += elem
        if text.startswith('~'):
            try:
                decoded_file.write(dec_alp[text])
                text = ''
            except KeyError:
                pass
        else:
            decoded_file.write(dec_alp[text])
            text = ''

    decoded_file.close()


users_alphabet()
encoding()
decoding_()
