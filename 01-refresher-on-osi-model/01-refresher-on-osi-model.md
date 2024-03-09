# Refresher on ISO Open Systems Interconnection (OSI)model
- Models crucial to understandinf network virtualization: the ISO Open Systems Interconnection (OSI) model and the TCP model, starting with the Application Layer 
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
#### Remaining parts of the OSI session layer plus transport layer
#### Demo: Python / C
### Network Layer
#### Subset of the OSI network layer
#### Demo: Python / C
## Link Layer
### OSI data link layer and sometimes the physical layers,as well as some
protocols of the OSI's network layer. This layer also uses Address
Resolution Protocol (ARP) or Neighbor Discovery Protocol(NDP).
# Protocols and Ports
## Demo: Python / C
