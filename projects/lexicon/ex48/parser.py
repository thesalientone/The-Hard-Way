import lexicon
class Sentence(object):
    def __init__(self):
        self.subject = None
        self.verb = None
        self.objectS = None

    def assignsubject(self, word):
        self.subject = word
    def assignverb(self, word):
        self.verb = word
    def assignobject(self, word):
        self.objectS = word

def match(word_tuple, position):
    if (word_tuple[0] == 'noun') and (position == 0):
        return 'subject'
    elif word_tuple[0] in ['direction', 'noun']:
        return 'objectS'
    elif word_tuple[0] == 'verb':
        return 'verb'
    else:
        return None

class WordCount(Exception):
    def __init__(self):
        pass


def return_sentence(user_input):
    sentence = Sentence()
    dictionary = {
        'subject' : sentence.assignsubject,
        'verb' : sentence.assignverb,
        'objectS' : sentence.assignobject
    }

    results = user_input
    for word_tuple in results:
        sentence_part = match(word_tuple, results.index(word_tuple))
        if sentence_part:
            evalcode = "sentence." + sentence_part
            if eval(evalcode):
                raise Exception('Word Count')
            else:
                dictionary[sentence_part](word_tuple[1])
    if not sentence.subject:
        sentence.subject = 'player'
    return(sentence)
