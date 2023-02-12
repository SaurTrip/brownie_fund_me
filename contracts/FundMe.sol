// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";


contract FundMe{




address public owner;
mapping(address=>uint256) public addressToAmountFunded;
address[] public funders;
AggregatorV3Interface public priceFeed;

uint256 public version;

    constructor (address _priceFeedAddress) public {
        owner = msg.sender;
        // priceFeed = AggregatorV3Interface(0xD4a33860578De61DBAbDc8BFdb98FD742fA7028e);
        priceFeed = AggregatorV3Interface(_priceFeedAddress);
    }




function fund() public payable {

    uint256 minimumFundUSD = 50 * 10 ** 18;

    require(getConversionRate(msg.value) >= minimumFundUSD,"You need to spend more eth!");

    addressToAmountFunded[msg.sender] += msg.value;
    funders.push(msg.sender);

}

function getEntranceFee() public view returns (uint256){
    // minimum usd
        uint256 minimumFundUSD = 50 * 10 ** 18;
        uint256 price = uint256(getLatestPrice());
        uint256 precision = 1 * 10 ** 18;
        return (minimumFundUSD * precision) / price;
}

function getVersion() external  returns (uint256){
    //  AggregatorV3Interface priceFeed = AggregatorV3Interface(0xD4a33860578De61DBAbDc8BFdb98FD742fA7028e);
     version =  priceFeed.version();
     return version;
}

    function getLatestPrice() public view returns (int) {
        // AggregatorV3Interface priceFeed = AggregatorV3Interface(0xD4a33860578De61DBAbDc8BFdb98FD742fA7028e);
        // prettier-ignore
        (
            /* uint80 roundID */,
            int price,
            /*uint startedAt*/,
            /*uint timeStamp*/,
            /*uint80 answeredInRound*/
        ) = priceFeed.latestRoundData();
        
        return price * 10000000000;
    }

    function getConversionRate(uint256 ethAmount) public view returns(uint256)
    {

        //163284000000000000000
        uint256 ethPriceInUSD = ethAmount * uint256(getLatestPrice()) / 10 ** 18;

        return ethPriceInUSD;

        // .000001631600000000

    }

    modifier onlyOwner{
        require(msg.sender == owner,"Only the owner of contract can withdraw the fund!");
        _;
    }

    function withdraw()  payable  onlyOwner public {
        
        payable(msg.sender).transfer(address(this).balance);

        for(uint256 funderIndex = 0 ; funderIndex < funders.length; funderIndex++){
            address funder = funders[funderIndex];
            addressToAmountFunded[funder] = 0;

        }

        funders = new address[](0);


    }

}