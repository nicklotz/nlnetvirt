# Import necessary classes from Mininet
from mininet.net import Mininet  # The main Mininet class to create and manage networks.
from mininet.node import Controller, OVSKernelSwitch  # Controller and switch classes.
from mininet.cli import CLI  # Command Line Interface class to interact with the network.
from mininet.log import setLogLevel  # Function to set the verbosity of log messages.

# Define the function to create and set up the custom topology
def customTopology():
    # Create the network, specifying the default controller and switch types to be used
    net = Mininet(controller=Controller, switch=OVSKernelSwitch)

    # Add a controller to the network
    # 'c0' is the name of the controller
    c0 = net.addController('c0')

    # Add hosts to the network
    # 'h1', 'h2', 'h3', 'h4' are the names of the hosts
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')

    # Add switches to the network
    # 's1' and 's2' are the names of the switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    # Create links between network devices
    # Connect hosts h1 and h2 to switch s1
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    # Connect switch s1 to switch s2
    net.addLink(s1, s2)
    # Connect hosts h3 and h4 to switch s2
    net.addLink(h3, s2)
    net.addLink(h4, s2)

    # Start the network
    # This initiates all controllers, switches, and hosts
    net.start()

    # Drop the user into a CLI so they can interact with the network
    # This allows for manual command input, such as ping tests or network configuration commands
    CLI(net)

    # Stop the network
    # This is called after exiting the CLI to clean up and terminate all network devices
    net.stop()

# This is a Python idiom that checks if this script is being run directly
# This ensures the following block of code runs only if the script is executed, not if it's imported as a module
if __name__ == '__main__':
    # Set the log level to 'info' to show informational messages during the execution
    setLogLevel('info')
    # Call the function to create and start the custom topology
    customTopology()

