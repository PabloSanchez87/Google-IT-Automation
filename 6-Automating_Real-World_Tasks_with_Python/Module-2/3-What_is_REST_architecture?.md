# What is REST architecture?

**REST stands for Representational State Transfer**. REST architecture is an architectural style for designing networked applications and web services. It was invented as a standard way for clients and servers to communicate with each other over the internet. 

REST is designed to be stateless, meaning the server does not have to remember any information about the client between requests. Every request carries all the parameters and data needed for the server to satisfy that request.

## Constraints with the REST architecture
The `six constraints or principles of REST` each serve a specific purpose in guiding the design of RESTful systems, contributing to the overall scalability, simplicity, and interoperability of the architecture. The six constraints are:

- `Uniform interface` - There should be consistent methods for clients to access and change resources on the server using standard HTTP (Hypertext Transfer Protocol) conventions. 

- `Stateless` - Every piece of information the server requires to process the request should be within the request. There shouldn't be any leftover information on the server between requests.

- `Cacheable` - Every server response should indicate whether the data can be cached on the client and the length of time is needed to cache the data.

- `Client-server` - The client and server can evolve independently. The REST interface serves as a “contract” between them.

- `Layered system` - An application should be split into layers. Each layer of the application handles a particular concern (data access, business logic, presentation, etc) and acts independently from the other layers.

- `Code on demand (optional)` - Servers can also provide code to be executed on the client. This enables the client to change its behavior dynamically.

## HTTP protocol with REST

REST is also designed to run on top of HTTP. This design enables clients and servers to communicate over the public internet using standard HTTP conventions. Companies will often publish their REST API (Application Programing Interface) so that developers can make use of it. Nearly any programming language is capable of speaking HTTP, so you can use your favorite language, like Python, to make REST API calls.

All interaction between client and server takes place over HTTP, using standard HTTP features: verbs, headers, and data payloads. Almost everything the server needs to know is included in the request URL itself. 

For example, a photo-sharing app might send a series of HTTP requests to a REST API server that look like the following (command is listed first and then the action the command is performing is listed after the dash):

- `GET /api/v1/albums` - get the list of photo albums

- `GET /api/v1/albums/1234/pictures` - get the list of pictures in album 1234

- `GET /api/v1/pictures/5678 `- get the details for picture 5678

- `GET /api/v1/pictures/5678/comments` - get the comments for picture 5678

HTTP allows clients to GET, PUT, and DELETE resources. Clients can also POST queries with complex data, such as performing a search or transferring money between accounts. The PATCH verb allows clients to update a resource by just sending what has changed.

REST APIs often allow the client to adjust their behavior by sending additional headers with the request. Headers might include authentication, enable optional features, or allow the client to request that the server send data in specific formats (e.g. JavaScript Object Notation, JSON, or eXtensible Markup Language).

The client may send data in the body of its request, and the server replies with data in the response body. The format of the data is controlled by a header (see above).

## What is the Richardson Maturity Model?
The `Richardson Maturity Model`, also known as `RMM`, is a framework that categorizes and describes different levels of implementation for RESTful APIs based on their adherence to the six constraints referenced earlier in this reading. RMM is a way of assessing the sophistication of a REST API based on how compliant it is with the REST constraints. 

The `Richardson Maturity Model consists of four levels`, each representing a progressive level of adherence to the principles of REST:

- `Level 0` - A single URI (uniform resource identifier) and a single verb (usually GET or POST)

- `Level 1` - Multiple URIs but still a single verb

- `Level 2` - Makes use of URIs and multiple methods, but is not HATEOAS (Hypermedia as the Engine of Application State)

- `Level 3` - Full HATEOAS

`HATEOAS` indicates that the server’s responses should include hyperlinks for the client to access related resources. 

For example, in the picture gallery app example above, the GET request for albums  should return a list of albums. Each album should include its name, ID, and links to retrieve album details, comments, and pictures. With a full Level 3 REST implementation, the client would not need to hardcode URIs of the resources it needs. The URIs would be discoverable from the server’s responses.

To check out some further information with how to create REST APIs in Python, check out this link [here](https://auth0.com/blog/developing-restful-apis-with-python-and-flask/). If you’re interested in further information for REST APIs with GCP, click on this link [here](https://medium.com/mdblog/creating-a-serverless-rest-api-with-gcp-32cc62188a03). 

## Key Takeaways
REST architecture is based on six key constraints, including a uniform interface for consistent interactions, statelessness for efficient communication, cacheability for improved performance, separation of client and server concerns, layered system organization, and the optional ability for servers to provide executable code to clients. 

REST APIs are often designed to run on top of the HTTP protocol, utilizing standard HTTP features for communication. APIs are difficult to change after they are published and being utilized. Invest the time to create clean, rational, extensible APIs right from the start.

