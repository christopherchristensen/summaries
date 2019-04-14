---
title: Evolution of The Container Technology
subtitle: Preparation
author: Christopher Christensen
modul: INFKOL
documentclass: scrartcl
---

# Summary

Docker Inc. calls Docker a platform to develop, deploy and run applications with containers. It use Linux containers which is called containerization. Applications are deployed on to these containers. Some advantages of containers are listed as follows (Docker Inc. 2019):

- Flexible
- Lightweight
- Interchangeable
- Portable
- Scalable
- Stackable

## Containers
Docker runs an image that launches a container. These images are executable packages that have all configurations, code, runtime, libraries and environment variables that you need to provide in order to run your application. Each container then represents a runtime instance of that image (Docker Inc. 2019). 

## Containers vs. VMs
The differences are listed in this table (Wong 2016).

- Containers
    - Relies on underlying OS to provide basic services
    - Virtual-Memory support for isolation
    - Lower overhead
    - Container systems typically target environments where thousands of containers are in play
    - Service isolation between containers, therefore can have limited resource access
    - Abstract OS
- Virtual Machines
    - VM runs software on the bare metal hardware, whilst isolating it from the real hardware
    - VM are run on hypervisors that use their own OS
    - Use hardware VM support
    - Larger overhead
    - Abstract machines that use device drivers

# Questions

1. Why has Docker become so popular?
2. What are the limits of Docker?
3. What are the downsides of Docker?
4. Where is Docker not a smart idea?
5. Are there any vulnerabilities to consider when using Docker?

# Sources

- Docker Inc., _Get Started, Part 1: Orientation and setup_, 2019, [docs.docker.com](https://docs.docker.com/get-started/)
- William G. Wong, _What's the Difference Between Containers and Virtual Machines?_, 2016, [electronicdesign.com](https://www.electronicdesign.com/dev-tools/what-s-difference-between-containers-and-virtual-machines)
