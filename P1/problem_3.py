import sys
import heapq


class HeapNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq < other.freq


def huffman_encoding(data):
    # create frequency generator
    # generate  priority queue(using heap)
    # generate huffman tree
    # generate codes for char
    if not data:
        print("No data to encode!")
        return "", []
    frequency = make_frequency(data)
    make_heap(frequency)
    merge_codes()
    make_codes()
    return get_encoded_text(data), heap


heap = []
codes = {}
reverse_codes = {}


def make_frequency(txt):
    frequency = {}
    for char in txt:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


def make_heap(frquency):
    # make priority queue
    for key in frquency:
        node = HeapNode(key, frquency[key])
        heapq.heappush(heap, node)
    pass


def merge_codes():
    # build huffman tree save root node in heap
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HeapNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)


def make_codes():
    # make codes for character
    root = heapq.heappop(heap)
    make_codes_rec(root, "")


def make_codes_rec(node, current_code):
    if node is None:
        return
    if node.char is not None:
        # if leaf node code is "" , set it to either 1 or 0
        if current_code == "":
            current_code = "0"
        codes[node.char] = current_code
        reverse_codes[current_code] = node.char
    make_codes_rec(node.left, current_code + "0")
    make_codes_rec(node.right, current_code + "1")


def get_encoded_text(data):
    encoded_txt = ""
    for char in data:
        encoded_txt += codes[char]
    return encoded_txt


def huffman_decoding(data, tree):
    # decode char value
    current_code = ""
    decoded_txt = ""
    for bit in data:
        current_code += bit
        if current_code in reverse_codes:
            decoded_txt += reverse_codes[current_code]
            current_code = ""
    return decoded_txt


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    second_test_case = ""

    print("The size of the data is: {}\n".format(sys.getsizeof(second_test_case)))
    print("The content of the data is: {}\n".format(second_test_case))
    encoded_data, tree = huffman_encoding(second_test_case)

    third_testcase = "dddddd"

    print("The size of the data is: {}\n".format(sys.getsizeof(third_testcase)))
    print("The content of the data is: {}\n".format(third_testcase))
    encoded_data, tree = huffman_encoding(third_testcase)
    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
