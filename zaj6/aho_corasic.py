## aho - corasic algorithm


from collections import deque


class State:
    def __init__(self, id, character=''):
        self._character = character
        self._id = id
        self._next = {}
        self._out = []
        self._on_fail_ret_to = 0
        self._fail_transition_established = False

    def get_next_states(self):
        return self._next.values()

    def __str__(self):
        return f"State( id:{self._id}, char<{self._character}>, next:{self._next}, on_fail:{self._on_fail_ret_to} )"

class Searcher:
    def __init__(self, case_sensitive=True, dtype=None):
        self.__states = [State(id=0)]
        self.__patterns = ['']  # Null pattern to start enumerating rest from 1
        self.__patterns_to_idx = {'': 0}
        self.__case_sensitive = case_sensitive
        # TODO types handling
        self.__dtype = dtype

    def __str__(self):
        return "TextSearcher:\n   " + "\n   ".join([s.__str__() for s in self.__states])

    def pattern_idx(self, pattern):
        return self.__patterns_to_idx[pattern]

    def __next_state(self, state, character):
        if character in self.__states[state]._next.keys():
            return self.__states[state]._next[character]
        return None

    def add(self, pattern, establish=True):
        if not self.__case_sensitive and self.__dtype == str:
            pattern = pattern.lower()

        if pattern in self.__patterns_to_idx.keys():
            return
        self.__patterns.append(pattern)
        self.__patterns_to_idx[pattern] = len(self.__patterns) - 1

        curr_state = 0
        j = 0
        next_state = self.__next_state(curr_state, pattern[j])
        while next_state != None:
            curr_state = next_state
            j = j + 1
            if j < len(pattern):
                next_state = self.__next_state(curr_state, pattern[j])
            else:
                break
        for i in range(j, len(pattern)):
            new_state = State(id=len(self.__states), character=pattern[i])
            self.__states.append(new_state)
            self.__states[curr_state]._next[pattern[i]] = len(self.__states) - 1
            curr_state = len(self.__states) - 1
        self.__states[curr_state]._out.append(self.__patterns_to_idx[pattern])

        if establish:
            self.__establish_fail_transitions()


    def add_all(self, patterns):
        for p in patterns:
            self.add(p, establish=False)
        self.__establish_fail_transitions()

    def __establish_fail_transitions(self):
        # BFS
        Q = deque()
        for s in self.__states[0].get_next_states():
            # if not self.__states[s]._fail_transition_established:
                Q.append(s)
                self.__states[s]._on_fail_ret_to = 0
        while Q:
            q = Q.popleft()
            for v in self.__states[q].get_next_states():
                Q.append(v)
                state = self.__states[q]._on_fail_ret_to

                while state != 0 and self.__next_state(state, self.__states[v]._character) == None:
                    state = self.__states[state]._on_fail_ret_to
                self.__states[v]._on_fail_ret_to = self.__next_state(state, self.__states[v]._character)

                if self.__states[v]._on_fail_ret_to is None:
                    self.__states[v]._on_fail_ret_to = 0
                self.__states[v]._out += self.__states[self.__states[v]._on_fail_ret_to]._out
            # self.__states[q]._fail_transition_established = True


    def search(self, sequance):
        if not self.__case_sensitive and self.__dtype == str:
            sequance = sequance.lower()
        current_state = 0
        res = []

        for i, c in enumerate(sequance):
            while self.__next_state(current_state, c) is None and current_state != 0:
                current_state = self.__states[current_state]._on_fail_ret_to
            current_state = self.__next_state(current_state, c)
            if current_state is None:
                current_state = 0
            else:
                for k in self.__states[current_state]._out:
                    res.append((i - len(self.__patterns[k]) + 1, k))
        return res


if __name__ == '__main__':
    patter = "__a"
    text = "___a"
    S = Searcher()
    S.add(patter)
    res = S.search(text)
    print(res)

