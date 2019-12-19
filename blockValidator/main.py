from bitcoin.rpc import RawProxy
import binascii
import hashlib

p = RawProxy()


def to_little_endian(hexstring):
    ba = bytearray.fromhex(hexstring)
    ba.reverse()
    s = ''.join(format(x, '02x') for x in ba)
    return s


def hex_block_header(block_header):
    header_hex: str = ""
    header_hex += to_little_endian(block_header['versionHex'])
    header_hex += to_little_endian(block_header['previousblockhash'])
    header_hex += to_little_endian(block_header['merkleroot'])
    header_hex += to_little_endian(format(int(block_header['time']), 'x'))
    header_hex += to_little_endian(block_header['bits'])
    header_hex += to_little_endian(format(int(block_header['nonce']), 'x'))
    return header_hex


def check_block_validity(block_number):
    block_hash = p.getblockhash(block_number)

    if block_hash is None:
        print('Block was not found aborting')
        return

    block_header = p.getblockheader(block_hash)

    hexed_block_header = hex_block_header(block_header)

    unhexed_header = binascii.unhexlify(hexed_block_header)

    hashed_result = hashlib.sha256(hashlib.sha256(unhexed_header).digest()).hexdigest()

    return to_little_endian(hashed_result) == block_hash


def main():
    block_number = int(input("Enter the block number: "))
    is_valid = check_block_validity(block_number)

    if is_valid:
        print("Block is valid")
    else:
        print("Block is invalid")
    return


if __name__ == '__main__':
    main()
