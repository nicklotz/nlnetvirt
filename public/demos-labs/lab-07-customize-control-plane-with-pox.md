# Lab 07: Customizing the Control Plane Using POX

## A. Setup and initial test

1. Connect to your Vagrant Mininet VM if not already there.

```
cd ~/mininet-vm
```
```
vagrant ssh
```

2. Clean up any existing mininet topologies.

```
sudo mn -c
```

3. Create a new mininet topology of three hosts connected to a single switch.
```
sudo mn --topo single,3 --mac --switch ovsk --controller remote
```

The **--mac** option sets MAC addresses automatically, **--switch** ovsk specifies the use of the Open vSwitch kernel switch, and **--controller remote** tells Mininet to use a remote controller, which will be our POX controller.

4. Test the mininet network communication. Can hosts communicate with each other? Why or why not?

```
pingall
```
```
iperf
```

5. Exit mininet for now.

```
quit
```
```
sudo mn -c
```

## B. Launch the POX controller

1. Open a *second* terminal window and navigate to the POX directory. 

```
cd ~/pox/
```

2. Start the POX controller with a simple forwarding module:

```
./pox.py forwarding.l2_learning
```

This command starts POX and loads the l2_learning modul. It implements a basic learning switch that mimics the behavior of a physical switch by learning the source MAC addresses of packets and forwarding them accordingly.

3. Back in your *first* terminal window, relaunch mininet with the same topology as earlier.

```
sudo mn --topo single,3 --mac --switch ovsk --controller remote
```

4. Test the mininet network's communication. Is it successful this time?

```
pingall
```
```
iperf
```

## C. Create a Simple Firewall

1. In your *second* terminal window, run `CTRL-C` to kill the POX server for now.

2. Navigate to the POX forwarding modules directory.

```
cd ~/pox/pox/forwarding
```

3. Create a new Python script in the **pox/pox/forwarding** directory named **firewall.py**. This script will define firewall rules to block traffic between specific hosts.

```
touch ~/pox/pox/forwarding/firewall.py
```

4. Open **firewall.py** and paste the following code.

```python
from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.addresses import IPAddr
from pox.lib.packet import ipv4, icmp

log = core.getLogger()

class SimpleFirewall(object):
    def __init__(self, connection):
        self.connection = connection
        connection.addListeners(self)

    def _handle_PacketIn(self, event):
        packet = event.parsed
        if not packet.parsed:
            log.warning("Ignoring incomplete packet")
            return

        self.process_packet(event)

    def process_packet(self, event):
        ip_packet = event.parsed.find('ipv4')
        if ip_packet:
            if self.is_blocked(ip_packet):
                log.debug("Blocking packet from %s to %s", ip_packet.srcip, ip_packet.dstip)
                return  # Drop the packet by not forwarding
            else:
                self.forward_packet(event)
        else:
            # Forward non-IP packets
            self.forward_packet(event)

    def is_blocked(self, ip_packet):
        # Define the blocking condition for ICMP packets from H1 to H2
        icmp_packet = ip_packet.find('icmp')
        src_ip = ip_packet.srcip
        dst_ip = ip_packet.dstip

        # Return True to block, False to allow
        return src_ip == IPAddr("10.0.0.1") and dst_ip == IPAddr("10.0.0.2") and icmp_packet is not None

    def forward_packet(self, event):
        # Forward the packet out of all ports
        msg = of.ofp_packet_out()
        msg.data = event.ofp
        action = of.ofp_action_output(port=of.OFPP_ALL)
        msg.actions.append(action)
        self.connection.send(msg)

def launch():
    def start_switch(event):
        log.debug("Controlling %s" % (event.connection,))
        SimpleFirewall(event.connection)
    core.openflow.addListenerByName("ConnectionUp", start_switch)

```

5. Save and close firewall.py.i

6. Navigate back to the root **pox** directory.

```
cd ~/pox
```

## D. Update POX and test the firewall module

1. In your *second* terminal winow, restart POX with your firewall module instead of the l2_learning module

```
./pox.py forwarding.firewall
```

2. Back in your *first terminal window*, try pinging h3 from h2. Would you expect these pings to work? Why or why not?

```
h2 ping -c 4 h3
```

3. Try pinging h2 from h1. Would you expect these pings to work? Why or why not?

```
h1 ping -c 4 h2
```

4. Try pinging h1 from h2. Would you expect these pings to work? Why or why not? The answer isn't obvious! Think about how ICMP pings work, and look at the code to your firewall module.


```
h2 ping -c 4 h1
```

5. Exit Mininet and clean up.

```
quit
```
```
sudo mn -c
```
