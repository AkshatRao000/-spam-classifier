from web3 import Web3

# Ganache Local Blockchain
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Your contract ABI & Address
contract_address = '0xYourContractAddress'
contract_abi = [...]  # paste ABI here

# Contract Instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Account to send transaction
sender = '0xYourAccount'
private_key = 'your_private_key'

# Simulated location data
latitude = "26.8500"
longitude = "80.949997"

# Build transaction
nonce = web3.eth.get_transaction_count(sender)
txn = contract.functions.addLocation(latitude, longitude).build_transaction({
    'chainId': 1337,  # Ganache's chain ID
    'gas': 2000000,
    'gasPrice': web3.to_wei('50', 'gwei'),
    'nonce': nonce
})

# Sign & send transaction
signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)
txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
print("Transaction sent! Hash:", txn_hash.hex())
