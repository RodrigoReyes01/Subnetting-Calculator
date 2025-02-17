# Subnetting Calculator

## Description

This is a subnetting calculator designed to help users calculate the number of subnets and available hosts within a given network address. The application takes as input a network address and subnet mask and displays key information such as the number of hosts, subnets, and subnet increment.

## Features

- Calculation of the number of available hosts.
- Calculation of the number of created subnets.
- Calculation of the subnet increment.
- Intuitive interface with an input section and an output section.
- "Reset" button to clear values.

## Technologies Used

- HTML, CSS, and JavaScript: For the user interface and calculation logic.

## Formulas Used

- **Calculation of the number of hosts:**
  - Where N is the number of bits available for hosts.
  - Formula: `(2^N) - 2`
  
- **Calculation of the number of subnets:**
  - Where M is the number of bits borrowed from the host part to create subnets.
  - Formula: `2^M`
  
- **Calculation of subnet increment:**
  - Formula: `2^(number of borrowed bits)`

## How to Use

1. Enter the network address in the "Network Address" field (Example: 192.168.1.0).
2. Enter the subnet mask in the "Subnet Mask" field (Example: 255.255.255.0).
3. Click the "Calculate" button to get the results.
4. Review the calculated values in the results section.
5. To clear the values and perform a new calculation, click the "Reset" button.

## Example Usage

### Input:
- **Network Address:** 192.168.1.0
- **Subnet Mask:** 255.255.255.192

### Output:
- **Number of Hosts:** 62
- **Number of Subnets:** 4
- **Subnet Increment:** 64

## Additional Notes

- The calculator assumes that the entered address is a valid network address.
- If an invalid subnet mask is entered, the results may be incorrect.
- This tool is designed for IPv4 networks.
