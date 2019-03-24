# 1 | Explore The Network



## Introduction

* Internet is super duper important



## Network Sizes

* Small Home Networks
  + e.g. Sharing printers, documents, ...
* Small Office / Home Office Networks
  * e.g. Connect to your office from home
* Medium to Large Networks (Enterprise)
  * e.g. Consolidation, storage, access to information
  * e.g. Email, instant messaging, collaboration amongst employees
* World Wide Networks (WWW)
  * e.g. Internet



## Hosts

* Computers connected to a network that participate directly in network communication
* End devices



## Servers

* Computers with software that
  * Enable them to provide information to other end devices
  * e.g. Email, web pages
* Each service requires separate server software
* Can provide services to one or many clients
* A single computer can run multiple types of server software



## Clients

* Computers with software (e.g. web browser) installed that
  * Enable them to request and display information obtained from server
* A single computer can run multiple types of client software



## Types of Clients and Servers

* File Client and Server
* Web Client and Server
* Email Client and Server



## Peer-to-Peer

> P2P

* Client and server software usually runs on separate computers
* Also possible for one computer to carry out both roles 



## Advantages of P2P

* Easy setup
* Less complexity
* Lower cost 
  (no dedicated servers, etc.)
* For simple tasks 
  (file transfer, sharing printers, etc.)



## Disadvantages of P2P

* No centralized administration
* Not as secure
* Not scalable
* Slower performance 
  (all devices could be client and server)



## 3 Components of Network Infrastructure

* Devices
* Media
* Services



## Processes

* Provide funktionaliy
* Direct and move messages through the network
* Less obvious to us but critical to the operation of networks



## End Devices

* Source or destination of a message transmitted over network
* Distinguished by an address
* Use addresses to define where messages should be sent
* PC, Smartphone, etc.



## Intermediary Network Devices

> IND: Intermediary Network Devices

* Connect end devices to network
* Connect multiple networks to form an internetwork
* Provide connectivity
* Ensure data flows across the network



## Examples of INDs

* (Wireless) Router

* LAN / Multilayer Switch

* Firewall Appliance

  



## How do INDs work?

* Use destination end devices address and information about network interconnections to determine path of message through network



## Function of INDs

* Regenerate and retransmit data signals
* Maintain info about existing pathways through (inter)network
* Notify other devices of errors and communication failures
* Direct data along alternate pathways if link failure
* Classify and direct messages according to priorities
* Permit or deny flow of data, based on security settings



## Network Media

* Carries out communication accross a network
* Provides channel over which a message travels from source to destination



## 3 Basic Forms of Network Media

- Electrical Signals (Copper cable)
- Light Pulse (Fiber-optic cable)
- Microwave Signals (Wireless)



## Network Representations

* Use Topology Diagram
* Important terms
  * Network Interface Card (NIC / LAN Adapter)
  * Physical Port
  * Interface



## Topology Diagrams

* Provide visual map of how network is connected
* Physical topology diagrams
  * Identify physical location of INDs
* Logical topology diagrams
  * Identify devices, ports and addressing scheme



## Types of Networks

* Local Area Network (LAN)
* Wide Area Network (WAN)
* Metropolitan Area Network (MAN)
* Wireless LAN (WLAN)
* Storage Area Network (SAN)



## LAN

> Local Area Network

* Provides acces to users and end devices
* Small geographical area
* Provides high speed bandwidth to
  * Internal end devices
  * Intermediary devices
* Typically by enterprise, home, small business network, campus, ...
* Usually administered by single organization or individual
* Administrative control enforced on network level 
* Administrative control governs security and access control policies



## WAN

> Wide Area Network

* Provides access to other networks
* Wide geographical area (cities, states, provinces, countries, continents, …)
* Typically managed by (multiple)
  * Service Providers (SP)
  * Internet Service Providers (ISP)
* Provide slower speed links between LANs (typically)



## MAN

> Metropolitan Area Network

* Larger area than LAN but smaller than WAN
* City, ...
* Typically by single entity (large organization)



## SAN

