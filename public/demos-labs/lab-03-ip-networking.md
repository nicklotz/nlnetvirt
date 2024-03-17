# Lab 03: Calculating and Simulating IP Networking

## A. Create Python IP network simulator

1. Create a file called ipdemo.py.

```
touch ipdemo.py
```

2. Open ipdemo.py and paste the following code.

```python
#!/usr/bin/env python3

import ipaddress
import argparse 

def calculate_network_and_broadcast(ip_cidr):
    network = ipaddress.ip_network(ip_cidr, strict=False)
    return network.network_address, network.broadcast_address

def divide_into_subnets(ip_cidr, new_prefix):
    network = ipaddress.ip_network(ip_cidr, strict=False)
    return list(network.subnets(new_prefix=new_prefix))

def generate_ipv6_address(subnet_ipv6):
    ipv6_network = ipaddress.ip_network(subnet_ipv6)
    for ip in ipv6_network.hosts():
        return ip

routing_table = {
    '192.168.1.0/24': 'Router1',
    '192.168.2.0/24': 'Router2',
    '10.0.0.0/8': 'Router3',
}

def find_next_hop(ip_address):
    for network, next_hop in routing_table.items():
        if ipaddress.ip_address(ip_address) in ipaddress.ip_network(network):
            return next_hop
    return "No route found"

nat_table = {
    '192.168.1.10': '203.0.113.5'
}

def simulate_nat(internal_ip):
    return nat_table.get(internal_ip, "No NAT mapping found")

dhcp_pool = ['192.168.1.100', '192.168.1.101', '192.168.1.102']
assigned_ips = {}

def dhcp_assign_ip(client_id):
    if client_id not in assigned_ips:
        assigned_ips[client_id] = dhcp_pool.pop(0)
    return assigned_ips[client_id]

def main():
    parser = argparse.ArgumentParser(description="Network Concepts Demonstrator")
    subparsers = parser.add_subparsers(dest='command')
    cidr_parser = subparsers.add_parser('cidr', help='Calculate network and broadcast addresses from CIDR')
    cidr_parser.add_argument('ip_cidr', type=str, help='IP address in CIDR notation (e.g., 192.168.1.0/24)')
    subnet_parser = subparsers.add_parser('subnets', help='Divide a network into subnets')
    subnet_parser.add_argument('ip_cidr', type=str, help='IP address in CIDR notation (e.g., 192.168.1.0/24)')
    subnet_parser.add_argument('new_prefix', type=int, help='New prefix length for subnets')
    ipv6_parser = subparsers.add_parser('ipv6', help='Generate an IPv6 address in a subnet')
    ipv6_parser.add_argument('subnet_ipv6', type=str, help='IPv6 subnet (e.g., 2001:db8::/64)')
    route_parser = subparsers.add_parser('route', help='Find the next hop for an IP address')
    route_parser.add_argument('ip_address', type=str, help='Destination IP address')
    nat_parser = subparsers.add_parser('nat', help='Simulate NAT for an internal IP address')
    nat_parser.add_argument('internal_ip', type=str, help='Internal IP address')
    dhcp_parser = subparsers.add_parser('dhcp', help='Simulate DHCP IP assignment')
    dhcp_parser.add_argument('client_id', type=str, help='Client identifier')
    args = parser.parse_args()

    if args.command == 'cidr':
        network_address, broadcast_address = calculate_network_and_broadcast(args.ip_cidr)
        print(f"Network Address: {network_address}, Broadcast Address: {broadcast_address}")
    elif args.command == 'subnets':
        subnets = divide_into_subnets(args.ip_cidr, args.new_prefix)
        for subnet in subnets:
            print(subnet)
    elif args.command == 'ipv6':
        ipv6_address = generate_ipv6_address(args.subnet_ipv6)
        print(f"Generated IPv6 Address: {ipv6_address}")
    elif args.command == 'route':
        next_hop = find_next_hop(args.ip_address)
        print(f"Next Hop for {args.ip_address}: {next_hop}")
    elif args.command == 'nat':
        external_ip = simulate_nat(args.internal_ip)
        print(f"External IP for {args.internal_ip}: {external_ip}")
    elif args.command == 'dhcp':
        assigned_ip = dhcp_assign_ip(args.client_id)
        print(f"Assigned IP for {args.client_id}: {assigned_ip}")
    else:
        # If no command is selected, print the help message
        parser.print_help()

if __name__ == "__main__":
    main()
```

