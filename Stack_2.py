from collections import deque


class StackAsDeque:
    """
    Stack implementation as collections deque.
    """

    def __init__(self, list_obj) -> None:
        self.container = deque(list_obj)

    def push(self, value):
        self.container.append(value)

    def pop(self) -> int:
        return self.container.pop()

    def peek(self) -> int:
        return self.container[-1]

    def is_empty(self) -> bool:
        return len(self.container) == 0

    def size(self) -> int:
        return len(self.container)

    def reverse_string(self):
        new_str = ''
        while len(self.container) != 0:
            last_elem = self.peek()
            new_str += last_elem
            self.container.pop()
        return new_str

    
def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2

def is_balanced(statement: str) -> bool:
    stack = StackAsDeque([])

    for ch in statement:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0



if __name__ == "__main__":
    # stack = StackAsDeque()
    # stack.push(5)
    # print(stack.container)
    # elem = stack.peek()
    # print(type(elem))
    # pp = stack.pop()
    # print(type(pp))
    # print(stack.is_empty())

# Exercise_1
    # list_obj = list("We will conquere COVID-19")
    # stack = StackAsDeque(list_obj)
    # print(stack.reverse_string())

# Exercise_2
    print(is_balanced("({a+b}){}}"))