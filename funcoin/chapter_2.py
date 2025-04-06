
# imports the sha256 hashing function from the hashlib library which is included with Python. 
# sha256 is one of the most popular hashing functions (it’s used extensively in Bitcoin).
from hashlib import sha256

# Hash functions expect bytes as input: the encode() method turns strings to bytes
# notice the even slight differences in the inputs
input1 = b"backpack"
input2 = b"Backpack"
input3 = b"BACKPACK"
input4 = b"backPACK"
input5 = b"back pack"
input6 = b"supercalifragilisticexpialidocious"

# Use 256-bit SHA-256 hash function on the inputs
output1 = sha256(input1)
output2 = sha256(input2)
output3 = sha256(input3)
output4 = sha256(input4)
output5 = sha256(input5)
output6 = sha256(input6)

# Output the digest in hex with hexdigest() because it's easier to read
print(output1.hexdigest())  # 5f00368a6ad231c3c439c4f6bc33c27014b4d35a904ff1656d74f9528636f496
print(output2.hexdigest())  # 5118f76d9067edc593d6946b88693cefa6604c7e613111193db118166d4af589
print(output3.hexdigest())  # a5fdb33bbcdcdff9700e02abe71ae3cdc41e604d743be030f6d4797b54653752
print(output4.hexdigest())  # 5a054570918b72560f134ed4c6250c92a0f68f92085f75beb50782cbfe6943ba
print(output5.hexdigest())  # 7db3fb3378a7fc4b81b065f1ad215666046badb3b335624ddf8d8de1650eba23
print(output6.hexdigest())  # c1111e162eb6d424f42b1b970b98780963ee494bac8ae1f3ad2ef42f426ab3cc

# Typically, hash functions are considered cryptographic if they satisfy the following properties:
# - Deterministic: The same input always yields the same hash.
# - Intractability: It’s infeasible to find the input for a given hash except by exhaustion.
# - Collision-safety: It’s infeasible to find two different inputs which output the same hash.
# - Avalanche effect: The smallest change in input should yield a hash so different that the new hash appears uncorrelated with the old hash.
# - Speed: It’s computationally fast to generate a hash.

# Note: Peer-to-peer blockchains make their choice of hash function known in their protocols: 
# Bitcoin uses double sha256, while Ethereum uses keccak256. The important thing to know is 
# that all of these hash functions do the same thing: they provide predictable output for a 
# given input.

# Termininology:
# - Hash: The function that takes an input and produces a fixed-size string of bytes.
# - Digest: The output of the hash function.
