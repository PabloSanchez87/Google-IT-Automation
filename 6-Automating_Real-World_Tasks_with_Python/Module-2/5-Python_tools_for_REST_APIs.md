# Python tools for REST APIs

Any programming language can use REST APIs, and of course that includes Python. Python REST API frameworks are toolkits and software libraries that offer the functions and tools needed to build RESTful APIs using the Python programming language. 

Tools for working with REST APIs in Python break down into two categories: client-side tools for consuming REST APIs and server-side frameworks for serving your own REST APIs.

## Client-side
REST API client libraries are designed to simplify calling an API and parsing the responses. You could do all of this with the low-level built-in urllib library, but these tools are designed to make the process much easier.

## Requests
Requests is a third-party Python module that you can easily download and install to simplify sending HTTP requests. It’s easy to use and has been around for a while, so it’s frequently chosen by developers. There are newer derivatives of Requests that are gaining popularity, like HTTPX and AIOHTTP. For a comparison of these three, see [HTTPX vs Requests vs AIOHTTP](https://oxylabs.io/blog/httpx-vs-requests-vs-aiohttp). 

## PycURL
As you advance as a developer, you might want to try a client library like PycURL, which offers concurrent connections and can be much faster than Requests. Note that Pycurl is more complicated to install than Requests, and it is not written in pure Python, which can make it harder to learn. 

## Server-side
On the server side, REST API frameworks are designed to make it easier for you to write, run, and debug REST services by eliminating a lot of the boilerplate code you’d need to receive HTTP requests, parse the URI, and route the request to an appropriate class or method. The most popular REST API server frameworks are Flask, Django, and FastAPI.

### Flask
Flask is a flexible and comfortable web development framework that is easy to set up and simple to use, which makes it good for beginners. Tools like template engines, for caching, and authentication help developers work quickly. But Flask handles requests sequentially, so although you can get commercial projects going fast using Flask, it isn't good for high load needs. Flask also uses third-party modules, which can make it prone to security breaches. 

Uber, Pinterest, and Twilio were all built using the Flask framework.

### Django
Django is one of the most popular frameworks worldwide. It’s a free, open-source Python framework designed for building websites of any size, with any traffic needs. Django is sturdy and efficient, particularly because it makes use of reusable code. Django is also more secure than Flask, but Django software is much more unwieldy to work with. Developers may find Django slow because of the need to employ reusable modules and the need to check compatibility against previous versions. 

YouTube, Instagram, Spotify, and DropBox were built with Django.

### FastAPI
FastAPI is exactly what the name says: fast. It’s an open-source, high-performing web framework for building web APIs in Python, and it includes hints similar to those in Python. The main downside of FastAPI is how new it is. The FastAPI documentation is robust, but there is not as much in the way of external materials or community for Fast API as there is for Flask and Django. 

Netflix uses FastAPI internally. 

---

For more on comparing these three REST API frameworks, see [“Choosing between Django, Flask, and FastAPI ” ](https://www.webscale.com/engineering-education/) and [“Top Python REST API Frameworks in 2023.”](https://www.browserstack.com/guide/top-python-rest-api-frameworks)

## Pro tip
Nothing makes a developer complain faster than when things are messy. Start your own good habits now by making your APIs clean and consistent. Best practices include:

- Use the same name for a given parameter across multiple calls, in requests, and in responses. Don’t use room_id, RoomID, and guest_room_ID to all mean the same thing.

- Keep things like capitalization consistent.

- Pay attention to when you use GET vs. POST, etc. so you know exactly what function you are calling and what response should be expected. 

- Keep the RESTful design principles in mind.

Document your APIs and publish them. Encourage developers to experiment with them, which will encourage a robust ecosystem to blossom around your project.

REST APIs can be tricky to consume. Sometimes the responses you get don’t match the published docs. Your client should try its best to validate the responses and deal with the unexpected.

## Key takeaways
There are lots of REST API frameworks available on both the server side and the client side. These include plenty of free, open-source modules so you can get started right away learning to use these in Python. As you learn to work with REST, focus on developing good habits that will make it easier to collaborate with other developers as you progress.