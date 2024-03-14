# Lab: Customizing the Control Plane Using POX

## Prerequisites
- Mininet
- Pox (should come with Mininet)
- Python

```
sudo mn --topo single,3 --mac --switch ovsk --controller remote
```

This command tells Mininet to create a network with a single switch connected to three hosts. The --mac option sets MAC addresses automatically, --switch ovsk specifies the use of the Open vSwitch kernel switch, and --controller remote tells Mininet to use a remote controller, which will be our POX controller.

## Customizing the Control Plane with POX
### B. Implementing Switching
#### Launch the POX Controller
1. Open a new terminal window and navigate to the POX directory. Start the POX controller with a simple forwarding module:

```
./pox.py forwarding.l2_learning
```

This command starts POX and loads the l2_learning module, which implements a basic learning switch that mimics the behavior of a physical switch by learning the source MAC addresses of packets and forwarding them accordingly.

### C. Create a Simple Firewall
#### Write a Custom Firewall Module
1. Create a new Python script in the **pox/pox/forwarding** directory named **firewall.py**. This script will define firewall rules to block traffic between specific hosts.

```
touch ~/pox/pox/forwarding/firewall.py
```

2. Edit **firewall.py** to include the following:

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

#### Update the POX Controller to Use Your Firewall Module
3. Restart POX with your firewall module instead of the l2_learning module

```
./pox.py forwarding.firewall
```

#### Test firewall functionality
4. Verify that the firewall rules are working by attempting to ping between hosts that should be blocked according to your firewall rules. If the firewall is functioning correctly, these pings should fail.

```
sudo mn
h1 ping h2
```
