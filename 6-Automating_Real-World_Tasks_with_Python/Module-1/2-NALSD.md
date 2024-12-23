# NALSD

NALSD, also known as non-abstract large system design, is a discipline and a process invented by Google that aims to give SREs (site reliability engineers) the ability to assess, design, and evaluate large systems. 

NALSD is the process of designing complex and substantial systems, such as software applications, hardware systems, or even organizational structures, with a focus on practical, concrete details rather than on abstract or theoretical concepts. NALSD emphasizes the tangible and real-world aspects of system design and implementation. 

NALSD combines elements of capacity planning, component isolation, and graceful system degradation that are crucial to highly available production systems. 

## Key characteristics of NALSD

NALSD requires DevOps teams to think about scale and resilience during the design process. It separates the design process into two phases. 

The two phases have the following key characteristics: 

### Phase 1: Technical design
Phase 1 is an iterative process that involves multiple rounds of design and refinement. It's common to create prototypes, conduct feasibility studies, and gather feedback from stakeholders to continuously refine the technical design. In this phase, the team tries to answer two questions about the proposed design:

- Is it possible? Will the design even work?

- Can we do better? Can we make it faster, simpler, or cheaper?

### Phase 2: Scaling up
In Phase 2, the team assesses whether the system design is feasible at scale. They consider how the system will perform when subjected to significant increases in load. Scalability is essential to ensure that the system can accommodate growth without a dramatic loss of performance. What if you suddenly add a million users to the system? How will the system be able to accommodate a random increase in users?

- Is it feasible? Will it work at scale? Is it cost-effective?

- Is it resilient? What happens if the database goes down? 

- Can we do better? Are there changes or additions that we need to make?

## Three key goals of NALSD
Three of the key goals of NALSD are the following: 

- The first is proper capacity planning. Capacity planning is understanding how to properly size each component and how to properly plan for growth. This goal involves careful monitoring, performance analysis, and prediction of growth trends to prevent resource exhaustion or over-provisioning. Capacity planning is crucial in NALSD design because it involves estimating the required resources (CPU, memory, storage, network bandwidth, etc.) to meet current and future demands.

- The second is component isolation. In NALSD design, a fundamental principle is component isolation, highlighting the importance of designing each element of the system to maximize simplicity, modularity, and independence from one another. The "do one thing and do it well" philosophy encourages developers to create components that have a clear and specific purpose.

- The final goal is graceful degradation. This is the idea that parts of the system should continue to work when another part fails, rather than everything failing at once. For example, in a web application, if a database server becomes unavailable, the system might switch to a read-only mode, allowing users to access existing data while blocking new updates until the database is restored.

## Google’s NALSD Workbook 
The NALSD Workbook was created by Google's SRE team. It is designed to help engineers and developers with the design and architecture of large-scale, reliable systems.

The NALSD Workbook contains valuable insights, best practices, and guidelines for designing and building complex and scalable systems that can handle high loads and remain reliable. Engineers often refer to such resources to improve their system design skills and create more robust and efficient software and infrastructure. If you're interested in learning more about large-scale system design, this workbook is a fantastic resource and can be found [here](https://static.googleusercontent.com/media/sre.google/en//static/pdf/nalsd-workbook-letter.pdf).


## Key takeaways
Here are three key takeaways from this reading on NALSD:

- `Definition of NALSD:` NALSD, or Non-Abstract Large System Design, is a discipline and process introduced by Google, primarily aimed at empowering site reliability engineers (SREs) to assess, design, and evaluate large-scale systems. 

- `Two phases of NALSD:` Phase 1 involves continuous refinement through feedback, prototyping, and feasibility studies. It seeks to answer: "Is it possible?" and "Can we do better?" Phase 2 evaluates the system's feasibility and resilience at scale, considering how it will perform under significant load increases. 

- `Three key goals of NALSD:` Proper capacity planning, component isolation, and graceful degradation are the three goals of NALSD. These goals are in place so that the system can continue functioning even when individual parts fail.

As previously mentioned, if you are interested in learning more about NALSD, review Google’s [Non-Abstract Large System Design Workbook](https://static.googleusercontent.com/media/sre.google/en//static/pdf/nalsd-workbook-letter.pdf).


