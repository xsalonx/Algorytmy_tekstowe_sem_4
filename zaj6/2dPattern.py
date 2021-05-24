## aho - corasic algorithm

from collections import defaultdict

class Automaton:
    def __init__(self, patterns):
        self.patterns = patterns.copy()
        self.signum = list(set("".join(patterns)))
        self.f = []

        def_state=  lambda : 0
        self.delta = [defaultdict(def_state, [])]
        self.final = [0] * len(patterns)

        # build main edges:
        for i, p in enumerate(patterns):
            currState = 0
            for j, c in enumerate(p):
                if c not in self.delta[i].keys():
                    currState += 1
                    if currState >= len(self.delta):
                        self.delta.append(defaultdict(def_state, []))
                    self.delta[currState][c] = currState
                else:
                    currState = self.delta[currState][c]
            self.final[currState] |= (1 << i)





if __name__ == '__main__':
    patterns = ["aab", "bba", "abc"]
    text = "abcdcdcbgvfaasd"

