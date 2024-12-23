# RESTful APIs

RESTful APIs were originally conceptualized by Roy Thomas Fielding in his 2000 PhD thesis. Unlike APIs which directly open up ports to the entire internet and directly connect, RESTful APIs rely on the HTTP protocol. The HTTP protocol, in turn, can be further secured using HTTPS, and API endpoints can authenticate users via authorization tokens, API keys, or other security mechanisms. 

**RESTful APIs use HTTP requests to perform CRUD (create, read, update, delete) operations on resources.**

## RESTful methods

RESTful APIs work by associating methods (functions) with resources. Some of the most commonly used [HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) are:

- [`GET:`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET) The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.

- [`HEAD:`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD) The HEAD method asks for a response identical to a GET request, but without the response body.

- [`POST:`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST) The POST method submits an entity to the specified resource, often causing a change in state or side effects on the server.

- [`PUT:`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT) The PUT method replaces all current representations of the target resource with the request payload.

You can use GET to obtain information (called a “request”) from a RESTful API endpoint, which would deliver a replay from the endpoint (called a “response”). 

Each type of response has a three-digit code associated with it; these are [HTTP response codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status). 

You might already be familiar with a 404 (not found) response. If a request succeeds, the response status code is 200, and the response will contain a message payload, typically JSON (JavaScript Object Notation). 

It is important to note that RESTful APIs almost always use JSON, but RESTful APIs can also be used to send and receive files, as well as stream data. 


## JSON
`JSON` is a data-interchange format used in RESTful APIs to facilitate communication between clients and servers. 

In RESTful services, JSON serves as the standard payload format for transmitting data. When a client makes a request, the server processes it and sends back a response, often in JSON format. 

This structured format allows for easy parsing, ensuring both the server and client can interpret the data consistently. With its key-value pairs, JSON is both human readable and machine friendly, making it a popular choice for web-based APIs.

## Additional protection
Another important thing to note is that RESTful APIs provide a layer of protection over existing cloud assets, such as a database. 

Instead of allowing the entire internet to query your database, you can put an API in front of it and **allow the API to serve as an intermediary**: an endpoint associated with that resource. 

You can then force authentication using a `JavaScript Web Token (JWT`) or a `third-party authentication provider`. This layer of protection not only provides security, but it also separates control logic from data, so that rate-limiting, usage analytics, and caching can be added on top to improve quality of service.

## Compatibility 
Lastly, RESTful APIs are callable from any programming language that can support HTTP or HTTPS. This includes Python but also C#, JavaScript, Swift, Go, and many others. RESTful APIs, relying on only HTTP, allow any modern computers to talk to each other. 

## Key takeaways
RESTful APIs are a fundamental and versatile part of web development. Knowing how to design, consume, and work with them is essential for building modern web applications, ensuring they can communicate effectively with other services.

