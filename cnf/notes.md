# Additional Notes



## Why do we need to load the OS on boot?

- To load the data from the slower flash card into the RAM



## HAL

- hardware abstraction layer
- a layer of programming that 
  - allows an operating system to interact with a hardware device 
  - at a general or abstract level 
  - rather than at a detailed hardware level



## Cisco Server Monitoring

* Cisco Server have a monitoring layer



## Persisting Server Settings after Configuration

* Run these two commands
  * `copy run config`
  * `startup config`
* configuration is in RAM
* when unpluggin or power cut all configurations in RAM are lost
* running commands above save configuration in non-volatile memory



## Tipp: Manual Backup of Server Configuration

* Configuration is saved in a text file
* Copy and paste text file to another computer (TADAA!)



## K9

- secure shell supported