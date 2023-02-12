from brownie import config,FundMe,MockV3Aggregator,accounts,network
from scripts.helper_scripts import get_account,LOCAL_DEVELOPMENT_ENVIRONMENTS,deploy_mockV3,FORKED_LOCAL_ENVIRONMENTS


#  to Debug any script, use :- python3 -m pdb  <script name>
# To kill all the process running on a port first list all the process using command :- lsof -i TCP:8545, then use:- kill -9 <pid>


# By default, brownie creates the folder inside build->deployments->5(which is chain id of the network we deployed the contract)
# So it does not create the folder inside this path when we are deploying the contract to development network, such as
# ganache ui, so if we want the brownie creates the chain id folder inside this path, then run the following command from terminal
# brownie networks add Ethereum ganache-local host=http://127.0.0.1:7545 chainid=1337, this command will add the ganache-local
# network to network list,afterwards, we can deploy the contract using -: brownie run ./scripts/deploy.py --network ganache-local

def deploy_fundMe():
    #  etherscan api token for verifying smarty contract on etherscan 
    #  QB27SJYCGBWBY96PYS3NBVFXK8F3URJD3C

        account = get_account()

        if (network.show_active() not in LOCAL_DEVELOPMENT_ENVIRONMENTS):
        # eth_usd_price_feed:
            price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
        else:
            deploy_mockV3()
            price_feed_address = MockV3Aggregator[-1].address

        deploy_contract = FundMe.deploy(price_feed_address,{"from":account},publish_source=config["networks"][network.show_active()].get("verify"))
        print(f"Contract deployed to {deploy_contract.address}")
        return deploy_contract


    # print(deploy_contract.getLatestPrice())
    # print(FundMe.getConversionRate(1000000000000000000))
    # retrieved_val = deploy_contract.retrieve()
    # print(retrieved_val)
    # transaction = deploy_contract.store(8791,{"from":account})
    # transaction.wait(1)
    # updated_retrieved_val = deploy_contract.retrieve()
    # print(updated_retrieved_val)


    
def main():
    deploy_fundMe()