3. Save and close ipdemo.py.

4. Make the program executable.

```
chmod +x ipdemo.py
```

5. Learn about the program's arguments and usage.

```
./ipdemo.py --help
```

## B. Find network and host addresses from CIDR blocks

1. List the usage for ipdemo's **cidr** function.

```
./ipdemo.py cidr --help
```

2. Find the network and host addresses for 192.168.100.14 when the subnet mask is 255.255.255.0.

```
./ipdemo.py cidr 192.168.100.14/24
```

3. Now increase the subnet mask in the CIDR notation. How have the network and host addresses changed? Why?

```
./ipdemo.py cidr 192.168.100.14/26
```

4. Now decrease the subnet mask in the CIDR notation. How have the network and host addresses changed? Why?

```
./ipdemo.py cidr 192.168.100.14/22
```

## C. Divide a network into subnets

1. Consider the network **10.0.0.0/8**. How many hosts can the network currently support?

2. Divide the network into smaller subnets with a new mask of 16 bits. How many subnets can we see the original network divided into? How many hosts can each subnet support?

```
./ipdemo.py subnets 10.0.0.0/8 16
```

3. Divide one of the smaller subnets into smalle subnets by changing *its* mask to 24 bits. How many subnets does that network support? How many hosts can each of *its* subnets support?

```
./ipdemo.py subnets 10.1.0.0/16 24
```

4. How many smaller subnets can we divide 10.0.0.0/8 into if we divide into subnets we a new mask length of 24 bits? How many hosts can each subnet hold? (Hint: `./ipdemo.py subnets 10.0.0.0/8 24`.

## D. Generate an IPv6 addresses within a subnet

1. Generate an IPv6 address from the 123:abcd:456::/64 network.

```
./ipdemo.py ipv6 123:abcd:456::/64
```

2. Change the subnet mask to 32 bits. What error, if any, is shown and why?

```
./ipdemo.py ipv6 123:abcd:456::/32
``

3. If you modify the input so that the network if 123:abcd::/32, would you stil get an error? Why or why not?

```
./ipdemo.py ipv6 123:abcd::/32
```

4. What if you changed *that* netowrk's subnet mask to 24 bits?

```
./ipdemo.py ipv6 123:abcd::/24
```

5. What would you expect if you set the suffix to 128? Does the output confirm?

```
./ipdemo.py ipv6 123:abcd::/128
```

## E. Find the next hop for an IP address

1. Determine the next hop for the IP address **192.168.1.10**.

```
./ipdemo.py route 192.168.1.10
``

2. Determine the next hop for the IP address **10.100.4.50**.

```
./ipdemo.py route 10.100.4.50
```

3. Determine the next hop for the IP address **192.168.3.15**. What does the output show?

```
./ipdemo.py route 192.168.3.15
```

4. Open ipdemo.py. What code in the program determines the next hop? Why did you get the output you received in step E.3?

```
cat ipdemo.py
```

5. What can you modify in ipdemo.py so that step E.3 gives you a next hop? There may be more than one answer. Feel free to ask a classmate or you instructor for assistance. 

6. Run the command again after modifying ipdemo.py.

```
./ipdemo.py route 192.168.3.15
```

## F. Network address translation

1. Find the external IP, if any, for the internal IP address 192.168.1.10.

```
./ipdemo.py nat 192.168.1.10
```

2. Find the external IP, if any, for the internal IP address 192.168.1.11.

```
./ipdemo.py nat 192.168.1.11
```

3. Open ipdemo.py. What code determines the NAT rules and command output?

```
cat ipdemo.py
```

4. **CHALLENGE:** How can you modify ipdemo.py so that 192.168.1.11 also translates to the external IP 203.0.113.5? What about any host on the 192.168.1.0/24 network? Feel free to work together with a classmate on this!

## G. DHCP IP assignment

1. Assign an IP address to the host **client123**.

```
./ipdemo.py dhcp client123
```

2. Assign an IP address to the host **client456**. Is the output what you expected?

```
./ipdemo.py dhcp client456
```

3. Open ipdemo.py. What logic in the program determines DHCP IP assignment? Think about how the script behaves when you run it. What would need to be changed or added in the program so that DHCP with multiple clients behaves in the way you'd expect?
