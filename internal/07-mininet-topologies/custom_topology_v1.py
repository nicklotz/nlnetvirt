# Import necessary libraries and classes
import argparse
from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

def create_network():
    """
    Initialize and return a Mininet network object with the specified controller and switch types.
    """
    return Mininet(controller=Controller, switch=OVSKernelSwitch)

def add_controller(net, name='c0'):
    """
    Add a controller to the given network.
    """
    return net.addController(name)

def add_hosts(net, number_of_hosts):
    """
    Add a specified number of hosts to the given network.
    """
    return [net.addHost(f'h{i+1}') for i in range(number_of_hosts)]

def add_switches(net, number_of_switches):
    """
    Add a specified number of switches to the given network.
    """
    return [net.addSwitch(f's{i+1}') for i in range(number_of_switches)]

def create_links(net, hosts, switches):
    """
    Create links between the hosts and switches in a linear topology.
    """
    for i, host in enumerate(hosts):
        net.addLink(host, switches[i // (len(hosts) // len(switches))])

def start_network(net):
    """
    Start the network, provide an interactive CLI, and then stop the network on exit.
    """
    net.start()
    CLI(net)
    net.stop()

def parse_arguments():
    """
    Parse command-line arguments to configure the network topology.
    """
    parser = argparse.ArgumentParser(description='Generate a custom Mininet topology.')
    parser.add_argument('--hosts', type=int, default=4, help='Number of hosts in the network')
    parser.add_argument('--switches', type=int, default=2, help='Number of switches in the network')
    args = parser.parse_args()
    return args

def custom_topology(args):
    """
    Main function to create and set up a custom network topology based on user input.
    """
    net = create_network()
    add_controller(net)
    hosts = add_hosts(net, args.hosts)
    switches = add_switches(net, args.switches)
    create_links(net, hosts, switches)
    start_network(net)

if __name__ == '__main__':
    args = parse_arguments()
    setLogLevel('info')  # Set log level to 'info' to show informational messages
    custom_topology(args)  # Create and start the custom network topology based on parsed arguments

