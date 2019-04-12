# Routing Concepts

## Characteristics of a Network
- Topology
- Speed
- Cost
- Security
- Availability
- Scalability
- Reliability

## Why Routing?
- Connect one network to another
- Determines best route to destination
- Responsible for routing traffic between network
- Routing table to determine efficient path to destination

## What are Routers?
- Specialized Computers
- Requires same components as PC (CPU, OS, RAM, ...)
- Have specialized ports and NICs to interconnect devices to other networks

## Responsibilities of a Router
- Forwarding packets from source to destination
- Multiple networks on a router require multiple interfaces that each belong to a different IP network (these interfaces used to connect LANs / WANs)
- When packet arrives on router interface, check if router is final destination or if packet needs forwarding

## Router's Path-Choosing Methods
1. Router receives packet
2. Examines destination address
3. Uses routing table to examine best path
4. When match found, it encapsulates packet into data link frame of outgoing exit interface
5. Forwards packet out of that interface to destination

## Routers and Data Link Layer Frame Encapsulations
- Router can handle different data link layer frame encapsulations

## 3 Packet Forwarding Mechanisms
- Process Switching
- Fast Switching
- Cisco Express Forwarding (CEF)

## Process Switching
- Slower, older mechanism
- Process
    1. Packet arrives on interface
    2. Forwarded to Control Plane where CPU matches destination address with entry in routing table to determine exit interface
- Slow, because repeated for every packet in stream

## Fast Switching
- Common
- Uses fast-switching cache to store next-hop info
- Process
    1. Packet arrives on interface
    2. Forwarded to Control Plane where CPU searches for match in cache
    3. If no match, process-switched and forwarded to exit interface

## Cisco Express Forwarding
- Fastest, most recent, preferred
- Builds a Forwarding Information Base (FIB) and adjacency table
- Table entries triggered when changes occur in network topology
- When network converged, FIB and tables contain all info a router needs when forwarding packets
- FIB contains 
    - pre-computed reverse lookups
    - next hop info for route
    - interface and Layer 2 info

## Connect to a Network: Home Office
- Wireless to home router (laptop, tablets, ...)
- Ethernet to switch port on home router (printers, ...)
- Ethernet to ISP cable modem (home router, ...)
- Cable modem to ISP network

## Connect to a Network: Branch site
- Devices connect to Layer 2 switches via Ethernet
- Smart-Devices connect to Wireless Access Points (WAPs)
- WAPs connect to switches via Ethernet
- Layer 2 switches connect to edge router via Ethernet
- Edge router connects to WAN Service Provider

## Connect to a Network: Central site
- Devices connect to Layer 2 switches via Ethernet (Desktop PCs, VoIP phones, ...)
- Layer 2 switches connect (redundantly) to multilayer Layer 3 switches via Ethernet fiber-optic cables
- Layer 3 switches connect to edge router via Ethernet
- Corporate website server connects to edge router
- Edge router connects to WAN SP and also ISP for backup

## What info do Devices need for Network Access?
- IP address
- Subnet mask
- Default gateway

## Host sends Packet to Device: Same IP Network
- Packet forwarded directly to destination device
- Router does not get involved

## Host sends Packet do Device: Different IP Network
- Packet forwarded to default gateway
- Because can't communicate with devices outside of local network

## Default Gateways
- Device that routes traffic from local network to devices on remote network
- Routers often configured with own default gateway

## What should Documentation of Network Addressing include?
- Device names
- Interfaces used in design
- IP addresses and subnet masks
- Default gateway addresses

## Useful Documents when documenting a Network
- Topology diagram
- Addressing table

## 2 Ways of assigning IP Address to Host
> Most devices use DHCP
- Statically (Manual)
- Dynamically (DHCP)

## Device LEDs
- NICs have one or two LED indicators next to interface
- Green: good connection
- Blinking Green: network activity
- No Light: problem with cable or network
- Amber: malfunction (on Cisco Catalyst 2960 switch)

## Console Access

