// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank {
    // Mapping of each user's address to their account balance
    mapping(address => uint) public balances;

    // Deposit Ether into your account
    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    // Withdraw specified Ether amount from your account
    function withdraw(uint _amount) public {
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        balances[msg.sender] -= _amount;

        // Transfer the Ether back to the sender
        (bool sent, ) = msg.sender.call{value: _amount}("");
        require(sent, "Transaction failed");
    }

    // Get the total Ether balance stored in the contract
    function getContractBalance() public view returns (uint) {
        return address(this).balance;
    }

    // Get your personal account balance
    function getMyBalance() public view returns (uint) {
        return balances[msg.sender];
    }
}
