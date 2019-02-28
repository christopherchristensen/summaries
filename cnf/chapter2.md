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



## Terminal Emulation Program

* give users ability to log on and get direct access to legacy programs in a mainframe operating system
* Regardless of access method, a terminal emulation program will be required
* (PuTTY, Tera Term, SecureCRT, and OS X Terminal)



## What are CISCO Operation Modes?

* Cisco IOS modes use a hierarchical command structure
* Each mode has a distinctive prompt
* used to accomplish particular tasks with a specific set of commands that are available only to that mode



## Primary Command Modes

* user EXEC `>`
  * allows only a limited number of basic monitoring commands
  * By default, there is no authentication required to access the user EXEC mode but it should be secured
* privileged EXEC `#`
  * allows the execution of configuration and management commands
  * referred to as “enable mode” because it requires the enable user EXEC command
  * By default, there is no authentication required to access the user EXEC mode but it should be secured



## Configuration Command Modes

* primary configuration mode is called global configuration or simply, global config



!Missing 12 - 27



## Encrypt Passwords

* startup-config and running-config files display most passwords in plaintext
* This is a security threat because anyone can see the passwords if they have access to these files
* `service password-encryption` 
  * global config command to encrypt all passwords
* The command applies weak encryption to all unencrypted passwords
* However, it does stop “shoulder surfing”



## Banner Messages

* displayed when someone attempts to gain access to a device
* important part of the legal process in the event that someone is prosecuted for breaking into a device
* `banner motd delimiter message delimiter`



Missing! 30



## Save Running Configuration File

* Cisco devices use a running configuration file and a startup configuration file
* `show running-config`
* TODO



## Alter Running Configuration

* TODO



