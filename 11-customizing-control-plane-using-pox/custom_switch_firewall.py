from pox.core import core
from pox.lib.util import dpid_to_str
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class CustomSwitchFirewall(object):
    def __init__(self, connection):
        self.connection = connection
        connection.addListeners(self)

        # Add your firewall rules here
        # Example: Block traffic between two hosts
        self.firewall_rules = [{"src": "10.0.0.1", "dst": "10.0.0.2"}]

    def _handle_PacketIn(self, event):
        packet = event.parsed
        packet_in = event.ofp

        # Implement basic L2 learning switch functionality
        # For demonstration, skipping implementation details

        # Implement firewall functionality
        # Check if the packet matches any firewall rule
        for rule in self.firewall_rules:
            if packet.src.toStr() == rule["src"] and packet.dst.toStr() == rule["dst"]:
                log.info("Dropping packet based on firewall rule: %s -> %s" % (packet.src, packet.dst))
                return  # Drop packet

        # Example: Forward packet to all ports (Flood)
        msg = of.ofp_packet_out()
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        msg.data = packet_in
        self.connection.send(msg)

def launch():
    def start_switch(event):
        log.info("Controlling %s" % (dpid_to_str(event.dpid),))
        CustomSwitchFirewall(event.connection)

    core.openflow.addListenerByName("ConnectionUp", start_switch)

