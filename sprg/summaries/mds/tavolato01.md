# Security Requirements



## Security

* Defense of computers against
  * instrusion
  * unauthorized use of resources
  * humans with malicious or criminal intent



## Safety

* Avoiding hazardous situations
* Alerting the correct systems if situation becomes unsafe
* Defending humans / environment against malfunctioning systems



## Important Notes about Security

Security

- is not a programming problem only
- must be considered from the beginning on
- is relevant in all phases of software development
- can't be fixed by using special methods / tools
- can't be seen isolated from deployment / operations



## Security vs. Safety

* No strict borderline between both concepts
* Security breaches may have serious safety consequences



## Perimeter Security

* Measures to protect external perimeter of a system
  * Access Control
  * Firewalls
  * Anti Virus Software
* Not sufficient by today's standards (medieval concept of yesterday)



## Why is Perimeter Security not sufficient anymore?

* More applications offer direct access to external users
* Modern applications often considered to be doors into OS ($$\sim$$ wall)



## Why Perimeter Security often focused on before Insecurities in Software?

> Bad Practice

* Secure coding often not considered to be important in the past
* Often, security professionals $$\neq$$ software developers (full insight into software vulnerabilities missing)
* Functionality often focus of software developers
* Vendors want quick time to market, often no time for proper security architecture, design and testing
* Customers used to flaws and regular security updates (patches)
* Customers can't control software flaws, therefore depend upon perimeter protection



## How to Intrusion happens

1. Infection
2. Exploit
3. Payload



## Malware

> **Mal**icious Soft**ware**

* Software doing something the user / owner of the computer doesn't like

* Special forms of malware
  * Virus
  * Worm
  * Trojan



## Infection

* How malware gets into system
* When user trusts a piece of software (with malware)



## Exploit

> "to use something to one's own advantage"

* Taking advantage of weak points in systems / applications
* Piece of software, chunk of data, or a sequence of commands 
  * that takes advantage of a bug / vulnerability 
  * to cause unintended / unanticipated behavior on computer software, hardware, or something electronic



## Vulnerabilities

* Programming errors (direct or indirect)
* Vulnerabilities lead to exploits
* Attacker must have applicable tool / technique that can connect to a system weakness (attack surface)



## Example of an Indirect Error

* Flawed handling of memory management
  * may render a system vulnerable to denial-of-service attacks
  * doesn't effect system's functionality therefore may remain undetected during testing



## Can Vulnerabilities and Exploits be prevented?

* Every system of minimum complexity contains errors
* No way of completely preventing it
* Relative security can be reached by
  * clean and intelligent software development
  * including security considerations in all phases of a system



## Ways to improve Security

* Security and functionality need to be designed and integrated into the individual phases of a development life cycle
* Security considerations need to be interlaced into product core
* Understand security needs, implement the right controls and test thoroughly



## Security Cost Considerations

* The higher the security efforts, the lower the costs for security breaches
* The higher the security efforts, the higher the costs for security measures
* With the right amount of security efforts the total costs can be kept at a minimum



## Attributes of Software Security

* Quality
* Correctness
* Availability
* Robustness
* Verifiability
* Reliability
* Safety



## What does Software Engineering deal with?

* Cost-effective development of high-quality software

* …of software systems

  * Construction...

  * Control...
  * Rollout...
  * Operation and maintenance...



## Scales of Software Project

* Trivial
  * Staff: 1, 4-6 Weeks, Lines of code < 500
  * e.g. Simple administrative programs
* Small
  * Staff: 1, 1-6 Months, Lines of code: 1'000-2'000
  * e.g. Small commercial applications
* Medium
  * Staff: 2-5, 1-2 Years, Lines of code: 10'000-50'000
  * e.g. Warehouse management
* Big
  * Staff: 5-20, 2-3 Years, Lines of code: 50'000-100'000
  * e.g. Small operating system
* Very Big
  * Staff: 100-1'000, 4-5 Years, Lines of code: ca. 1'000'000
  * e.g. Database system
* Extremely Big
  * Staff: 2'000-5'000, 5-10 years, Lines of code > 10'000'000
  * e.g. Air traffic control



## Attributes of Software Quality

* Correctness / Verifiability
* Reliability
* Robustness
* User-Friendliness
* Maintainability
* High Performant
* Portability / Compatability
* Reusability



## Software Quality

* Features of software necessary for meeting requirements
* Features of security and safety (partly competing)
* Importance of features dependant on project



## Development- vs. Maintenance-Costs

* Cost-effective $$=$$ ca. 20% Dev / 80% Maintenance



## Where do bugs come from?

* 56% Analysis and Specification
* 27% Design
* 7% Coding
* 10% Other



## How much do Bugs cost in Relation to their Source?

* 82% Analysis and Specification
* 13% Design
* 1% Coding
* 4% Other



## Process Models

> Description of a process

* Activities must be 
  * defined exactly
  * arranged along a time scale
* Process model is the starting point for
  * project planning
  * project management
* Process model must be adapted to
  * the project
  * the development environment (personnel / tools)



## Different Process Models

* Waterfall
* Prototyping
* Unified Process
* Agile Development
* SCRUM
* $$\to$$ Devops



## Waterfall

* Strict linear sequence of activities
* Simple definition of milestones
* Relatively easy project management
* Little freedom for developers
* Problems
  * Not flexible



## Prototyping

* Iterative
* Flexible reactions to user requests possible
* More freedom for developers
* Problems
  * Hard to manage (hard to define milestones)
  * "quick-and-dirty" solutions stay in product forever



## Unified Process

* Compromise between Waterfall and Prototyping
* Iterative
* Flexible reaction to user requests possible
* Little freedom for developers
* Function-Oriented
* Problems
  * Often too slow, complicated, inefficient (cumbersome)



## Agile Development

* Agile Values
  * Individuals / Interactions $$>$$ Processes / Tools
  * Working Programs $$>$$ Elaborate Documentation
  * Constant Cooperations with Customer $$>$$ Contracts
  * Courage / Openness for Change $$>$$ Obeying fixed plans
* Agile Principles
  * Reuse existing ressources
  * KISS
  * Functional / Customer-Oriented
  * Collective Code Ownership
* Agile Methods
  * Pair Programming
  * Testdriven Programming
  * Refactoring
  * ...



## SCRUM

* Process Model for Agile Methods

* Time-Oriented

  

## DevOps

* Build
* Deploy
* Test
* Release
* Build