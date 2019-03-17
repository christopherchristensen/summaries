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



## Apache Kafka®

* Distributed Streaming Platform

* Used for
  * building real-time data pipelines
  * streaming apps
* Horizontally scalable
* Fault-Tolerant
* Fast



Apache Kafka is



## Keywords

- Lambda Architecture (http://lambda-architecture.net/)
- Hadoop



## Source

* Posta, C. (Unknown) https://techbeacon.com/app-dev-testing/what-apache-kafka-why-it-so-popular-should-you-use-it
* Apache Kafka (Unknown) https://kafka.apache.org/intro



# Questions & Answers

1. Are there any serious downsides to not having individual message IDs?
2. Messages are addressed by their offset in the log. How exactly is this done?
3. When should you use Kafka and when not?
4. Are there any danger to Kafka?
   * Duplication assures that issued messages which are available are absorbed in the case of any appliance mistake, plan fault or recurrent software promotions
5. What is an offset exactly?
6. What are the main advantages of Apache Kafka?
   * High-Throughpu
   * Low Latency
   * Fault-Tolerant
   * Durability
   * Scalability
7. What is the difference between Kafka and Flume?
   * Kafka can replicate the events
   * Flume doesn't replicate the events