from bitcoin.rpc import RawProxy

# Create a connection to local Bitcoin Core node
p = RawProxy()


def calculate_utxo(in_val):
    index = in_val['vout']
    transaction_id = in_val['txid']
    raw_transaction = p.getrawtransaction(transaction_id)
    decoded_tx = p.decoderawtransaction(raw_transaction)
    outputs = decoded_tx['vout']
    return outputs[index]['value']


def calculate_transaction_fee(transaction_id):
    transaction_in_val = 0
    transaction_out_val = 0
    try:
        raw_transaction = p.getrawtransaction(transaction_id)
    except Exception as e:
        print("Could not get transaction data")
        return
    decoded_transaction = p.decoderawtransaction(raw_transaction)
    trans_vin = decoded_transaction['vin']
    trans_out = decoded_transaction['vout']
    for in_val in trans_vin:
        transaction_in_val += calculate_utxo(in_val)
    for out_val in trans_out:
        transaction_out_val += out_val['value']
    return transaction_in_val - transaction_out_val


def main():
    transaction_id = input('Enter a transaction ID: ')
    transaction_fee = calculate_transaction_fee(transaction_id)
    print(f'Transaction fee for this transaction is: {transaction_fee} BTC')


if __name__ == '__main__':
    main()
