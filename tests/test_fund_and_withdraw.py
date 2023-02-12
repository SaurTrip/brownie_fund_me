
import pytest
from scripts.helper_scripts import get_account,LOCAL_DEVELOPMENT_ENVIRONMENTS
from scripts.deploy import deploy_fundMe
from brownie import FundMe,network,accounts,exceptions


def testFund():
    account = get_account()
    fund_me_contract = deploy_fundMe()
    entranceFee = fund_me_contract.getEntranceFee() + 100
    #  100 is added so that to make amount that in case if we have less amount
    tx1 = fund_me_contract.fund({"from":account,"value":entranceFee})
    tx1.wait(1)
    assert fund_me_contract.addressToAmountFunded(account.address) == entranceFee


def testWithdraw():
    account = get_account()
    fund_me_contract = deploy_fundMe()
    entranceFee = fund_me_contract.getEntranceFee() + 100
    tx2 = fund_me_contract.withdraw({"from":account})
    tx2.wait(1)
    assert fund_me_contract.addressToAmountFunded(account.address) == 0

# def test_only_owner_can_withdraw():
#     if (network.show_active() not in LOCAL_DEVELOPMENT_ENVIRONMENTS):
#         pytest.skip("only for local testing!")
#     fund_me = deploy_fundMe()
#     badActor = accounts.add()
#     with pytest.raises(exceptions.VirtualMachineError):
#         fund_me.withdraw({"from":badActor})













