# What is OpenFlow?
## Relation with SDN
- Often described as the first southbound protocol of SDN
- Serves as primary means of communication between SDN controller (brain of the network) and the network devices it manages
- Provides a standardized interface for controlling the flow of packets through network devices

## Southbound Protocol
- As a southbound protocol, OpenFlow defines communication between SDN controller (north) and network devices it controls (south)
- Specifies set of messages that the controller can use to add, update, and delete flow entries in flow tables of network devices
- Effectively determines the path of packets across the network

### Control / Data Plane Separation
#### Control plane
- Logical component that makes decisions about where traffic should go
- In an SDN environment is implemented by the SDN controller which uses OpenFlow to communicate with the network devices
#### Data plane
- Physical component actually moving packets from one point to another based on rules established by the control plane
- In OpenFlow-enabled networks, switches and routers act as the data plane
  - Execute actions specified by the flow entries installed by the controller

### Challenges in separating Control & data separation
#### Scalability
- As networks grow, ensuring the SDN controller can efficiently manage an increasing number of OpenFlow messages and maintain a real-time view of the network becomes challenging
#### Security
- Centralizing control in an SDN controller creates a potential single point of failure
- Protecting the controller and the communication channels (including OpenFlow messages) against attacks is critical
#### Performance
- Latency introduced by the communication between the controller and network devices can impact network performance
- Especially in scenarios requiring real-time or near-real-time decision-making
#### Interoperability
- Need to ensure network devices from different manufacturers can communicate effectively with the SDN controller via OpenFlow
- Adherence to protocol standards can be challenging to achieve in practice

## Hands-on: Setup mininet with VirtualBox & Vagrant
