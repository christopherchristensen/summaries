---
title: Why Kafka data streaming is the future
subtitle: Summary, Questions and Answers
author: Christopher J. Christensen
---



# Summary



## Introduction

* Exchanging data within existing IT-Systems still a hard problem to solve
* Involved data often seen as burden instead of valuable asset
* Talk will discuss challenges of modern IT-Infrastructures
* Data streaming with Apache Kafka is presented
* Examples of how above challenges are addressed with Apache Kafka
* How additional business value is created with Apache Kafka



## Problems exchanging Data within IT-Systems

* Low-latency ingestion of large amounts of event data (Posta, Unknown)
* Existing solutions for ingesting data into offline batch systems 
  * exposed implementation details to downstream users
  * used a push model that could easily overwhelm a consumer
  * were not designed for the real-time use case
* Real-time systems (e.g. traditional messaging queues) 
  * have great delivery guarantees
  * support things such as transactions, protocol mediation, and message consumption tracking
  * are often overkill for many use case
* Fancy machine-learning algorithms without the data, the algorithms are useless
* Getting the data from source systems and reliably moving it around was very difficult, and existing batch-based solutions and enterprise messaging solutions did not solve the problem
* Kafka was developed to be the ingestion backbone for this type of use case



* Complex integrations between backend & frontend ("many lines")
  * a lot of redundancy
* 



## Apache Kafka®

* Distributed Streaming Platform
* Used for
  * building real-time data pipelines
  * streaming apps
* Horizontally scalable
* Fault-Tolerant
* Fast
* True Storage
* Scalability
* Real-time Processing



Not supported

* Transaction Support
* Error Handling (messages stored in dead letter storage)
* Slim Broker



* Distributed streaming platform
  * publish and subscribe of record streams (message queue / topic)
  * store streams of records in a fault-tolerant durable way (database)
  * Process streams of records as they occur 
    (ordering -> hard problem to solve for message queue)
* Other features
  * partitioned topics (can otherwise cause a bottleneck) (scaling)
  * distribution of brokers (scaling)
  * consumer groups (scaling)
  * runs on commodity HW 
    (you don't download and install it, you just start a docker container and run it)
* Load balance partitions by topics
* On partitions there are consumers and kafka only needs to know about there whereabouts. kafka can then ask the consumer where the next message is.

* Kafka Environment
  * Producers (App)
  * Connectors (DB)
  * Stream Processors (Consumer and Producer in One) (App)
  * Consumers (App)
  * Kafka Cluster (Only used for managing messages)
* Other services like Kafka don't always offer true storage
* More based on text-file streaming, they have a format. but you can use byte streams
* Kafka stores messages on disc (so fast storage is needed), also maybe timestamp issues
* Wouldn't put Kafka directly on an Angular Application
* Kafka is really a backend service
* Don't use OAuth or session tokens directly over Kafka
* Don





## Keywords

- Lambda Architecture (http://lambda-architecture.net/)
- Hadoop



## Source

* Posta, C. (Unknown) https://techbeacon.com/app-dev-testing/what-apache-kafka-why-it-so-popular-should-you-use-it
* Apache Kafka (Unknown) https://kafka.apache.org/intro



# Questions & Answers

1. Are there any serious downsides to not having individual message IDs?

   * Messages can land in dead message storage

2. Messages are addressed by their offset in the log. How exactly is this done?

   * Via the order of the messages. The consumers can ask where the next message is.

3. When should you use Kafka and when not?

   * Use: 
     * For instance for streaming applications
     * Credit Card defrauding
     * Generally for big products
   * Don't Use: 
     * In a very simple application where no scaling is needed (overkill)

4. Are there any dangers / pitfalls to Kafka?

   * Is a single point of failure and could also be a risk because the data is all available there. It is regulated via access rights. There is a strong system of private and public keys though, with a lot of additional features. There is also an abstraction layer.

   * Shouldn't use it in synchronized messaging, since Kafka is asynchronous

   * Duplication assures that issued messages which are available are absorbed in the case of any appliance mistake, plan fault or recurrent software promotions
   * Everytime you see a Apache Kafka component you should be scared
   * Timestamps are used for orderings, therefore if the hardware is slow timestamp issues may occur
   * Complexity: 
     * Components: Brokers, Zookeeper, Schema registry, monitoring, persisten storage
     * Configuration: Brokers, Zookeeper, … very many possible configurations
     * Scaling: brings parallelism, many messages on different nodes
     * Transaction: are made even more complex than regular transactions
   * Data Governance: in case of replication of data you have to assign which one has priority, which one is the master (you lose the one truth)

5. What is an offset exactly?

6. What are the main advantages of Apache Kafka?
   * High-Throughput
   * Low Latency
   * Fault-Tolerant
   * Durability
   * Scalability

7. What is the difference between Kafka and Flume?
   * Kafka can replicate the events
   * Flume doesn't replicate the events