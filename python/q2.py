import secrets
from coincurve import PublicKey
from eth_hash.auto import keccak

# Private Key
private_key_bytes = secrets.token_bytes(32)
print("Private Key: " + private_key_bytes.hex())

# 検証用
# private_key_hex_str = "118c8fdb82d0938eaf494e737365bc8c45fb4af1784c5ef9f860b8c9b6e0654f"
# private_key_bytes = bytes.fromhex("118c8fdb82d0938eaf494e737365bc8c45fb4af1784c5ef9f860b8c9b6e0654f")
# print("Private Key: 118c8fdb82d0938eaf494e737365bc8c45fb4af1784c5ef9f860b8c9b6e0654f")

# Public Key
public_key = PublicKey.from_valid_secret(private_key_bytes).format(compressed=False)[1:]
print("Public Key: "+public_key.hex())

# Ethereum Address
print("Ethereum Address: 0x"+keccak(public_key).hex()[-40:])
