// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentRegistry {
    // Structure to store student data
    struct Student {
        string name;
        uint256 age;
    }

    // Array to store multiple students
    Student[] private students;

    // Event to log Ether received
    event ReceivedEther(address indexed sender, uint256 value);

    // Receive function to accept Ether
    receive() external payable {
        emit ReceivedEther(msg.sender, msg.value);
    }

    // Fallback function
    fallback() external payable {
        emit ReceivedEther(msg.sender, msg.value);
    }

    // Function to add student data
    function addStudent(string memory name, uint256 age) public {
        students.push(Student(name, age));
    }

    // Function to get student by index
    function getStudent(uint256 index) public view returns (string memory, uint256) {
        require(index < students.length, "Student not found");
        return (students[index].name, students[index].age);
    }

    // Function to get total number of students
    function getStudentCount() public view returns (uint256) {
        return students.length;
    }
}
