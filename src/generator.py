from random import choices
from fcm import Fcm


class Generator:
    prior: str
    model: Fcm

    def __init__(self, Fcm):
        self.model = Fcm

    def generate(self, prior: str, length: int):
        context_size = self.model.get_context_size()
        res = prior

        for _ in range(0, length - len(prior)):
            res += self.next_symbol(res[-context_size:])

        return res

    def next_symbol(self, context: str):
        context_symbol_ocurrences = self.model.get_context(context)

        return choices(list(context_symbol_ocurrences.keys()),
                       weights=list(context_symbol_ocurrences.values()),
                       k=1)[0]
