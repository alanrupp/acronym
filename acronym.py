#!/usr/bin/python

'''
Finding words that are valid english acronyms from input words
'''

import itertools
import csv

# load english dictionary from dwyl
def load_words(with_vowel=True, quiet=False):
    if not quiet: print('Loading words ...')
    with open('words_alpha.txt') as word_file:
        valid_words = list(set(word_file.read().split()))
    if with_vowel:
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        has_vowel = [any([x in vowels for x in word]) for word in valid_words]
        valid_words = list(itertools.compress(valid_words, has_vowel))
    return valid_words

# get all substrings of a given word
def get_subs(word):
    return [word[:x+1] for x in range(len(word))]

# get all combinations of substrings from a word list
def get_combos(word_list, quiet=False):
    if not quiet: print('Generating intial combinations ...')
    subs = [get_subs(x) for x in word_list]       # create word substrings
    # permute order of word lists
    perm = itertools.permutations(range(len(word_list)))
    d = {}
    for p in perm:
        name = ' '.join([word_list[x] for x in p]) # make name for dict key
        words = [subs[x] for x in p]               # order substrings
        combos = list(itertools.product(*words))   # generate sub combinations
        combos = [''.join(x) for x in combos]      # combine tuples to str
        d[name] = combos                           # add result dictionary
    return d

# filter word combinations dictionary by presence in valid_word list
def filter_list(word_combos, valid_words, quiet=False):
    if not quiet: print('Filtering acronyms for valid words ...')
    d = {}
    length = 0
    for k in word_combos.keys():
        d[k] = list(set(word_combos[k]) & set(valid_words))
        length += len(d[k])
    print(f"Found {length} valid acronyms")
    return d

def write(result, quiet=False):
    if not quiet: print('Writing result to acronyms.tsv ...')
    with open('acronyms.tsv', 'w') as f:
        f.write("name,acronym\n")
        for key in result.keys():
            for value in result[key]:
                f.write(f"{clean(key, value)}\n")

# - Run ----------------------------------------------------------------------
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('words', help='Words', nargs='+')
    parser.add_argument('--quiet', action='store_true')
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    english_words = load_words(quiet=args.quiet)         # read in english words
    args.words = [x.lower() for x in args.words]      # make all input lowercase
    combos = get_combos(args.words, quiet=args.quiet)          # generate combos
    acronyms = filter_list(combos, english_words, quiet=args.quiet)
    acronyms = {k:v for k,v in acronyms.items() if v}      # remove empty values
    # print result
    for key in acronyms.keys():
        for value in acronyms[key]:
            print(f"{value.upper()}\t{key}")
    if args.write: write(acronyms, quiet=args.quiet)                # write file
