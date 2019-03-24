# Configure a Network Operating System



## Operating System

* Low-level software that 
  * Supports a computer's basic functions
  * Such as scheduling tasks and controlling peripherals
* All devices require an operating system



## Network Operating System

* OS for switches, routers, access points, and firewalls



## What does an Operating System consist of?

* OS Shell
  * Command-line interface (CLI) or 
  * Graphical user interface (GUI, e.g. Windows, OS X) 
  * Enables a user to interact with the system
* OS Kernel
  * Communicates directly with hardware
  * Manages how hardware resources are used to meet software requirement
* Hardware
  * Physical part of a computer including underlying electronics



## Purpose of OS

* GUI enables user to
  * Use a mouse to make selections and run programs
  * Enter text and text-based commands
  * View output on a monitor
* CLI enables network technician to
  * Use keyboard to run CLI-based network programs
  * Use keyboard to enter text and text-based commands
  * View output on a monitor
  * e.g. on a Cisco IOS switch or router 



> * All devices come with default IOS and feature set
> * It's possible to upgrade the IOS version or feature set 
>   (e.g. download from cisco.com)



## Why are Network Devices typically accessed via CLI?

* GUIs don't always provide all of features available
* GUIs can also fail, crash, or simply not operate as specified
* CLI is less resource intensive and very stable when compared to a GUI



## Types of Cisco IOS

* IOS for switches, routers, and other Cisco networking devices
* IOS numbered versions for a given Cisco networking devices



## Methods to Access IOS

* Console Port
  * Out-of-band serial port 
  * Primarily for management purposes (initial configuration of router)
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

* Enable users to log on and get direct access to legacy programs in a mainframe OS
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

* User EXEC `>`
  * Limited number of basic monitoring commands allowed
  * By default, no authentication required, but should be secured
* Privileged EXEC `#`
  * Execution of configuration and management commands allowed
  * Also called “enable mode” because it requires the `enable` user EXEC command
  * By default, no authentication required, but should be secured



## Configuration Command Modes

* Primary configuration mode 
  * Called global configuration or global config
  * `configure terminal` to access mode
  * Changes affect operation of device
* Sub configuration modes can be accessed from global config mode
* Each of these modes allow config of particular part / function of the IOS device



## Sub Configuration Modes

* Interface mode: configure on of the network interfaces
* Line mode: configure console, AUX, Telnet or SSH access



## Navigate Between IOS Modes

* `enable` : Enter privileged EXEC mode
* `disable` : Return to user EXEC mode
* `configure terminal` : enter config mode
* `interface fa0/1` : enter interface sub-config mode 
  (e.g. **fa**st interface bank **0 / 1**. interface)
* `exit` : Exit out of any mode (from specific to previous more general mode)
* `end` : Exit a sub-config mode and return to privileged EXEC mode
* `^z` : Exit a sub-config mode and return to privileged EXEC mode



## Basic IOS Command Structure

* `Switch>show ip protocols`
* Prompt: `Switch>`
* Command: `show`
* Keyword / Argument: `protocols`



## Keyword

* Specific parameter defined in the OS



## Argument

* Not predefined
* Value or variable defined by the user



## IOS Command Convention

> Used when describing the use of commands

* **boldface**: Commands / keywords you enter literally as shown
* *italics*: Arguments for which you supply values
* \[x\]: Optional element
* \{x\}: Required element
* \[x \{y | z}]: Required choice in optional element



## IOS Help Features

* Context-Sensitive Help
    * Quickly find available commands
    * Varies in each command mode
    * Type `?` in the CLI
* Command Syntax Check
    * Verifies that valid command was entered
    * When command entered, CLI interpreter validates command
    * From left to right



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



