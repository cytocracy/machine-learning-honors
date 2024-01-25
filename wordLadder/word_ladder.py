import string
from util import *

def word_ladder_neighbors(current_word, valid_words):
    '''
    Given a word (current_word) as a string and a set of valid words,
    returns a list of words that are all one letter different 
    than current_word.
    '''
    alphabet = string.ascii_lowercase
    neighbors = []
    for i in range(len(current_word)):
        for letter in alphabet:
            newWord = current_word[:i] + letter + current_word[i+1:]
            if newWord in valid_words and newWord != current_word:
                neighbors.append(newWord)

    return neighbors

def word_ladder_search(valid_words, start_word, end_word):
    '''
    Given a list of valid words, a starting word (string), and an ending 
    word (string), returns the path of of strings representing the word ladder from
    start_word to end_word.
    '''
    startState = (start_word, [start_word])
    visited = set()
    q = [startState]
    while q:
        word, path = q.pop(0)
        if word == end_word:
            return path, len(visited)
        if word not in visited:
            visited.add(word)
            nextWords = word_ladder_neighbors(word, valid_words)
            for nextWord in nextWords:
                if nextWord not in visited:
                    q.append((nextWord, path + [nextWord]))

def better_word_ladder_search(valid_words, start_word, end_word):
    '''
    Given a list of valid words, a starting word (string), and an ending 
    word (string), returns the path of of strings representing the word ladder from
    start_word to end_word. This search should use heuristic_function to speed up
    the search.
    '''
    startState = (start_word, [start_word])
    visited = set()
    q = PriorityQueue()
    q.update(startState, 0)
    while q:
        word, path = q.pop()
        if word == end_word:
            return path, len(visited)
        if word not in visited:
            visited.add(word)
            nextWords = word_ladder_neighbors(word, valid_words)
            for nextWord in nextWords:
                if nextWord not in visited:
                    nextState = (nextWord, path + [nextWord]) 
                    priority = heuristic_function(nextWord, end_word)
                    q.update(nextState, priority)

def heuristic_function(state, end_word):
    count = 0
    for i in range(len(state)):
        if state[i] != end_word[i]:
            count += 1
    return count


if __name__=="__main__":
    # valid_words is a set containing all strings that should be considered valid
    # words (all in lower-case)
    with open('words_alpha.txt') as f:
        valid_words = {i.strip() for i in f}

    print("You have", len(valid_words), "words to work with.")

    start = "atlases"
    end = "cabaret"

    path, numExpanded = word_ladder_search(valid_words, start, end)
    path2, numExpanded2 = better_word_ladder_search(valid_words, start, end)
    print(path)
    print(numExpanded)
    print("better:")
    print(path2)
    print(numExpanded2)