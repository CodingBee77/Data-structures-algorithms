class StackAsList:
    """
    Stack implementation as list (not recommended).
    """
    def __init__(self, empty_list) -> None:
        self.empty_list = empty_list
    

    def append_address(self,http_address:str)->None:
        self.empty_list.append(http_address)
    

if __name__ == "__main__":
    empty_list = []
    stack = StackAsList(empty_list)
    stack.append_address('https://www.cnn.com/')
    stack.append_address('https://www.cnn.com/world')
    stack.append_address('https://www.cnn.com/india')
    stack.append_address('https://www.cnn.com/china')
    print(stack.empty_list)
    stack.empty_list.pop()
    print(stack.empty_list)
