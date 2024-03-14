# Refresher on ISO Open Systems Interconnection (OSI)model
- Models crucial to understanding network virtualization: the ISO Open Systems Interconnection (OSI) model and the TCP model, starting with the Application Layer 
- Topic is essential for grasping how different layers of network architecture interact and support the virtual networks we rely on today
- Start with a quick refresher on the OSI model
  - Conceptual framework used to understand network interactions in seven distinct layers
  - Each layer serves a specific function and communicates with the layers directly above and below it
  - From bottom to top, these are the Physical, Data Link, Network, Transport, Session, Presentation, and Application layers

## TCP Model
- The TCP/IP model, often more closely aligned with real-world networking, simplifies this architecture into four layers: 
  - Link Layer, Internet (or Network) Layer, Transport Layer, Application Layer
  - We'll start on the Application Layer of the TCP model

### TCP Application Layer
- Includes OSI application layer, presentation layer, and most of the session layer

#### The Application Layer in Detail
- Application Layer is the topmost layer in both models
- Acts as the interface between the end-user and the network 
- Where high-level protocols reside, facilitating user or software applications to access network services

#### Example application layer protocols and Implementations
- HTTP (Hypertext Transfer Protocol)
  - Foundation of data communication for the World Wide Web
  - When you visit a website, your browser uses HTTP to request web pages from servers.
- HTTPS (HTTP Secure) 
  - An extension of HTTP
  - Uses SSL/TLS to provide encrypted communication and secure identification of a network web server, making your browsing secur 
- FTP (File Transfer Protocol)
  - Used for transferring files between a client and a server on a network 
  - Standard network protocol used for uploading files from a local computer to a remote server or vice versa
- SMTP (Simple Mail Transfer Protocol)
  - The standard protocol for sending emails across the Internet 
  - When you send an email, your email client uses SMTP to transfer your message to the recipient's mail server.
- DNS (Domain Name System)
  - Translates domain names to IP addresses 
  - Allows you to access a website by typing its name instead of its numerical IP address.

#### Includes OSI Presentation and Session Layer Functions
- Application Layer in the TCP model also encompasses functionalities from the OSI model's Presentation and Session layers
- Presentation Layer responsibilities
  - Ensures that data transferred from the application layer of one system can be read by the application layer of another
  - Responsibilities include data encryption, compression, and translation between different data formats
- Session Layer tasks
  - Establishes, manages, and terminates connections (sessions) between applications 
  - Responsible for authenticating and authorizing sessions 
  - Ensures data exchange during a session is well-organized and resynchronized.

#### Real-World Application and Importance
- Understanding the Application Layer and its protocols is crucial for network virtualization
  - Virtual networks rely on these protocols to provide secure, efficient, and reliable communication between distributed services and applications.
- Examples
  - In a virtualized network, HTTP and HTTPS protocols are fundamental for enabling web-based management interfaces and API endpoints that facilitate network management and orchestration
  - Similarly, DNS plays a vital role in service discovery within virtual networks, allowing for the dynamic resolution of service endpoints in cloud environments

#### Demo: Python / C
- Just run and click enter through client_tcp.py
- Will show full functionality after transport layer

### Transport Layer
- Plays key role in data transfer across network
- Integrates emaining parts of the OSI session layer plus transport layer

#### TCP Transport Layer Explained
- Transport Layer is responsible for providing end-to-end communication services for applications 
- Ensures that data is transferred from one point to another reliably, in sequence, and without errors
- Where you'll find the core protocols that define how data packets are transmitted across networks, like
  - TCP (Transmission Control Protocol)
  - UDP (User Datagram Protocol).

#### Key Protocols of the Transport Layer
- TCP (Transmission Control Protocol)
  - Connection-oriented protocol
  - Establishes a connection before any data can be sent, ensuring that data is delivered in the order it was sent and without errors
  - Used by applications that require reliable delivery
    - Web browsers
    - Email clients
    - Database systems
- UDP (User Datagram Protocol)
  - Unlike TCP, UDP is connectionless
  - Does not establish a connection before sending data 
  - Makes UDP faster and more efficient for applications that can tolerate lost packets
    - Streaming video
    - Online games 
    - Voice over IP (VoIP).

#### Implementations and Real-World Applications
- Web Browsing
  - When you visit a website, your browser uses TCP
  - Ensures that all the webpage data is received accurately and in order
