# Network Access



## Types of Connections

* Physical connection to local network needed for network communications
* Physical connection can be
  * wireless
  * wired



## Network Interface Cards

* NICs
* connect device to network
* used for **wired** connection
* Wireless Local Area Network (WLAN) NICs for **wireless** connection



## Purpose of Physical Layer

* Provides the means to transport bits that make up a data link layer frame across the network media
* Accepts complete frame from data link layer and encodes it as a series of signals that are transmitted onto the local media
* Encoded bits that comprise a frame are received by
  * end device
  * intermediate device



## 3 Basic Forms of Network Media

* Electrical Signals (Copper cable)
* Light Pulse (Fiber-optic cable)
* Microwave Signals (Wireless)



## Physical Layer Standards

* International Organization for Standardization (ISO)
* Telecommunications Industry Association / Electronic Industries Association (TIA/EIA)
* International Telecommunication Union (ITU)
* American National Standards Institute (ANSI)
* Institute of Electrical und Electronics Engineers (IEEE)



## Physical Layer Functions

* Encoding
  * Converting stream of data bits into predefined "code"
* Signaling Method
  * Method of representation bits
  * Physical layer standards must define what type of signal represents a `1` and `0` 
  * Long pulse might represent `1` and short a `0`



## Modulation

* process where characteristics of one wave (signal) modifies another wave (carrier)
* $$\text{Modulation Wave} + \text{Carrier Signal} = \text{Signal}$$ (e.g. AM / FM)



> TODO transition $$\to$$ slide 10



## Bandwidth

* Capacity of a medium to carry data
* Digital Bandwidth measures amount of data
  * that can flow from one place to another
  * in a given amount of time
* Sometimes thought of speed that bits travel
  * that is not accurate
  * data always sent at same speed
  * 10Mb/s is the number of bits transmitted per second



## Throughput

* Measure of the transfer of bits across media over given period of time
* Usually doesn't match specified bandwidth
* Implementations due to
  * Amount of traffic
  * Type of traffic
  * Latency created by network devices 
    (between source / destination)
* e.g. Download Speed: 80.78 Mbps, Upload Speed: 8.78 Mbps



## Goodput

* Throughput minus traffic overhead for establishing
  * sessions
  * acknowledgements
  * encapsulation



## Types of Physical Media (Interfaces / Ports)

* FastEthernet Switch Ports
* SHDSL Interface
* Management Ports
* Gigabit Ethernet Interfaces
* USB Type A Connector



## Characteristics of Copper Media

* Transmitted on copper cables (electrical pulses)
* Attenuation
  * The longer signal travels, the more deterioration
* All copper media must follow strict distance limitations
* Electromagnetic interference (EMI) / Radio Frequency Interference (RFI)
  * Distorts and corrupts the data signals being carried by copper media
  * To counter copper cables wrapped in shielding
* Crosstalk
  * Disturbance caused by electric or magnetic fields of signal on one wire to the signal in an adjacent wire
  * To cancel crosstalk opposing circuit wire pairs twisted together



## 3 Types of Copper Media

* Unshielded Twisted-Pair (UTP) cable
* Shielded Twisted-Pair (STP) cable
* Coaxial cable



## Unshielded Twisted-Pair Cable

* most common networking media
* Terminated with RJ-45 connectors
* For interconnecting network hosts with networking devices (e.g. switches)
* Has 4 pairs of color-coded wires
  * wires twisted together
  * to protect against signal interference from other wires
* Color codes aid in cable termination



## How are UTP Cables built?

* Outer Jacket

  * Protects copper wire from physical damage

* Twisted Pair

  * Protects signal from interference

* Color-Coded Plastic Insulation

  * Electrically isolates wires from each other
  * Identifies each pair

  

> Outer Jacket $$\to$$ Twisted-Pair $$\to$$ Color-Coded Plastic Insulation
> (outside to inside)



## Shielded Twisted-Pair Cable

* Provides better noise protection than UTP
* Significantly more expensive
* Difficult to install
* Uses RJ-45 connector
* Techniques of shielding
  * To counter EMI / RFI
* Techniques of twisting
  * To counter crosstalk



## How are STP Cables built?

* Uses 4 pairs of wires

* Each wrapped in foil shield

* Foil shield wrapped in overall metallic braid / foil

  

> Jacket $$\to$$ Braided / Foil Shield $$\to$$ Foil Shields $$\to$$ Twisted-Pairs
> (outside to inside)



## Coaxial Cable

* Replace by UTP cables in modern Ethernet installations
* Used in
  * Wireless Installations (e.g. attach antennas to wireless devices)
  * Cable Internet Installations



## How are Coaxial Cables built?

* Copper conductor to transmit electronic signals

* Flexible plastic insulation layer around copper conductor

* Insulation material surrounded in woven copper braid / metallic foil as

  * Second wire in the circuit
  * Shield for inner conductor

