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

    def __init__(self, smoothing: float, context_size: int) -> None:
        assert smoothing > 0 and smoothing <= 1
        assert context_size > 0

        self.index = dict()
        self.symbols = set()
        self.smoothing = smoothing
        self.context_size = context_size

    def hash_text(self, text: str):
        hash = md5()
        hash.update(text.encode("utf-8"))
        return hash.hexdigest()

    def get_all_contexts(self) -> Set[Tuple[str]]:
        return set(product(self.symbols, repeat=self.context_size))

    def get_probability(self, symbol: str, context: str):
        assert len(context) == self.context_size

        res = self.index[context][symbol] + self.smoothing
        other = self.smoothing * len(self.symbols)

        for key in self.index[context]:
            other += self.index[context][key]

        return res / other

    def get_information_amount(self, symbol: str, context: str):
        pass

    def get_entropy(self, context: str):
        pass

    def add_symbols_from_text(self, text: str):
        self.symbols.update(sorted(set(text)))

        for context in self.get_all_contexts():
            self.index[''.join(context)] = defaultdict(int)

    def add_file(self, path: str):
        file = open(path, "r")
        text = file.read()
        self.add_text(text)

    def add_text(self, text: str):
        assert len(text) > 0

        i = 0
        hash = self.hash_text(text)
        self.add_symbols_from_text(text)

        if self.load_cache(hash):
            return

        while i < len(text):
            if i + self.context_size >= len(text):
                break

            context = text[i: i + self.context_size]
            symbol = text[i + self.context_size]
            self.add_sequence(symbol, context)
            i += 1

        self.save_cache(hash)

    def add_sequence(self, symbol: str, context: str):
        assert len(symbol) == 1
        assert len(context) == self.context_size
        assert context in self.index

        self.index[context][symbol] += 1

    def save_cache(self, hash: str):
        assert len(hash) == 32

        path = f"cache/{hash}"
        file = open(path, "wb")
        pickle.dump(self.index, file)

    def load_cache(self, hash: str):
        assert len(hash) == 32

        path = f"cache/{hash}"

        if not exists(path):
            return False

        file = open(path, "rb")
        self.index.update(pickle.load(file))
        return True
