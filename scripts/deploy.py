import subprocess

from nft_data import NFT_DATA
from helpful_scripts import string_to_integer

def deploy_erc721(nft_data: dict):

    for _index, element in enumerate(nft_data["NAME"]):
        name = string_to_integer(nft_data["NAME"][_index])
        symbol = string_to_integer(nft_data["SYMBOL"][_index])
        owner_address = nft_data["OWNER_ADDRESS"]
    
        print(subprocess.check_output(['nile', 'deploy', 'ERC721', str(name), str(symbol), owner_address, '--network', 'localhost']))

    print("NFTs deployed 🚀!")
    
if __name__ == '__main__':
    deploy_erc721(NFT_DATA)