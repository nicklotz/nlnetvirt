# Mininet Topologies
- Mininet is a network emulator
- Topologies are the arrangement of network elements (nodes) and the connections between them (links)
- Topologies in Mininet are defined programmatically using Python
- Allows for complex network structures to be generated dynamically
## Common predefined topologies
### Linear
- Straight-line sequence of switches connected to a specified number of hosts
- Simple topology is useful for basic testing and experiments
### Tree
- Hierarchical structure with a root switch connected to multiple switches and hosts, forming a tree-like structure
- Depth and fanout can be customized
### Single
- Single switch connected to multiple hosts
- Useful for scenarios where a simple LAN setup is required
### Custom
- Users can define their own topologies by extending Mininet's Topo class in Python
- Can specify exactly how many switches, hosts, and links there are and how they're connected

## CLI Options
### Starting Mininet
- For example, `sudo mn --topo linear,3` would create a linear topology with three switches
### Custom scripts
- Can write a Python script that defines the topology 
- Then start Mininet using `sudo mn --custom <script.py> --topo <topology_name>`
### Interacting with hosts
#### Ping
- `h1 ping h2`
#### IP configuration
- `h1 ifconfig`
#### Executing commands on host
- `h1 ls /`
### Interacting with switches
#### Checking the Switch Ports
- `sh ovs-ofctl show s1` displays the ports and their details on switch s1
#### Dumping the flow table
- To view table entries, `sh ovs-ofctl dump-flows s1`
### CLI options for network inspection and management
- **nodes**: Lists all nodes in the network (hosts, switches, and controllers).
- **net**: Displays the network configuration, showing the links between nodes.
- **dump**: Provides detailed information about all network elements, including their IP addresses, MAC addresses, and associated interfaces
- **links**: Lists the active links between nodes, useful for verifying the network topology's connectivity

## Generating complicated topologies
- Mininet allows users to write Python scripts that leverage the Mininet API
- Involves creating instances of network topology class (Topo) and adding nodes (hosts, switches) and links with specific parameters
- After defining the topology, the script then creates an instance of the Mininet class
  - Passes the topology as an argument
  - Optionally specifies the controller and switch types
### Example
- Define your topology class that inherits from Topo
- Use methods like addHost(), addSwitch(), and addLink() to build your network

### Demo: Interacting with Python


