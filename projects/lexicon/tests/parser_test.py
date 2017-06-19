from nose.tools import *
from ex48 import parser
from ex48 import lexicon



def test_peek():
    pass

def test_match():
    results = lexicon.scan("bear go north")

    assert_equal('subject', parser.match(results[0], 0))

def test_sentence():
    results = lexicon.scan("bear go north ")
    sentence = parser.return_sentence(results)

    assert_equal(sentence.subject, "bear")
    assert_equal(sentence.verb, "go")
    assert_equal(sentence.objectS, "north")

def test_hardway():
    results = lexicon.scan("scream at the bear")
    sentence = parser.return_sentence(results)
    assert_equal([sentence.verb, sentence.objectS], ['scream', 'bear'])

def test_assert_error():
    results = lexicon.scan("scream at the bear princess")
    assert_raises(Exception, parser.return_sentence, results)
