class StringReverser:
    def __init__(self, word):
        self.string = word

    def reverse_words(self):
        words = self.string.split()
        reversed_words = words[::-1]
        return (reversed_words)


string = "My name is Mannan Sood"
reverser = StringReverser(string)
reversed_string = reverser.reverse_words()
print("Orignal String")
print(string)
print("Reversed String")
print(*reversed_string) 