> Storage Area Network

* Designed to support file servers
* Provide data storage, retrieval and replication



## Internet

* Worldwide collection of interconnected networks
* Not owned by any individual or group
* Relies on
  * Consistent and commonly recognized technologies and standards
  * Cooperation of many network administration agencies



## Internet Organizations and Agencies

* Help maintain structure and standardization of Internet protocols and processes
* Some examples,
  * Internet Engineering Task Force (IETF)
  * Internet Corporation for Assigned Names and Numbers (ICANN)
  * Internet Architecture Board (IAB)
  * ...



## Internet, Extranets and Intranets

> Biggest to smallest

* Internet
  * The world
* Extranet
  * Suppliers, customers, collaborators, ...
  * Provide secure safe access to individuals between different organizations
  * e.g. Company providing acces to suppliers contractors
  * e.g. Hospital providing a booking system to doctors for making appointments for patients
  * e.g. Local office of education providing budget to schools in its district
* Intranet
  * Private connection of LANs and WANs
  * Belong to organizations
  * Access only by members, employees, ...



## Internet Access Technologies

* Home Users
* Teleworkers (Remote Workers)
* Internet Service Provider (ISP)
  * Digital Subscriber Line (DSL)
  * Wireless WANs
  * Mobile Services



## Home and Small Office Internet Connections

* Cable
* DSL
* ADSL
* Cellular
* Satellite
* Dial-up Telephone
* Often connect directly with fiber optic cables
  * Higher bandwidth speeds
  * Supports more services (Internet, phone, TV, …)
* Choice of connection depends on 
  * Geography
  * Available ISP



## Business Internet Connections

* Dedicated Leased Line
  * Reserved circuits within ISP netwrok
  * Connects geographically separated offices
  * Montly or yearly rental rate (can be expensive)
* Ethernet WAN
  * Extends LAN into WAN
  * Benefits of Ethernet extended into WAN
* Business DSL (SDSL)
* Satellite
* Choice of connection depends on 
  * Geography
  * Available ISP



## Traditional Separate Networks

* Multiple services running on multiple networks
* Encapsulated from eachother
* Each network used different technologies to carry the communication signal
* Each network had own set of rules / standards to ensure communication
* z.B. separate computer, telephone and broadcast network



## Converging Network

* Multiple services running on one network

* Today networks are converging
* Converged networks capable of delivering data, voice and video over same network infrastructure
* Infrastructure uses same set of rules, agreements, implementation standards



## (Supporting) Network Architecture

* Technologies supporting the infrastructure, services and rules that move data across the network



## 4 Characteristics for Reliable Networks

* Fault Tolerance
* Scalability
* Quality of Service (QoS)
* Security



## Fault Tolerance

* Fault tolerant network is one that limits impact of a failure, so that fewest number of devices are affected
* Quick recovery
* Multiple (redundant) paths to divert when one fails
* Redundancy often by implementing a packet-switched network



## Scalability

* Scalable network can expand quickly to support more users / apps without performance loss
* Networks also scalable if designers follow standards and protocols
    * Soft-/hardware vendors can focus on improving products / services
    * Without worrying about reinventing the wheel



## Quality of Service (QoS)

* Description / measurement of overall performance of a service
* Quality of delivered services over a network
* Primary mechanism for 
    * congestion
    * reliable delivery of content to all users



## Security

* Refers to protecting information 
    * Contained within packets being transmitted
    * Stored on network attached devices

* Network infrastructure and information security
* Securing network infrastructures includes
    * Physical securing of devices that provide network connectivity
    * Preventing unauthorized access to management software



## 3 Primary Security Requirements

* Confidentiality
* Integrity
* Availability



## Confidentiality

* Only intended and authorized recipient can access and read data



## Integrity

* Assurance that information has not been altered in transmission



## Availability

* Assurance of timely and reliable access to data services for authorized users



## Packet Switched Network

- Splits traffic into packets that are routed over shared network
- Messages, emails, etc. broken into packets
- Each packet has addressing info of source and destination
- Routers switch packets based on network conditions at that moment
- User unaware / unaffected by router dynamically changing routes when a link fails



