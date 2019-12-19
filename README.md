# python-bitcoin

python-bitcoin is a simple project for testing a **python-bitcoinlib** library and its communication with Bitcoin Core.

Task is located [here](https://github.com/blockchain-group/Blockchain-technologijos/blob/master/pratybos/3uzduotis-Bitcoin-Core-API.md).

Special thanks to Augustinas Makevičius for the access to the full Bitcoin node.

# How to run the applications:

1. Clone this repository using *git clone*
2. *cd python-bitcoin/transacionFeeCalculator* **or** *cd python-bitcoin/blockValidator*
3. Compile and run **main.py** (Connection to Bitcoin Core node is required)
# Task 1: Transaction fee calculation

This simple application can calculate transaction fee for any transaction in the blockchain. 

Sample output:

```
Enter a transaction ID: 0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2
Transaction fee for this transaction is: 0.00050000 BTC

Process finished with exit code 0
```

# Task 2: Block validation

This simple application, given a block number, can check if block hash is valid, by replicating block hash generation of Bitcoin Blockchain. 

Sample output:

```
Enter the block number: 20000
20000
Block is valid

Process finished with exit code 0
```

# Changelog:

---
[v0.1](https://github.com/frix360/python-bitcoin/releases/tag/v0.1) - (2019-12-19)

- Initial commit
---

