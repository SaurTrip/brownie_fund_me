from brownie import config,FundMe,MockV3Aggregator,accounts,network
from scripts.helper_scripts import get_account

def fund():
    account = get_account()
    fund_me_contract = FundMe[-1]
    entranceFee = fund_me_contract.getEntranceFee()
    fund_me_contract.fund({"from":account,"value":entranceFee})

def withdraw():
    account = get_account()
    fund_me_contract = FundMe[-1]
    entranceFee = fund_me_contract.getEntranceFee()
    fund_me_contract.withdraw({"from":account})

        


    # print(entranceFee)
    # print(len(FundMe))


def main():
    fund()
    withdraw()