# Configure a Network Operating System



## Operating System

* low-level software that 
  * supports a computer's basic functions
  * such as scheduling tasks and controlling peripherals
  * all devices require an operating system



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



## Types of Cisco IOS

* IOS for switches, routers, and other Cisco networking devices
* IOS numbered versions for a given Cisco networking devices



## Methods to Access IOS

* Console Port
  * Out-of-band serial port 
  * primarily for management purposes (initial configuration of router)
* Secure Shell (SSH)
  * Inband method for remotely and securely establishing CLI session over network
  * User authentication, passwords, and commands are sent encrypted
  * best practice, use SSH (Version 2)
* Telnet
  *  Inband interfaces remotely establishing a CLI session through a virtual interface, over a network. 
  *  User authentication, passwords, and commands are sent in plaintext
* AUX port 
  * older method of establishing a CLI session remotely 
  * via a telephone dialup connection using a modem



## Terminal Emulation Program

* enable users to log on and get direct access to legacy programs in a mainframe OS
* Regardless of access method, a terminal emulation program will be required
* (PuTTY, Tera Term, SecureCRT, and OS X Terminal)



## What are CISCO Operation Modes?

* Modes used to 
  * accomplish particular tasks 
  * with a specific set of commands 
  * that are available only to that mode
* Cisco IOS modes use a hierarchical command structure
* Each mode has a distinctive prompt



## Primary Command Modes

* user EXEC `>`
  * limited number of basic monitoring commands allowed
  * By default, no authentication required, but should be secured
* privileged EXEC `#`
  * execution of configuration and management commands allowed
  * also called “enable mode” because it requires the `enable` user EXEC command
  * By default, no authentication required, but should be secured



## Configuration Command Modes

* primary configuration mode 
  * called global configuration or global config
  * `configure terminal` to access mode
  * changes affect operation of device
* sub configuration modes can be accessed from global config mode
* each of these modes allow config of particular part / function of the IOS device



## Sub Configuration Modes

* Interface mode: configure on of the network interfaces
* Line mode: configure console, AUX, Telnet or SSH access



## Navigate Between IOS Modes

* `enable` : enter privileged EXEC mode
* `configure terminal` : enter config mode
* `interface fa0/1` : enter interface sub-config mode 
  (e.g. **fa**st interface bank **0 / 1**. interface)
* `exit` : exit out of any mode (from specific to previous more general mode)
* `end` : exit a sub-config mode and return to privileged EXEC mode
* `^z` : exit a sub-config mode and return to privileged EXEC mode



## Basic IOS Command Structure





15 - 28!





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


