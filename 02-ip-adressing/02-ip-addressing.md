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
- NAT plays a key role in alleviating IPv4 address exhaustion 
- Allows multiple devices on a private network to share a single public IP address for internet access

### Types of NAT
#### Static NAT
- Maps one private IP address to one public IP address
- Commonly used for hosting services (like a web or mail server) on an internal network with a fixed IP address accessible from the internet
#### Dynamic NAT
- Dynamically assigns a public IP address from a pool of available addresses to a private IP address
- Less common in smaller networks but can be used in larger organizations with multiple public IP addresses
#### Port Address Translation (PAT)
- Also known as NAT overload
- Maps multiple private IP addresses to a single public IP address (or a few addresses) by differentiating the connections by source port number
- Most commonly used form of NAT
- What most home routers use to allow all family members to access the internet simultaneously
- Corporate firewalls often use a combination of static NAT for externally accessible servers and dynamic NAT or PAT for general employee internet access

### Importance to Network Virtualization
#### Virtual Networks
- Virtualized environments, such as those created with VMware, Hyper-V, or KVM, often use NAT
- Allows virtual machines (VMs) to access external networks through the host machine's single physical network interface
#### Containerization
- In containerized environments, like those managed by Docker or Kubernetes, NAT is used to route traffic to and from containers
- Allows multiple containerized applications to share the host's IP address
#### Software-defined networking
- SDN technologies leverage NAT to dynamically manage the IP addressing for applications and services running in virtualized environments
- Improves agility and efficiency in deploying and scaling services

## CIDR Notation
### Introduction to CIDR
- CIDR stands for Classless Inter-Domain Routing
- Introduced to improve the way IP addresses are allocated and to increase the efficiency of routing through aggregation
- Allows for a more flexible division of IP address space than the traditional class-based system by using subnetting
- Denoted by an IP address, followed by a slash (/) and a number (e.g., 192.168.0.0/24) 
  - The number at the end denotes the subnet mask length in bits
  - Indicates the division between the network and host portions of the address
### How CIDR works
- Allows multiple IP addresses to be represented as a single entry in a routing table through aggregation
- Achieved by combining similar IP address ranges into a single CIDR block, minimizing the number of routing paths that routers must store and manage
### Exercises/Calculations for Students
#### Exercise 1: CIDR block calculation
- Given the CIDR block 192.168.1.0/24, calculate the following:
 - The subnet mask
 - The number of usable IP addresses
 - The range of IP addresses within the block
- Answers 
  - Subnet mask: 255.255.255.0 
  - Usable IP addresses: 254 (256 total addresses minus 2 for the network and broadcast addresses)
  - Range of IP addresses: 192.168.1.1 to 192.168.1.254
#### Exercise 2: Subnetting with CIDR
- Given a requirement to create subnets each supporting at least 50 devices, determine the appropriate subnet size and CIDR notation for these subnets if you are starting with a fresh allocation. Assume you are working within the 192.168.0.0 network.
- Answer
  - We need at least 8 bits for host addresses 
    - 2^8 = 64 and 2^7 = 32, for 50 per subnet we need at least 2^8 bits
  - IP addresses are 32 bits, the host portion is 8 bits, so the subnet mask is 26 bits
  - Subnets therefore are:
    - Subnet 1: 192.168.0.0/26 
    - Subnet 2: 192.168.0.64/26
    - Subnet 3: 192.168.0.128/26
    - Subnet 4: 192.168.0.192/26
#### Exercise 3: CIDR Aggregation
- Assume you have the following IP address ranges that need to be aggregated into a single CIDR block:
  - 192.168.1.0/24
  - 192.168.2.0/24
  - 192.168.3.0/24
- All addresses use a subnet mask of 255.255.255.0. What is the smallest single CIDR block that can encompass all these addresses?- Answer:
  - We need to hold addresses from 192.168.1.0 to 192.168.3.255
  - A.k.a. 192.168.0000001.0, 192.168.00000010.0, 192.168.00000011.0,
  - That's 10 bits worth of host addresses, so the answer is 192.168.0.0/22

## Subnets
## IPv6
## IP Routing
##  Dynamic Host Configuration Protocol (DHCP)
## Demo: Python / C
