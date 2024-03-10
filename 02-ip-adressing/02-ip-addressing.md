# IP Addressing
- IP addressing is the mechanism that assigns a unique identifier to each device on a network
- These addresses are used to route traffic across the Internet and within local networks
- Two versions of the Internet Protocol in use today: IPv4 and IPv6

## IPv4
- IPv4 addresses are 32-bit numbers, typically represented in dot-decimal notation
- Each byte of the address is represented by its decimal value and separated by dots
   - Example 192.168.1.1

### IPv4 Structure and Addressing
#### Address classes
- IPv4 initially used class-based addressing
- Classes A, B, C, D, and E, with each class having a different range of addresses and serving different purposes
- Largely been replaced by CIDR (Classless Inter-Domain Routing) to improve address allocation efficiency

#### CIDR Notation
- Allows for flexible allocation of IP addresses
- Indicates the prefix length
  - Shows how many bits are used for the network portion of the address
- Example:
  - 192.168.0.0/24 represents a network with 256 possible addresses (including network and broadcast addresses)
  - The first 24 bits (192.168.0) are the network part
  - The last 8 bits are the host part (host values 1 to 254)

### Dynamic and Static Addressing
#### Static IP Addressing
- Some devices, like servers, require a fixed IP address (static IP) to ensure they are always reachable at the same address
#### Dynamic IP Addressing
- Most devices use dynamic IP addressing
- A DHCP server dynamically assigns an IP address from a pool of available addresse

### Public and Private IP Addresses
#### Public IP Addresses
-  Unique across the internet
- Allows devices to communicate globally
- ISPs allocate these addresses to customers
#### Private IP Addresses
- Used within private networks and not routable on the internet
- Common ranges
  - 192.168.x.x
  - 10.x.x.x
  - 172.31.x.x

### Benefits of IPv4
- Historic widespread use
- Network admin familiarity 

### Pitfalls of IPc4
- Address exhausion 
  - How many IPv4 addresses are there?
    A: 2^32 = 4,294,967,296
  - Why haven't we run out?
    A: Can hide behind local networks
- Complexity in large networks
  - NAT and private IP addresses can complicate routing and network configuration

## Network Address Translation (NAT)
## CIDR Notation
## Subnets
## IPv6
## IP Routing
##  Dynamic Host Configuration Protocol (DHCP)
## Demo: Python / C
