## Distributed systems

A distributed system is a collection of software components that are disigned to work together ecen though they're on separete servers.

Distributed systems, also rederrred to as distrubuted computing or distributed database, utilize different nodes to interact and synchronize over a shared network. These node con also represent independent software processes or other recursive encapsulated systems. They often represent independent physical hardware items as well, such as servers. Distributed systems work to elimanate system bottlenecks ans single points of failure.

A common example of a distribued system would be a website that contains:
    - `Presentation logic` - responsible for displaying the user interface and handling user interactions.
    
    - `Business logic` - manages the application's rules and processes, ensuring proper data handling and functionality.

    - `Database engine` - sores and retrives data used by the website.

    - `Web server` - serves as the intermediary between the user's browser and the various components.

All od these items could be run on a single server, but it is a common to run each component on separete servers for redeundancy and fault tolerance.

### Key characteritstics of a distributed system:

Distributed computind systems have the following characteristics:

    - `Resource sharing` - A distributed system mau share hardware, software or data.

    - `Error detection` - Erros and inefficiencies can be more easily detected.

    - `Transparency` - A nose in the system can interact and commiunicate with other nodes

    - `Simultaneous processing`- The some function can be processed by multiple machines at once.

    - `Scalability` - If more machines are added, the computation and processing power can increase as needed.

    - `Heterogeneity` - The majority of distributed systems are asynchronous nodes and components that use various operating systems, middleware, software and hardware which make it possible to expand or add new components.
    
Distributes systems are used in various applicaions and scenarios, including cloud computing, web services, peer-to-peer networks, content delivery nerworks (CDNs), grid computing and more. 

The enable organizations to harness the power of multiple machines and locations to achieve high performance, fault tolerance and scalability in their computing environments.

However, designing and maniging a distributed system can be complex, requiring careful considerations of communications protocols, data consistency, and fault-tolerance strategies.

Let's take a look at the advantages and disadvantages of using a distributed system.

### Adavantages of using a distributed system:

Distributed computing systems have the following advantages:

- `Flexibility` - You can tune characteristics of each sercer to the component that it will be hosting.

    For example, an application server might need more memory or CPU; a database server needs more dis and I/O throughput.

- `Large volume` - You can run multiple copies of components for fault tolerance or to handle higher amounts of traffic. 

- `Redundancy of nodes` - A distributed system's nodes provide redundancy so that if one fails, there are other nodes available to step in and take its place. 

- `Fault tolerance` - By lowering the risks associated with having a single point of failure, distributed systems improve dependability and fault tolerance.


### Disadvantages of a distributed system
Distributed computing systems have the following disadvantages:

- `Increased complexity` - Compared to conventional computer environments, distributed systems are more difficult to design, administer, and comprehend.

- `Extra work` - Components have to do some extra work to find each other. 

- `Potential introduction of new problems` - Network problems could introduce a new point of failure into your application.

- `Potential introduction of delays` - The network could also introduce some delays.

- `Increased costs` - In contrast to centralized systems, distributed systems' scalability enables managers to quickly add more capacity as needed, which can potentially raise expenses.

**On one hand**, if you are designing an application that needs to scale, you should build in some awareness of distributed systems architecture from the beginning. 

You should not assume that everything is on the same server as you. Try to find some way for each component to discover the others (anything from a configuration file, to a service catalog, to a full service mesh). 

**On the other hand**, don’t overcomplicate things before you need to. Overcomplicated designs can be fragile and hard to maintain in the long term.

## Key takeaways
Distributed systems are crucial in various applications, but require careful design and management to address their complexities and potential challenges.  

- `Definition of distributed systems`

     A distributed system is a collection of software components that collaborate across separate servers or nodes, often using a shared network. These systems aim to eliminate bottlenecks and single points of failure by distributing tasks and functions across multiple components.

- `Characteristics of distributed systems`

     Distributed computing systems exhibit several key characteristics, including resource sharing, error detection, transparency, simultaneous processing, scalability, and heterogeneity.

- `Advantages and disadvantages`

     Distributed systems offer advantages such as flexibility, handling large volumes of traffic, redundancy of nodes, and fault tolerance. However, they also come with disadvantages like increased complexity, the need for extra work to locate components, potential introduction of new problems and delays due to network issues, and increased costs associated with scalability.