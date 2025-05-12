from collections import defaultdict

class TuringMachine:
    def __init__(self, transition_function, start_state, accept_state, reject_state):
        self.delta = transition_function
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state

        self.state = start_state
        self.tape = defaultdict(lambda: '_')
        self.head = 0

    def step(self):
        read = self.tape[self.head]
        new_state, write, direction = self.delta(self.state, read)
        self.state = new_state
        self.tape[self.head] = write
        if direction == "RIGHT":
            self.head += 1
        else: #direction == "LEFT"
            self.head -= 1

    def run(self, tape):
        self.tape = tape
        while True:
            if self.state == self.accept_state:
                print("input accepted :)")
                break
            if self.state == self.reject_state:
                print("input rejected :(")
                break
            self.step()

class MultiHeadTM(TuringMachine):
    def __init__(self, transition_function, start_state, accept_state, reject_state, num_heads):
        super().__init__(transition_function, start_state, accept_state, reject_state)
        self.num_heads = num_heads
        


