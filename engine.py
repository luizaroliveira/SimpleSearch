# -*- coding: utf-8 -*-

import re, os, unicodedata
from collections import defaultdict
from datetime import datetime

# Compiling pattern to make it faster to call it multiple times.
SPLIT_PATTERN = re.compile(r"[^\w]")

FILE_NAMES = {}
INDEX = defaultdict(set)
STOPWORDS = ['of', 'the', 'a', 'an']


def index_text(index, text):
    """" Adds text to the current index. """
    for term in tokenize(text):
        INDEX[term].add(index)


def load_files(path=None):
    """" Reads all the files in the data path and indexes them. """

    workdir = path or 'data'

    # Testing if data path exists
    if not os.path.isdir(workdir):
        raise(AttributeError('Data directory not found'))

    #  List the files inside the data folder
    files = os.listdir(workdir)
    if not files:
        raise(FileNotFoundError('No files found in the data folder. No data available for indexing'))

    # Feeding the FILE_NAMES dict, which will be used for recovering the names later on
    for index, file in enumerate(os.listdir(workdir), 1):
        file_path = os.path.join(workdir, file)
        FILE_NAMES[index] = file_path

        # Indexing the text of each file
        try:
            _file = open(file_path)
            text = _file.read()
            _file.close()
            index_text(index, text)
        except FileNotFoundError:
            print(file)
            print("File above can't be read and might be corrupted")


def tokenize(text):
    return sorted([
        # Normalizando o texto
        unicodedata.normalize('NFKD', token.lower()).encode('ASCII', 'ignore').decode()
        # Separando o string em caracteres especiais
        for token in set(re.split(SPLIT_PATTERN, text))
        # removendo stopwords
        if token and token not in STOPWORDS
    ])


def query(terms):
    """" Returns a list of files where all the terms of the query can be found."""

    # For calculating the query time
    start = datetime.now()

    # The query must go through the same text tokenizing used for the files.
    tokens = tokenize(terms)

    # Finds the files that contain each token
    result_sets = [INDEX[token] for token in tokens]

    # Finds the files that contain all the tokens
    result = set.intersection(*result_sets)

    print('Results: %s. Time spent: %s' % (len(result), (datetime.now()-start).microseconds))

    # Returns a list with the names of the results
    return [FILE_NAMES[index] for index in result]
