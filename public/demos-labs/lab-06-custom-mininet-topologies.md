# Lab 06: Custom Mininet Topologies

## A. Custom topologies with the Mininet CLI

1. Log into the Vagrant Mininet VM if not already there.

```
cd ~/mininet-vm
vagrant ssh
```

2. Clean up previous mininet setup if needed.

```
sudo mn -c
```

3. Create a simple topology with several hosts.

```
sudo mn --topo single,4
```

4. From inside the mininet prompt, examine the number of switches, number of nodes, and links between them. What would this topology look like visually?

```
net
```

4. Clean up the single topology.

```
quit
sudo mn -c
```

5. Create a linear topology with several hosts.

```
sudo mn --topo linear,4
```

6. From inside the mininet prompt, examine the number of switches, number of nodes, and links between them. What would this topology look like visually?

```
net
```

7. Clean up the linear topology.

```
quit
sudo mn -c
```

8. Create a "square pyramid" tree topology.

```
sudo mn --topo tree,depth=4,fanout=2
```

9. From inside the mininet prompt, examine the number of switches, number of nodes, and links between them. Based on the observed topology, what can you see the **depth** and **fanout** values represent?

```
net
```

10. Clean up this topology.

```
quit
sudo mn -c
```

11. Create a second tree topology. How is this "pyramid" visually different from the previous example?

```
sudo mn --topo tree,depth=2,fanout=4
```

12. From inside the mininet prompt, examine the topology and see it it confirms with your intuition.

```
net
```

13. Clean up this topology.

```
quit
sudo mn -c
```

## B. Create a custom topology with Python

1. Create a new file called **customtopology.py**.

```
touch customtopology.py
```

2. Open customtopology.py and paste the following code:

```python
#!/usr/bin/env python3

import argparse
from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

def create_network():
    return Mininet(controller=Controller, switch=OVSKernelSwitch)

def add_controller(net, name='c0'):
    return net.addController(name)

def add_hosts(net, number_of_hosts):
    return [net.addHost(f'h{i+1}') for i in range(number_of_hosts)]

def add_switches(net, number_of_switches):
    return [net.addSwitch(f's{i+1}') for i in range(number_of_switches)]

def create_links(net, hosts, switches):
    for i, host in enumerate(hosts):
        switch = switches[i % len(switches)]
        net.addLink(host, switch)

def interconnect_switches(net, switches):
    for i in range(len(switches) - 1):
        net.addLink(switches[i], switches[i+1])

def start_network(net):
    net.start()
    CLI(net)
    net.stop()

def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate a custom Mininet topology.')
    parser.add_argument('--hosts', type=int, default=4, help='Number of hosts in the network')
    parser.add_argument('--switches', type=int, default=2, help='Number of switches in the network')
    args = parser.parse_args()
    return args

def custom_topology(args):
    net = create_network()
    add_controller(net)
    hosts = add_hosts(net, args.hosts)
    switches = add_switches(net, args.switches)
    create_links(net, hosts, switches)
    interconnect_switches(net, switches)
    start_network(net)

if __name__ == '__main__':
    args = parse_arguments()
    setLogLevel('info')
    custom_topology(args)

``` 

3. Save and close customtopology.py.

4. Make the program executable.

```
chmod +x customtopology.py
```

5. View the program's usage instructions.

```
sudo ./customtopology.py --help
```

6. Create a dynamic topology with 5 hosts and 3 switches.

```
sudo ./customtopology.py --hosts 5 --switches 3
```

7. From the Mininet CLI, examine the generated network.

```
net
pingall
```

8. Mannually change the network topology by adding a new host.

```
py net.addHost('h6')
```

9. Link the new host to one of the switches.

```
py net.addLink(net.get('h6'), net.get('s1'))
```

10. Set the new host's networking information.

```
py net.get('h6').setIP('10.0.0.6', intf='h6-eth0')
```

11. Bring up the new host's network interface.

```
py net.get('h6').cmd('ifconfig h6-eth0 up')
```

12. Check the new configuration.

```
nodes
net
```

13. Test communication between all the nodes. Does it work?

```
pingall
```

Type `CTRL-C` to kill the ping when you determine whether or not it's working as ex
pected.


14. Check the flow entries for switch **s1**. What do you see that might indicate what the issue is?

```
sh ovs-ofctl dump-flows s1
```

What component do you think is responsible for the switch's flow entries? We'll learn more later about how this configuration takes place.

15. Clean up your mininet topology.

```
quit
sudo mn -c
```
