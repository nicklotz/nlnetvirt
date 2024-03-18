# Lab 05: Mininet Commands

## A. General commands

1. Log into your vagrant VM that has Mininet installed if not already there.

```
cd ~/mininet-vm
vagrant ssh
```

2. Launch into the Mininet utility.

```
sudo mn
```

Mininet should start its default topology of 1 controller, 1 switch, and 2 hosts.

3. Confirm this by listing the available nodes via the interactive prompt.

```
nodes
```

4. List the nodes' network interfaces.

```
intfs
```

5. Show the links between the nodes (also gives a good sense of the network topology in simple setups).

```
links
```

6. Test communication between the hosts.

```
pingall
```

7. Test bandwidth between the hosts.

```
iperf
```

8. Show detailed networking information for all nodes in the network (switches, controllers, and hosts).

```
dump
```

## B. Commands for individual nodes

1. Examine the virtual network interface for host 1. What can you identify about the virtual network it lives on?

```
h1 ifconfig
```

2. Exameine the virtual network interface for host 2. What can you identify about the virtual network it lives on?

```
h2 ifconfig
```

3. Test communication between h1 and h2 directly.

```
h1 ping -c 4 h2
h2 ping -c 4 h1
```

4. List flow entries for the s1 switch. What can you identify about what traffic is allowed and from where?

```
sh ovs-ofctl dump-flows s1
``` 
