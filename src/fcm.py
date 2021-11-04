from typing import Dict, Set
from collections import defaultdict
from math import log2


class Fcm:
    index: Dict[str, Dict[str, int]]
    symbols: Set[str]
    smoothing: float
    context_size: int

    def __init__(self, smoothing: float, context_size: int) -> None:
        assert smoothing > 0 and smoothing <= 1
        assert context_size > 0

        self.index = defaultdict(lambda: defaultdict(int))
        self.symbols = set()
        self.smoothing = smoothing
        self.context_size = context_size

    def get_context(self, context: str):
        assert len(context) == self.context_size

        return self.index[context]

    def get_context_size(self):
        return self.context_size

    def get_symbol_occurrence(self, symbol: str, context: str):
        assert len(context) == self.context_size

        return self.index[context][symbol]

    def get_symbol_probability(self, symbol: str, context: str):
        assert len(context) == self.context_size

        res = self.index[context][symbol] + self.smoothing
        other = self.smoothing * len(self.symbols)

        for key in self.index[context]:
            other += self.index[context][key]

        return res / other

    def get_context_probability(self, context: str):
        assert len(context) == self.context_size
        res, total = 0, 0

        for symbol in self.index[context]:
            res += self.index[context][symbol]

        for state in self.index:
            for symbol in self.index[state]:
                total += self.index[state][symbol]

        return res / total

    def get_information_amount(self, symbol: str, context: str):
        return -log2(self.get_symbol_probability(symbol, context))

    def get_context_entropy(self, context: str):

        res = 0

        for symbol in self.index[context]:
            res += self.get_information_amount(symbol, context) * \
                self.get_symbol_probability(symbol, context)

        return res

    def get_model_entropy(self):
        res = 0

        for context in self.index:
            res += self.get_context_probability(context) * \
                self.get_context_entropy(context)

        return res

    def add_symbols_from_text(self, text: str):
        self.symbols.update(set(text))

    def add_file(self, path: str):
        file = open(path, "r")
        text = file.read()
        self.add_text(text)

    def add_text(self, text: str):
        assert len(text) > 0

        i = 0
        self.add_symbols_from_text(text)

        while i < len(text):
            if i + self.context_size >= len(text):
                break

            context = text[i: i + self.context_size]
            symbol = text[i + self.context_size]
            self.add_sequence(symbol, context)
            i += 1

    def add_sequence(self, symbol: str, context: str):
        assert len(symbol) == 1
        assert len(context) == self.context_size

        if symbol in self.index[context]:
            self.index[context][symbol] += 1
        else:
            self.index[context][symbol] = 1
