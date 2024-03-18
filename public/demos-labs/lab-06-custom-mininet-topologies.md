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

## B. Write custom topologies with Python

1. 
