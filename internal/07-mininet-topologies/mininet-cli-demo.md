# Mininet CLI examples
## General actions
- List All Nodes: `nodes`
- Ping All Hosts: `pingall`
- Dump Information about All Nodes: `dump`
- Test Network Connectivity: `pingall`
- Test Bandwidth between Two Hosts: `iperf`

# Individual nodes
- Host Commands: `h1 ifconfig, h1 ping h2`
- Switch Commands: `sh ovs-ofctl dump-flows s1`
- Controller Commands: For the default controller, there's usually not much to do from the CLI, but custom controllers can have their own set of commands.
