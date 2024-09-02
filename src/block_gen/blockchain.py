import hashlib
import datetime

class Block(object): 
    def __init__(self, index, prev_hash, data):
        self.index = index

        self.prev_hash = prev_hash
        self.hash = self.calculate_hash(index, prev_hash, data, self.timestamp)

        self.data = data
        self.timestamp = datetime.datetime.now().timestamp()
        self.state = 1 # 0 - close, 1 - open, 2 - freeze

    def __str__(self):
        return str(self.hash)

    def generate_header(self, index, prev_hash, data, timestamp):
        return str(index) + prev_hash + data + str(timestamp)

    def calculate_hash(self, index, prev_hash, data, timestamp):
        header_string = self.generate_header(index, prev_hash, data, timestamp).encode('utf-8')

        sha = hashlib.sha256()
        sha.update(header_string)
        return sha.hexdigest()

    def close(self):
        self.state = 0

    def freeze(self):
        self.state = 2
