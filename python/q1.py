from eth_hash.auto import keccak
import binascii

print(binascii.hexlify(keccak("おがわけん".encode("utf-8"))))

print(binascii.hexlify(keccak("こがわけん".encode("utf-8"))))

print(binascii.hexlify(keccak("おかわけん".encode("utf-8"))))