def scan(sentence):
    results = []
    words = sentence.split(" ")
    for word in words:
        out_word = word
        if not word.isdigit():
            word = word.lower()
        if word in ['north', 'south', 'east', 'west']:
            results.append(('direction', word))
        elif word in ['go', 'stop', 'kill', 'eat', 'scream']:
            results.append(('verb', word))
        elif word in ['the', 'in', 'of', 'from', 'at', 'it']:
            results.append(('stop', word))
        elif word in ['door', 'bear', 'princess', 'cabinet']:
            results.append(('noun', word))
        elif word in ['up', 'down', 'left', 'right']:
            results.append(('preposition', word))
        elif word.isdigit():
            results.append(('number', int(word)))
        else:
            results.append(('error', out_word))

    return results

    #Takes a word and returns a list of tuples containing the key and the direction


# older bad code :D
#     if word == 'north':
#         results.append(('direction', 'north'))
#     elif word == 'south':
#         results.append(('direction', 'south'))
#     elif word == 'east':
#         results.append(('direction', 'east'))
#     elif word == 'west':
#         results.append(('direction', 'west'))
#     elif word == 'go':
#         results.append(('verb', 'go'))
#     elif word == 'kill':
#         results.append(('verb', 'kill'))
#     elif word == 'eat':
#         results.append(('verb', 'eat'))
#     elif word == 'stop':
#         results.append(('verb', 'stop'))
#     elif word == 'the':
#         results.append(('stop', 'the'))
#     elif word == 'in':
#         results.append(('stop', 'in'))
#     elif word == 'of':
#         results.append(('stop', 'of'))
#     elif word.isdigit():
#         results.append(('number', int(word)))
#     else:
#         results.append(('error', word))
