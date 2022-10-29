import json

from eth_utils import keccak

# トランザクションデータを読み込む
transactionFile = json.load(open('transactions.json', "r"))

# トランザクションを変数に格納
tx1 = transactionFile["transactions"][0]
tx2 = transactionFile["transactions"][1]
tx3 = transactionFile["transactions"][2]
tx4 = transactionFile["transactions"][3]

# トランザクションのハッシュ値を計算
tx1_hash_bytes = keccak(json.dumps(tx1, separators=(',', ':')).encode('utf-8'))
tx2_hash_bytes = keccak(json.dumps(tx2, separators=(',', ':')).encode('utf-8'))
tx3_hash_bytes = keccak(json.dumps(tx3, separators=(',', ':')).encode('utf-8'))
tx4_hash_bytes = keccak(json.dumps(tx4, separators=(',', ':')).encode('utf-8'))
print("tx1_hash: " + tx1_hash_bytes.hex())
print("tx2_hash: " + tx2_hash_bytes.hex())
print("tx3_hash: " + tx3_hash_bytes.hex())
print("tx4_hash: " + tx4_hash_bytes.hex())

# トランザクションのハッシュ値を結合
node_tx1_tx2_hash_bytes = keccak(tx1_hash_bytes + tx2_hash_bytes)
node_tx3_tx4_hash_bytes = keccak(tx3_hash_bytes + tx4_hash_bytes)
print("node_tx1_tx2_hash: " + node_tx1_tx2_hash_bytes.hex())
print("node_tx3_tx4_hash: " + node_tx3_tx4_hash_bytes.hex())

# ルートハッシュを計算
markle_root_hash_bytes = keccak(node_tx1_tx2_hash_bytes + node_tx3_tx4_hash_bytes)
print("Markle Root Hash: " + markle_root_hash_bytes.hex())