- Email Transmission
  - SMTP, discussed earlier, relies on TCP for the reliable delivery of emails across the Internet
- Streaming Services
  - Services like Netflix or Spotify use UDP for streaming video and audio
  - UDP's efficiency in handling packet loss and latency makes it ideal for real-time data transmission
- Online Gaming
  - Many multiplayer online games use UDP
  - Minimizes the delay (latency) between player actions and game responses, providing a smoother gaming experience.
- VoIP Calls
  - Voice over IP services, such as Skype or Zoom, also prefer UDP
  - UDP is lower latency, which is crucial for maintaining call quality.

#### Integrating OSI Session Layer Functions
- TCP model does not explicitly have a Session layer
- Most of its functions are embedded within the Transport Layer
- Includes establishing, managing, and terminating connections between applications
- Example: when a TCP connection is established, it is the result of the Transport Layer negotiating and setting up a session for data exchange
  - Setting up port numbers
  - Managing the state of the connection ensuring that data flows smoothly between the correct applications.

#### Importance in Network Virtualization
- Virtual networks rely on TCP and UDP to establish secure, reliable, and efficient communication channels between virtualized services and applications. 
- Virtual switches and routers within a software-defined network (SDN) architecture use these protocols to route traffic effectively across virtual networks.
- Ability to encapsulate and segment data into TCP or UDP packets enables network virtualization technologies to:
  - Efficiently manage network traffic
  - Prioritize certain types of traffic (like VoIP or streaming services)
  - Ensure data integrity and order across complex, distributed network environments

Conclusion

#### Demo: Python / C
- Demo server_tcp and client_tcp
- Demo server_udp and client_udp
- Step through code and show how different

### Network Layer

#### TCP/IP Network Layer Explained
- Primarily concerned with packet forwarding 
  - Includes routing through different routers across networks
- Is where logical addressing (i.e., IP addresses) is used to ensure data packets reach their correct destination
- Networkl layer corresponds to a subset of the OSI model's Network Layer but is focused on the protocols used in the TCP/IP suite

#### Key Protocols of the Network Layer
- IP (Internet Protocol)
  - Fundamental protocol that underpins the entire Internet
  - Responsible for delivering packets from the source host to the destination host solely based on the IP addresses in the packet headers
  - IP includes both IPv4 and IPv6 protocols
- ICMP (Internet Control Message Protocol)
  - Used by network devices to send error messages and operational information
  - For example, that a requested service is not available or that a host or router could not be reached.
- ARP (Address Resolution Protocol)
  - Responsible for mapping a network address (IP address) to a physical address
  - Example: MAC address in a local network.


#### Implementations and Real-World Applications
- Routing
  - Routers operate at the Network Layer
  - Use protocols determine the best path for forwarding packets across multiple networks to their destination
  - Examples:
    - OSPF (Open Shortest Path First)
    - BGP (Border Gateway Protocol)
- Network Troubleshooting and Management
  - Tools like ping and traceroute use ICMP to diagnose network connectivity issues
- IP Addressing and Subnetting
  - Design and implementation of IP addressing schemes and subnetting are crucial for: 
    - Network segmentation
    - Efficient use of IP address space
    - Security within an organization's network.

#### Importance in Network Virtualization
- Virtual Routing and Forwarding (VRF)
  - In a virtualized network, VRF allows for segmentation of a single physical network infrastructure into multiple virtual networks, each with its own routing table
- Software-Defined Networking (SDN)
  - SDN controllers programmatically control the flow of network traffic
  - Leverage the capabilities of the Network Layer to make networks more flexible and efficient.
- Overlay Networks
  - Technologies like VXLAN (Virtual Extensible Local Area Network) and NVGRE (Network Virtualization Using Generic Routing Encapsulation)
  - Encapsulation at the Network Layer to create overlay networks that operate independently from the underlying physical network
  - Enables scalable multi-tenancy in cloud environments
Conclusion

#### Demo: Python / C
- Run server_network.py and client_network.py
- Similar to previous demo but shows network layer info


### Link Layer
- Foundational TCP Layer in network communication
- Corresponds to the OSI model's Data Link and Physical layers
- Where the "rubber meets the road" in terms of actual data transmission over physical and logical network interfaces.

#### TCP/IP Link Layer Explained
- Responsible for the physical transmission of data over network devices
- Includes protocols that operate on the link that a host is physically connected to
- Layer is crucial for defining
  - How data is formatted for transmission
  - How it accesses the medium
  - How it manages errors and retransmissions

