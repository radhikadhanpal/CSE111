from sentences import get_determiner, get_noun, get_preposition, get_prepositional_phrase, get_verb
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 11)

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(quantity)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    # 1. Test the single noun.

    single_noun = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]

    for _ in range(10):

        word = get_noun(1)

        assert word in single_noun

    plural_noun = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]

    for _ in range(10):

        quantity = random.randint(2, 11)

        word = get_noun(quantity)

        assert word in plural_noun



def test_get_verb():

    past_verb = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    
    for _ in range(5):

        word = get_verb(1,"past")

        assert word in past_verb

    singular_present_verb = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(5):

        word = get_verb(1,"present")

        assert word in singular_present_verb

    plural_present_verb = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    for _ in range(5):

        word = get_verb(2, "present")

        assert word in plural_present_verb

    future_verb = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]

    for _ in range(5):

        word = get_verb(1, "future")

        assert word in future_verb

def test_get_preposition():

    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"] 

    for _ in range(5):

        preposotion = get_preposition()

        assert preposotion in prepositions

def test_prepositional_phrase():
    prepositions = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", 
        "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"] 
    plural_noun = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]
    single_noun = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
    plural_determiners = ["two", "some", "many", "the"]
    single_determiners = ["a", "one", "the"]

    for _ in range(5):
        word = get_prepositional_phrase(1)
        words = word.split(" ")

        assert words[0] in prepositions


    for  _ in range(5):
        word = get_prepositional_phrase(1)
        words = word.split(" ")

        assert words[1] in single_determiners

    for  _ in range(5):
        word = get_prepositional_phrase(1)
        words = word.split(" ")

        assert words[2] in single_noun

    for  _ in range(5):
        word = get_prepositional_phrase(2)
        words = word.split(" ")

        assert words[2] in plural_noun

    for  _ in range(5):
        word = get_prepositional_phrase(2)
        words = word.split(" ")

        assert words[1] in plural_determiners



pytest.main(["-v","--tb=line","-rN",__file__])