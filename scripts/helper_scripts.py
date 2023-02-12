
from brownie import config,FundMe,accounts,network,MockV3Aggregator
from web3 import Web3

LOCAL_DEVELOPMENT_ENVIRONMENTS = ['development','ganache-local']
FORKED_LOCAL_ENVIRONMENTS = ['mainnet-fork','mainnet-fork-dev']
DECIMALS = 8
STARTING_PRICE = 200000000000



def get_account():
    if (network.show_active() in LOCAL_DEVELOPMENT_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
    
def deploy_mockV3():
        if len(MockV3Aggregator) <= 0:
            verify_publish_source = config["networks"][network.show_active()]["verify"]
            # mockAggregator = MockV3Aggregator.deploy(18,2000000000000000000,{"from":account},publish_source=verify_publish_source)
            mockAggregator = MockV3Aggregator.deploy(DECIMALS,Web3.toWei(STARTING_PRICE,"ether"),{"from":get_account()},publish_source=verify_publish_source)