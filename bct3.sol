// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BankAccount {
    mapping(address => uint) private balances;

    event Deposit(address indexed accountHolder, uint amount);
    event Withdraw(address indexed accountHolder, uint amount);

    function deposit() public payable {
        require(msg.value > 0, "Send some Ether to deposit.");
        balances[msg.sender] += msg.value;
        emit Deposit(msg.sender, msg.value);
    }

    function withdraw(uint amount) public {
        require(amount > 0 && amount <= balances[msg.sender], "Invalid withdrawal amount.");
        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
        emit Withdraw(msg.sender, amount);
    }

    function checkBalance() public view returns (uint) {
        return balances[msg.sender];
    }
}