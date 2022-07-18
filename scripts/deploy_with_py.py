from starknet_py.net.gateway_client import GatewayClient
from starknet_py.contract import Contract
from pathlib import Path
from starknet_py.net.networks import TESTNET
from helpful_scripts import string_to_integer
from nft_data import NFT_DATA

client = GatewayClient(TESTNET)

directoy = "../contracts/"


def get_nft_data(nft_data: dict, _index):
    name = string_to_integer(nft_data["NAME"][_index])
    symbol = string_to_integer(nft_data["SYMBOL"][_index])
    owner_address = nft_data["OWNER_ADDRESS"]

    return [name, symbol, owner_address]


def deploy_and_mint_erc721():


    for _index, _ in enumerate(NFT_DATA["NAME"]):\

        constructor_args = get_nft_data(NFT_DATA, _index)
        # list with filepaths - useful for multiple files
        deployment_result = await Contract.deploy(
            client,
            compilation_source=[Path("../contracts/", "contract.cairo")],
            constructor_args=constructor_args,
        )

        await deployment_result.wait_for_acceptance()

        contract = deployment_result.deployed_contract
        
        token_id = 1
        for _, minter_address in enumerate(NFT_DATA["MINT_ADDRESSES"]):
            invocation = await contract.functions["mint"].invoke(minter_address, token_id, max_fee=int(1e16))
            token_id += 1

    print("Contracts deployed and minted")