## Circuit-Switched Network

* Establishes dedicated circuit between source and destination before users can communicate
* Traditionally used for voice communication
* If call unexpectedly terminated, new connection needed
* User aware / affected if link fails



## When does Congestion occur?

> Congestion: reduced quality of service

*  When 
    * Network node or link carrying more data than it can handle
    * Demand for bandwidth (bits per second) exceeds amount available
    * Simultaneous communications attempted at same time
* Devices then queue or hold packets in memory until transmission available
* Prioritization can help against congestion
    * Low priority: Web pages
    * High priority: Streaming media
* QoS policy to manage the flow of data and traffic



## New Trends according to CISCO

* BYOD
* Online Collaboration
* Video Communication
* Cloud Computing
* Smart Home Technology



## BYOD

> Bring your own device

* Any device, to any content, in any manner
* A *new* trend according to CNF
* The freedom of end users to use personal tools to access information and communicate across a business or campus network
* e.g. Student doesn't need to access campus network via school computer



## Online Collaboration

* Collaborate across applications
* e.g. Cisco WebEx



## Cloud Computing

* Store files on servers over the internet
* Four primary types of Clouds
    * Public Clouds (e.g. cloud based app)
    * Private Clouds (strict access security, e.g. for organization)
    * Hybrid Clouds (e.g. two, or more clouds that are connected)
    * Custom Clouds (e.g. healthcare, government)
* Made possible by data centers



## Data Center

* Facility (room or building) to house computer systems and associated components
* Typically expensive to build and maintain
* Only large organizations use privately built data centers
* Smaller organizations lease server and storage services from large data center organizations



## Smart Home Technology

* Technology integrated into every-day appliances interconnected with other devices
* e.g. connect to oven with smartphone to make adjustments



## Powerline Networking

* Trend for home networking
* Ability to connect a device to network wherever there is an electrical outlet
* Saves cost of installing data cables without additional cost to electrical bill
* Powerline networking sends data on certain frequencies using same wiring that delivers electricity
* Useful when wireless access points can't be used or can't reach all devices in home
* Alternative when data network cables or wireless communications not possible



## WISP

> Wireless Internet Service Provider

* ISP that connects subscriber to designaged access point via similar wireless technologies in found in home WLANs
* Small dish / antenna installed on subscriber’s roof in range of WISP transmitter

* Subscriber’s access unit connected to the wired network inside the home
* Main difference to DSL: connection from home to ISP is wireless instead of a physical cable
* Often used in rural environments where DSL or cable service not available



## Wireless Broadband

* Same cellular technology to access internet via smartphone or tablet
* Antenna installed outside home providing either wireless or wired connectivity for devices in the home
* In some areas competing directly with DSL and cable services



## Common External Security Threats

* Viruses, Worms and Trojan Horses
* Spyware and Adware
* Zero-day attacks
* Hacker attacks
* Denial of service attacks
* Data interception and theft
* Identity theft



## Internal Security Threats

* Data breaches because of internal users of the network
    * Lost or stolen devices
    * Accidental misuse by employees
    * Malicious employees
    * Corporate data much more vulnerable since BYOD



## Required Security Components for Home or Small Office Network

* Antivirus and Antispyware
    * Protection against infection by malicious software
* Firewall filtering
    * Block unauthorized access
    * May include host-based firewall system
    * May include basic filtering system



## Required Security Components for Larger Networks

* Dedicated Firewall System
    * More advanced firewall capabilities
    * Filter large amounts of traffic with higher granularity
* Access Control Lists (ACL)
    * Filter access and traffic forwarding
* Intrusion Prevention Systems (IPS)
    * Identify fast-spreading threats
    * e.g. Zero-day attacks
* Virtual Private Networks (VPN)
    * Provide secure access to remote workers



## What does a well-planned Network Technology Architecture ensure?

* Connection of any device across any combination of networks
* Higher cost efficiency by integrating network security and management
* Improved business processes