#### Key Protocols of the Link Layer
- ARP (Address Resolution Protocol)
  - We touched on ARP when discussing the Network Layer 
  - Its operation is also deeply tied to the Link Layer
  - ARP translates IP addresses into MAC addresses
  - Enables IP packets to be transmitted over Ethernet networks
- NDP (Neighbor Discovery Protocol)
  - The IPv6 equivalent of ARP
  - Used for:
    - Address autoconfiguration
    - Discovery of other nodes on the network
    - Determining their addresses
    - Finding available routers
    - Maintaining reachability information.
- Ethernet
  - The most widely used LAN (local area network) technology
  - Ethernet defines:
    - Wiring and signaling standards for the physical layer
    - Frame formats and protocols for the data link layer
- Wi-Fi (IEEE 802.11) 
  - A set of standards for wireless local area networking
  - Wi-Fi operates at the Link Layer
  - Allowing devices to communicate without direct cable connections
- PPP (Point-to-Point Protocol)
  - Used over direct connections between two nodes
    - Example: dial-up connections
  - PPP provides a standard method for transporting multi-protocol datagrams over point-to-point links.

#### Implementations and Real-World Applications
- Network Interface Cards (NICs)
  - Every device that connects to a network, whether wired or wireless, includes a NIC
  - This hardware operates at the Link Layer and enables device to communicate over the network
- Switching
  - Network switches operate at the Link Layer
  - Forward data based on MAC addresses
  - Play a crucial role in segmenting network traffic, improving efficiency and security within LANs
- Wireless Access Points
  - Wi-Fi access points allow devices to connect to a network wirelessly
   - Use IEEE 802.11 standards to manage data transmission over radio waves
- Virtual Switches
  - In virtualized environments, virtual switches connect virtual machines (VMs) to both physical and virtual networks
  - Perform similar functions as physical switches but within a software-defined infrastructure

#### Importance in Network Virtualization
- Link layer supports the creation and management of virtualized network interfaces and connections
- Virtual NICs (vNICs) 
  - Virtual machines use vNICs to connect to virtual networks
  - vNICs emulate physical NICs but operate entirely in software
- Virtual LANs (VLANs)
  - VLANs allow network administrators to segment networks into smaller, isolated networks over the same physical infrastructure,   - Can automate network management management and security.
- Overlay Networks
  - Technologies such as VXLAN leverage Link Layer protocols to encapsulate Layer 2 frames within Layer 3 packets
  - Enabling the creation of scalable overlay networks across Layer 3 infrastructures

# Protocols and Ports

## Understanding Protocols

- Protocols are sets of rules and standards
- Define how data is transmitted and received over a network
- Each protocol operates at a specific layer of the OSI or TCP/IP model
- Ensures that information is passed correctly between layers and across network devices
- Examples:
  - IP operates at the Network Layer, ensuring data packets are routed correctly
  - TCP and UDP work at the Transport Layer, managing the details of data transmission between end systems

## The Role of Ports
- Ports work alongside protocols at the Transport Layer to direct traffic to specific services or applications on a device
- Numerical identifier that enables a network device to recognize the specific process or application to which incoming data should be delivered
- Mechanism is crucial for a device that runs multiple services to distinguish between, for instance, web traffic (HTTP) destined for a web server and email traffic (SMTP) intended for a mail server

## How Protocols and Ports Interact
- Protocol Specification
  - Protocols define the structure and type of communication
  - Example: TCP ensures reliable, ordered, and error-checked delivery of a stream of bytes.
- Port Differentiation
  - Ports allow a single device to differentiate between multiple types of traffic or sessions
  - Example: port 80 is commonly used for HTTP traffic, while port 443 is used for HTTPS traffic
- Without ports, a server wouldn't know which application should handle an incoming packet, even if it knew, via the IP address and protocol, on which device the application resides

## Real-World Applications and Network Virtualization
- Web Browsing
  - When you access a website, your browser uses HTTP or HTTPS protocols, typically over port 80 or 443, to request web pages from a server
- Email Services
  - Email clients use:
    - SMTP (port 25) for sending emails
    - POP3 (port 110) or IMAP (port 143) for receiving emails
  - Ensures that messages are directed to the correct application.
- FTP Services
  - FTP clients use ports 20 and 21 for data transfer and control messages
  - Allows for the reliable upload and download of files.

## Demo: Python / C
- See previous server/client demos
