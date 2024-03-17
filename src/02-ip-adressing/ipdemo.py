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

