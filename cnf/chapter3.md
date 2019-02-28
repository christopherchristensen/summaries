# Network Protocols and Communication



## 3 Elements of Communication

> * All communication methods have three elements in common
> * Rules or protocols govern all methods of communication

* Source (sender)
* Destination (receiver)
* Channel (media)



## What are Protocols for?

* necessary for effective communication



## What do Protocols include?

* An identified sender and receiver
* Common language and grammar
* Speed and timing of delivery
* Confirmation or acknowledgment requirements



## What do Protocols in Network Communication define?

* Message encoding
* Message delivery options
* Message Formatting and Encapsulation
* Message Timing
* Message Size



## Message Encoding

* Encoding between hosts in appropriate format for medium
* Messages first converted into bits by the sending host
* Each bit encoded into
  * pattern of sounds
  * light waves
  * electrical impulses 
  * depending on network media
* Destination host receives and decodes signals 
  * in order to interpret the message



## Message Formatting and Encapsulation

* agreed format for letters / addressing letters 
  (required for proper delivery)
* Encapsulation: putting letter into the addressed envelope
* Each computer message is
  * encapsulated in a specific format (frame)
  * before sent over network
* Frame 
  * acts like an envelope 
  * providing destination address and source address



## Message Size

* Humans break long messages into smaller parts or sentences
* Long messages broken into smaller pieces to travel across network
* Each piece is sent in separate frame
* Each frame has own addressing information
* Receiving host reconstructs multiple frames into original message



## Message Timing

* Access Method
  * when to begin sending messages
  * how to respond on collisions
* Flow Control
  * negotiate correct timing
  * avoid overwhelming destination
  * ensure information is received
* Response Timeout
  * rules that specify how long to wait for responses
  * what action to take if a response timeout occurs



## Message Delivery Options

* Unicast Message (One-to-one)
* Multicast Message (One-to-many)
* Broadcast Message (One-to-all)



M!12

M!13-17

## TCP/IP Communication Process (Sending)

* encapsulation procedure (web to client)

  1. Webserver prepares HTML page

  2. HTTP application layer protocol sends data to Transport Layer

  3. Transport Layer breaks data into segments and identifies each
  4. IP source and destination addresses are added (create IP Packet)
  5. Ethernet information added creating Ethernet Frame (or data link frame)
  6. Frame delivered to nearest router along path towards web client. Each router adds new data link information before forwarding the packet



## TCP/IP Communication Process (Receiving)

* decapsulation procedure 
  (remove each protocol header in opposite order)
  1. Remove Ethernet header
  2. Remove IP header
  3. Remove Transport Layer
  4. Process HTTP information and send to client browser



## Open Standards

* encourage
  * interoperability
  * competition
  * innovation