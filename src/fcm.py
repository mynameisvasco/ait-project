from os.path import exists
from typing import Dict, Set, Tuple
from itertools import product
from collections import defaultdict
import pickle
from hashlib import md5


class Fcm:
    index: Dict[str, Dict[str, int]]
    symbols: Set[str]
    smoothing: float
    context_size: int

    def __init__(self, symbols: Set[str], smoothing: float, context_size: int) -> None:
        assert len(symbols) > 0
        assert smoothing > 0
        assert context_size > 0

        self.index = dict()
        self.symbols = symbols
        self.smoothing = smoothing
        self.context_size = context_size

        for context in self.get_all_contexts():
            self.index[''.join(context)] = defaultdict(int)

    def get_all_contexts(self) -> Set[Tuple[str]]:
        return set(product(self.symbols, repeat=self.context_size))

    def get_probability(self, before: str, after: str):
        assert len(before) == self.context_size

        res = self.index[before][after]
        other = 0

        for key in self.index[before]:
            other += self.index[before][key]

        return res / other

    def add_file(self, path: str):
        assert exists(path)

        file = open(path, "r")
        text = file.read()

        hash = md5()
        hash.update(text.encode("utf-8"))
        hash = hash.hexdigest()

        i = 0

        if self.load_cache(hash):
            return

        while i < len(text):
            if i + self.context_size >= len(text):
                break

            before = text[i: i + self.context_size]
            after = text[i + self.context_size]
            self.add_sequence(before, after)
            i += 1

        self.save_cache(hash)

    def add_sequence(self, before: str, after: str):
        assert len(before) == self.context_size
        assert len(after) == 1
        assert before in self.index

        self.index[before][after] += 1

    def save_cache(self, hash: str):
        path = f"cache/{hash}"
        file = open(path, "wb")
        pickle.dump(self.index, file)

    def load_cache(self, hash: str):
        path = f"cache/{hash}"

        if not exists(path):
            return False

        file = open(path, "rb")
        self.index.update(pickle.load(file))
        return True
