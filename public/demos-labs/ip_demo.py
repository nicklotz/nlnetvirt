# Import necessary libraries
import ipaddress  # For handling IP addresses and networks
import argparse  # For parsing command line arguments

# Function to calculate network and broadcast addresses from an IP in CIDR notation
def calculate_network_and_broadcast(ip_cidr):
    # ipaddress.ip_network creates an IPv4 or IPv6 network object from the provided CIDR notation
    network = ipaddress.ip_network(ip_cidr, strict=False)
    # Returns the network and broadcast addresses of the given network
    return network.network_address, network.broadcast_address

# Function to divide a given network (in CIDR notation) into subnets
def divide_into_subnets(ip_cidr, new_prefix):
    # Convert the CIDR notation into a network object
    network = ipaddress.ip_network(ip_cidr, strict=False)
    # Returns a list of subnet objects, split based on the new prefix length provided
    return list(network.subnets(new_prefix=new_prefix))

# Function to generate an IPv6 address within a specified subnet
def generate_ipv6_address(subnet_ipv6):
    # Create an IPv6 network object from the provided subnet
    ipv6_network = ipaddress.ip_network(subnet_ipv6)
    # Iterate through the hosts in the network and return the first one
    # This is a simple way to generate a valid IPv6 address within the subnet
    for ip in ipv6_network.hosts():
        return ip

# Define a simple routing table as a dictionary
# This maps network CIDR notations to their respective next-hop identifiers (e.g., router names)
routing_table = {
    '192.168.1.0/24': 'Router1',
    '192.168.2.0/24': 'Router2',
    '10.0.0.0/8': 'Router3',
}

# Function to find the next hop for a given IP address based on the routing table
def find_next_hop(ip_address):
    # Iterate through the routing table
    for network, next_hop in routing_table.items():
        # Check if the given IP address belongs to the current network
        if ipaddress.ip_address(ip_address) in ipaddress.ip_network(network):
            # If it does, return the associated next hop
            return next_hop
    # If no matching network is found, indicate that no route is found
    return "No route found"

# NAT table mapping internal IP addresses to external ones
nat_table = {
    '192.168.1.10': '203.0.113.5'
}

# Function to simulate Network Address Translation (NAT) for an internal IP
def simulate_nat(internal_ip):
    # Return the external IP mapped to the given internal IP, if any
    return nat_table.get(internal_ip, "No NAT mapping found")

# Pool of IP addresses available for DHCP to assign
dhcp_pool = ['192.168.1.100', '192.168.1.101', '192.168.1.102']
# Dictionary to keep track of IP addresses assigned to client IDs
assigned_ips = {}

# Function to simulate DHCP assigning IP addresses to clients
def dhcp_assign_ip(client_id):
    # Check if the client already has an assigned IP
    if client_id not in assigned_ips:
        # If not, assign the first available IP from the pool and remove it from the pool
        assigned_ips[client_id] = dhcp_pool.pop(0)
    # Return the IP address assigned to the client
    return assigned_ips[client_id]

# Main function to parse command-line arguments and invoke the appropriate functions
def main():
    # Create an argument parser object
    parser = argparse.ArgumentParser(description="Network Concepts Demonstrator")
    # Add subparsers for each network concept demonstration
    subparsers = parser.add_subparsers(dest='command')

    # Each subparser corresponds to a different network concept or operation
    # For CIDR notation calculation
    cidr_parser = subparsers.add_parser('cidr', help='Calculate network and broadcast addresses from CIDR')
    cidr_parser.add_argument('ip_cidr', type=str, help='IP address in CIDR notation (e.g., 192.168.1.0/24)')

    # For dividing networks into subnets
    subnet_parser = subparsers.add_parser('subnets', help='Divide a network into subnets')
    subnet_parser.add_argument('ip_cidr', type=str, help='IP address in CIDR notation (e.g., 192.168.1.0/24)')
    subnet_parser.add_argument('new_prefix', type=int, help='New prefix length for subnets')

    # For generating an IPv6 address within a subnet
    ipv6_parser = subparsers.add_parser('ipv6', help='Generate an IPv6 address in a subnet')
    ipv6_parser.add_argument('subnet_ipv6', type=str, help='IPv6 subnet (e.g., 2001:db8::/64)')

    # For finding the next hop based on the IP routing table
    route_parser = subparsers.add_parser('route', help='Find the next hop for an IP address')
    route_parser.add_argument('ip_address', type=str, help='Destination IP address')

    # For simulating NAT
    nat_parser = subparsers.add_parser('nat', help='Simulate NAT for an internal IP address')
    nat_parser.add_argument('internal_ip', type=str, help='Internal IP address')

    # For simulating DHCP IP assignment
    dhcp_parser = subparsers.add_parser('dhcp', help='Simulate DHCP IP assignment')
    dhcp_parser.add_argument('client_id', type=str, help='Client identifier')

    # Parse the arguments provided by the user
    args = parser.parse_args()

    # Based on the command selected by the user, call the appropriate function and print its output
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

# Ensure that the script can be run directly
if __name__ == "__main__":
    main()

