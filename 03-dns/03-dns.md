# Domain Name System (DNS)
- Translates human-readable domain names (like www.example.com) into machine-readable IP addresses (such as 192.0.2.1 for IPv4 or 2001:db8::2:1 for IPv6)
- Vital because while domain names are easy for people to remember, computers and networks rely on IP addresses to route traffic to the correct destination

## Understanding DNS
- The "phonebook" of the internet
- When a user wants to access a website, their device makes a DNS query to resolve the site's domain name into an IP address
- The device then uses to establish a connection to the website's serve

## How DNS Works
### DNS Recursor
- Process starts when a client device queries a DNS recursor, often provided by the internet service provider (ISP)
- Designed to receive queries from client machines and act on their behalf to track down the IP address of the domain
### Root Nameserver
- The recursor queries a root nameserver
- Root nameserver responds with the address of a Top-Level Domain (TLD) nameserver (such as .com, .net, or .org)
### TLD Nameserver
- Recursor then queries the TLD nameserver
- TLD nameserver responds with the IP address of the requested domain
### Response Back to Client
- DNS recursor sends the IP address back to the client
- Allows the client to connect directly to the server hosting the domain

## Components of DNS
### DNS Records
- Instructions that live in authoritative DNS servers
- Provide information about a domain
  - IP addresses (A records for IPv4, AAAA records for IPv6)
  - Mail servers (MX records)
  - Other services such as SRV records
### Caching
- DNS data is cached at various levels of the DNS hierarchy as well as in web browsers and operating systems
- Reduces DNS query times

## Importance of DNS to Network Virtualization
- Not just in userspace, crucial to background infra automation
  - Scaling
  - Load balancing
  - High availability
  - Disaster recovery

## DNS Security
- DNS faces various security threats
  - Includes DNS spoofing or cache poisoning, where attackers redirect traffic to malicious sites
- DNS Security Extensions (DNSSEC)
  - Provide authentication for DNS responses
  - Helps ensure the integrity and authenticity of the data

## Live Demo: Namecheap or Route53


