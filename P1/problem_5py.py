import hashlib


class Node:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = calc_hash(data)


def calc_hash(data):
    sha = hashlib.sha256()
    hash_str = data.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()


class Block:

    def __init__(self, timestamp=0, data="", previous_hash=0):
        self.chain = []
        self.timestamp = timestamp
        self.data = data
        self.hash = calc_hash(data)
        self.previous_hash = previous_hash
        if timestamp and data and previous_hash:
            self.chain.append(Node(timestamp, data, previous_hash))

    def append(self, timestamp, data):
        self.chain.append(Node(timestamp, data, self.hash))


block = Block("t0", "0", 0)
block.append("t1", "1", )
block.append("t2", "2", )
block.append("t3", "3kdf skf skdfsd", )

block1 = Block("t0", "0", 0)
block1.append("t1", "1", )
block1.append("t1", "2", )
block1.append("t1", "3kdf skf skdfsd", )

block2 = Block()

for item in block.chain:
    print(item.data, item.hash, item.previous_hash)

for item in block1.chain:
    print(item.data, item.hash, item.previous_hash)

for item in block2.chain:
    print(item.data, item.hash, item.previous_hash)