* Entire cable covered with cable jacket to prevent minor physical damage

  

>  Outer Jacket $$\to$$ Braided Copper Shielding $$\to$$ Plastic Insulation $$\to$$ Copper Conductor
> (outside to inside)



## Why are Safety Measure for Copper Media needed?

* Susceptible to fire and electrical hazards



## How to use Copper Media safely

* Separation of data and electrical power cabling must comply with safety codes
* Cables connected correctly
* Installations need damage inspection
* Correctly grounded equipment



## Properties of UTP Cabling

* 4 pairs of color-coded copper wires
  * twisted together
  * encased in flexible plastic sheath
* Small size advantageous during installation
* No shielding to counter effects of EMI / RFI
  * Cancellation: When 2 wires in electrical circuit placed close together, their magnetic fields are exact opposite of each other and cancel out any outside EMI and RFI signals
  * Varies the number of twists per wire pair to further enhance cancellation effects of a paired circuit
* Each colored pair twisted different number of times



## UTP Cabling Standards

* UTP conforms to standards established by TIA / EIA
* Cat 3 Cable
  * Voice communication
  * Most often phone lines
* Cat 5 and 5e Cable
  * Data transmission
  * Cat5 supports 100 Mb/s 
    (can support 1000 Mb/s but not recommended)
  * Cat5e supports 1000 Mb/s
* Cat 6 Cable
  * Data transmission
  * Added separator between each pair of wires for higher speeds
  * Support 1000 Mb/s - 10Gb/s
    (10 Gb/s not recommended)



## UTP Connectors

* Cable terminated with RJ-45 connector
* TIA/EIA-568 
  * Describes wire color codes to pin assignments (pinouts)
  * For Ethernet cables
* RJ-45 connector
  * Male component
  * Crimped at end of cable
* Socket
  * Female component
    (of a network device, wall, cubicle partition outlet or path panel)



## Why do Copper Media Terminations need High Quality?

* Optimum performance with current / future network technologies



## Types of UTP Cables

* Ethernet Straight-Through
  * Both ends T568A or both ends T568B
  * Connects Network to network device (switch, hub, …)
* Ethernet Crossover
  * One end T568A, other end T568B
  * Connects two network hosts
  * Connects two network intermediary devices 
    (switch to switch, router to router)
* Rollover
  * Cisco proprietary
  * Connects workstation serial port to router console port using an adapter



## Testing UTP Cables

* UTP Testing Parameters
  * Wire map
  * Cable length
  * Signal loss due to attenuation
  * Crosstalk



## In what Types of Industries is Fiber Optic Cabling used?

* Enterprise Networks
* Fiber-to-the-Home (FTTH)
* Long-Haul Networks
* Submarine Cable Networks



## Properties of Fiber Optic Cabling

* Transmits data over longer distances and at higher bandwidths
* Transmits signals with less attenuation
* Completely immune to EMI / RFI
* Used to interconnect network devices
* Flexible, but extremely thin, transparent strand of very pure glass not much bigger than human hair
* Bits encoded on fiber as light pulses



## How are Fiber Optic Cables built?

* Jacket
  * Protects against abrasion, moisture, other contaminants
  * Composition varies depending on cable usage
* Strengthening Matherial
  * Surrounds the buffer
  * Prevents fiber cable from being stretched when pulled
  * Often same material as bulletproof vests
* Buffer
  * Shield core and cladding from damage
* Cladding
  * Like a mirror
  * Reflects light back in the core of the fiber
  * Keeps light in core as it travels down the fiber
* Core
  * Light transmission element at center of optical fiber
  * Typically silica or glass
  * Light pulses travel through fiber core
* Jacket $$\to$$ Strenghthening Material $$\to$$ Buffer $$\to$$ Cladding $$\to$$ Core



## Types of Fiber Media

* Single Mode
* Multimode



## Single Mode Fiber Media

* Produces single straight path for light
* Build (outside to inside)
  * Polymeric coating
  * Glass Cladding 125 microns diameter
  * Glass Core = 9 microns
* Small core
* Less dispersion
* Suited for long distance apps
* Uses lasers as light source
* Commonly used with campus backbones
  (for distances of several 1000m)



## Multimode Fiber Media

* Allow multiple paths for light
* Build (outside to inside)
  * Coating
  * Glass Cladding 125 microns diameter
  * Glass Core = 50/62.5 microns
* Larger core
* Greater dispersion, therefore loss of signal
* Suited for long distance apps 
  (shorter than single mode)
* LEDs as light source
* Commonly used with LANs or distances of couple 100m within a campus network



## Fiber-Optic Connectors

>  light only travels in one direction, therefore two fibers are always required

* Straight-Tip (ST) Connectors
  * One of the first connector types used
  * Locks securely with a "twist-on/twist-off"
* Subscriber Connectors (SC)
  * Also square or standard connector
  * Push-pull mechanism for positive insertion
  * Used with multimode and single-mode fiber
* 