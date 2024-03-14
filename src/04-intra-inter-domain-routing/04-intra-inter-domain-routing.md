# Intra-domain & Inter-domain Routing

## Intra-domain routing
- Also known as Interior Gateway Protocol (IGP) routing
- Focuses on routing within a single domain or autonomous system (AS)
  - An AS is a collection of IP networks and routers under the control of one entity that presents a common routing policy to the internet
### Interior Gateway Protocols (IGP) includes
#### RIP (Routing Information Protocol)
- One of the oldest routing protocols
- Simple to configure but less efficient for larger networks due to its hop count limitation and slow convergence
#### OSPF (Open Shortest Path First)
- More sophisticated protocol
- Uses link-state information to make routing decisions
- Providing faster convergence and better scalability
#### IS-IS (Intermediate System to Intermediate System)
- Similar to OSPF in terms of operation but used in certain large enterprise and service provider networks
- IGPs manage routing information through algorithms that calculate the shortest or most efficient paths

## Inter-domain Routing
- Routing between different autonomous systems
- Where the Border Gateway Protocol (BGP) comes into play
### Border Gateway Protocol (BGP)
- Standard protocol for exchanging routing information between autonomous systems on the internet
  - Classified as an Exterior Gateway Protocol (EGP)
  - Manages how packets are routed across diverse networks owned and operated by different organizations
- Uses a path vector protocol
  - Each route advertisement includes the full path of ASes that the packet must traverse to reach the destination network
  - Allows BGP to make informed routing decisions and avoid routing loops

## Key terms
### Autonomous System (AS)
- Distinct network or group of networks under a common administration that shares a common routing policy
- BGP manages the exchange of routing information between these autonomous systems
### Egress/Ingress
- Relate to the flow of traffic in and out of a network
- Ingress refers to incoming traffic into a network
- Egress refers to outgoing traffic from a network
### Inbound/Outbound
- Inbound is connection initiated from outside network to inside
- Outbound is connection initiated from inside to outside
- Often used in context of policies or security settings

## Implementation Examples
### Enterprise Networks
- IGP protocols like OSPF or IS-IS are used to manage internal routing
- Ensures efficient communication between devices and servers within the AS
### Internet Service Providers (ISPs)
- ISPs use BGP to exchange routing information with other ISPs and large networks
- Ensuring that data can find its way across the global internet
- Ex. when ISP connects to an internet exchange point (IXP), it uses BGP to advertise its routes to other ISPs and learn their routes
### Data Centers
- In modern data centers, especially those providing cloud services, both IGP and BGP are used
- IGP protocols manage routing within the data center's network
- BGP may be used for routing between the data center and other networks, including the broader internet or other data centers



