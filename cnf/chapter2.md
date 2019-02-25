# Configure a Network Operating System



## Operating System

* low-level software that 
  * supports a computer's basic functions
  * such as scheduling tasks and controlling peripherals
  * all devices require an operating system



## HAL

* Hardware Abstraction Layer
* Zwischenschicht Hardware / software
* allows computer operating system to interact with 
  * hardware device at a general or abstract level 
  * rather than at a detailed hardware level



## Warum wird OS geladen?

* Um Daten von langsameren Flash-Karte ins RAM zu laden



## What does an operating system consist of?

* OS Shell
  * command-line interface (CLI) or 
  * a graphical user interface (GUI) 
  * enables a user to interface with applications
* OS Kernel
  * communicates directly with the hardware
  * manages how hardware resources are used to meet software requirement
* Hardware
  * physical part of a computer including underlying electronics



## Purpose of OS

* GUI enables user to
  * Use a mouse to make selections and run programs
  * Enter text and text-based commands
* CLI enables network technician to
  * e.g. on a Cisco IOS switch or router 
  * use keyboard to run CLI-based network programs
  * use keyboard to enter text and text-based commands



> * All devices come with default IOS and feature set
> * It is possible to upgrade the IOS version or feature set 
>   (e.g. download from cisco.com)



## K9

* Secure Shell tauglich



## Types of Cisco IOS

* IOS for switches, routers, and other Cisco networking devices
* IOS numbered versions for a given Cisco networking devices



## Methods to Access IOS

* Console Port
  * Out-of-band serial port 
  * primarily for management purposes (initial configuration of router)
* Secure Shell (SSH)
  * Inband method for remotely and securely establishing CLI session over network
  * User authentication, passwords, and commands sent over the network are encrypted
  * best practice, use SSH (Version 2) instead of Telnet whenever possible
* Telnet
  *  Inband interfaces remotely establishing a CLI session through a virtual interface, over a network. User authentication, passwords, and commands are sent over the network in plaintext
* AUX port 
  * older method of establishing a CLI session remotely 
  * via a telephone dialup connection using a modem



