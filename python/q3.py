import secrets
from coincurve import PrivateKey, PublicKey
from eth_utils import keccak

private_key_bytes = secrets.token_bytes(32)
print("Private Key: " + private_key_bytes.hex())
private_key = PrivateKey(private_key_bytes)

message_byte = keccak("おがわけん".encode("utf-8"))

signature = private_key.sign(message=message_byte, hasher=None)
print("Signature: " + signature.hex())

result = PublicKey.from_secret(private_key_bytes).verify(signature, message_byte, hasher=None)
print("Result: " + str(result))