# Introduction to SDN
- SDN decouples the network's control plane (which makes decisions about where traffic is sent) from the data plane (which forwards traffic to the selected destination)
- Transforms traditional networking architecture by introducing a centralized controller
- That controller can communicate with all the switches and routers in the network using southbound protocols
- Centralized control plane provides a comprehensive view of the network
- Allows for automated and dynamic traffic management based on the current network conditions, application requirements, and policies

## Need for Active Networks
- Cloud computing, big data, and mobile computing has exponentially increased network traffic volume, types, and patterns
- Active networks, like those enabled by SDN, can adapt to changing network conditions in real-time

## Protocols
- SDN's functionality largely dependent on communication protocols between SDN controller, network devices, and applications
- These protocols are categorized based on the direction of communication
  - Northbound
  - East/west-bound
  - Southbound
### Northbound protocol
- Defines communication between the SDN controller and the network applications or business logic
- Enables the applications to request network services (such as bandwidth or routing changes) from the controller
- Controller then translates these requests into specific networking configurations
- Generally implemented as APIs
#### Northbound examples
- REST APIs
- OpenDaylight Controller APIs
### East/West-bound protocol
- Communication between SDN controllers or between modules within a controller in a distributed SDN architecture
- Ensures consistency and coherence in network control plane 
  - Allows multiple controllers to share information, synchronize state, and coordinate actions
- Important in large networks or cloud environments where a single controller not be sufficient to manage entire network
#### East/West examples
- OVSDB (Open vSwitch Database Management Protocol)
- BGP-LS (Border Gateway Protocol - Link State)
### Southbound protocol.
- Most critical in the SDN architecture
- Facilitate communication between the SDN controller and the network devices (the data plane)
- Most well-known southbound protocol is OpenFlow
#### OpenFlow
- Allows the SDN controller to define how network devices should handle IP packets
- Sets up rules, actions, and paths for the traffic
- Enables more granular control over traffic flow
- Allowing for sophisticated management strategies
  - Load balancing
  - Netowrk virtualization
  - Security enforcement 
#### Other Southbound examples
- NETCONF (Network Configuration Protocol)
- OVSDB (Open vSwitch Database Management Protocol)

## Real-Life Implementation Examples
### Data Centers
- SDN is widely used in data center networks to:
  - Improve bandwidth utilization
  - Automate network configurations
  - Facilitate rapid deployment of virtualized services
### Cloud Services
- Cloud providers use SDN to offer networking solutions to customers like on-demand bandwidth and virtual networks
### Campus Networks
- Universities and corporate campuses use SDN to simplify network management and provide better services and access control







