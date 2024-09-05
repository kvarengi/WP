import hashlib
import datetime
import os
import json

STATES = {
    0: "close",
    1: "open",
    2: "freeze"
}

class Block(object): 
    def __init__(self, index, prev_hash, data, hash=None, timestamp=None, state=None):
        self.index = index
        self.data = data

        if timestamp == None:
            self.timestamp = datetime.datetime.now().timestamp()
        else:
            self.timestamp = timestamp

        if state == None:
            self.state = 1
        else:
            self.state = state

        if prev_hash == None:
            sha = hashlib.sha256()
            sha.update("genesis".encode('utf-8'))
            self.prev_hash = sha.hexdigest()
        else:
            self.prev_hash = prev_hash 

        if hash == None:
            self.hash = self.calculate_hash(self.index, self.prev_hash, self.data, self.timestamp)
        else:
            self.hash = hash

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

    def self_save(self, directory):
        block_data = {
            "index": self.index,
            "data": self.data,
            "timestamp": self.timestamp,
            "state": self.state,
            "prev_hash": self.prev_hash,
            "hash": self.hash
        }

        block_name = f"block_{self.index}_{STATES[self.state]}"

        with open(f"{directory}/{block_name}.json", 'w') as out:
            json.dump(block_data, out)


class Blockchain(object):
    def __init__(self):
        self.genesis = Block(0, None, "genesis")
        self.chain = [self.genesis]
        self.current_transactions = []

    def new_block(self):
        pass

    def new_transaction(self):
        pass

    @property
    def last_block(self):
        return self.chain[-1]

    def sync(self):
        node_blocks = []
        chain_data_dir = "chain_data"
        if os.path.exists(chain_data_dir):
            for filename in os.listdir(chain_data_dir):
                if filename.endswith('.json'):
                    filepath = '%s/%s' % (chain_data_dir, filename)

                    with open(filepath, 'r') as block_file:
                        block_info = json.load(block_file)
                        block_object = Block(block_info["index"], block_info["prev_hash"],
                                             block_info["data"], block_info["hash"],
                                             block_info["timestamp"], block_info["state"])
                        node_blocks.append(block_object)

        return node_blocks

if __name__ == "__main__":
    chain = Blockchain()
    chain_data_dir = "chain_data"
    print(chain.genesis.__dict__)

    if not os.path.exists(chain_data_dir):
        os.mkdir(chain_data_dir)

    if os.listdir(chain_data_dir) == []:
        chain.genesis.self_save(chain_data_dir)
