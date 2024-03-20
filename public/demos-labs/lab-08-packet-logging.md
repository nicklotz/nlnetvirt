# Lab 08: Create a Packet Logging POX Module

## A. Create a new POX module

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

3. Navigate to the **~/pox/pox/misc** directory.

```
cd ~/pox/pox/misc
```

3. Create a new file called **packetlogger.py**.

```
touch packetlogger.py
```
4. Paste the following into packetlogger.py:

```python
from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.packet import ethernet, ipv4, arp, icmp

log = core.getLogger()

class ExtendedPacketLogger(object):
    def __init__(self, connection):
        self.connection = connection
        connection.addListeners(self)

    def _handle_PacketIn(self, event):
        packet = event.parsed
        if not packet.parsed:
            log.warning("Ignoring incomplete packet")
            return
        packet_info = self.extract_packet_info(packet)
        log.info(packet_info)

    def extract_packet_info(self, packet):
        packet_type = type(packet.next).__name__
        src, dst = packet.src, packet.dst
        if packet_type == 'arp':
            arp_packet = packet.next
            return f"ARP: {arp_packet.opcode} from {arp_packet.hwsrc} ({arp_packet.protosrc}) to {arp_packet.hwdst} ({arp_packet.protodst})"
        elif packet_type == 'ipv4':
            ipv4_packet = packet.next
            src, dst = ipv4_packet.srcip, ipv4_packet.dstip
            if ipv4_packet.protocol == ipv4.ICMP_PROTOCOL:
                icmp_packet = ipv4_packet.payload
                return f"ICMP: Type {icmp_packet.type} from {src} to {dst}"
            # Add more conditions here for other types like TCP/UDP
        return f"{packet_type}: from {src} to {dst}"

def launch():
    def start_switch(event):
        log.debug("Controlling %s" % (event.connection,))
        ExtendedPacketLogger(event.connection)
    core.openflow.addListenerByName("ConnectionUp", start_switch)
```

5. Save and close packetlogger.py.

## B. Run the packet logging POX module

1. Change back into the main POX directory.

```
cd ~/pox
```

2. Run the simple controller along with your packer logging module.

```
./pox.py forwarding.l2_learning misc.packetlogger
```

3. Open up a different terminal screen and run a simple mininet topology.

```
sudo mn --topo tree,2 --mac --switch ovsk --controller remote
```

4. Practice pinging between hosts.

```
h1 ping h2
```
```
h3 ping h4
```
```
h4 ping h2
```

and so on. Let each ping run for several seconds. Navigate to the terminal screen where you are running the POX controller. Why does the controller only log the first few pings? (**Hint:** what do the switches do when the ping starts?)

5. Try pinging between switches.

```
h1 ping s1
s1 ping s2
```

Do you see any logging by the controller? Why or why not?

## C. Cleanup

1. In the terminal running the POX controller, type `CTRL-C` to kill the POX server.

2. In the terminal running Mininet, exit and clean up.

```
quit
```
```
sudo mn -c
```
