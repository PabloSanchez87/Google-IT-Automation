# Project Problem Statement

You work for an online fruit store, and you need to develop a system that will update the catalog information with data provided by your suppliers. When each supplier has new products for your store, they give you an image and a description of each product.

Given a bunch of images and descriptions of each of the new products, you’ll:

- Upload the new products to your online store. Images and descriptions should be uploaded separately, using two different web endpoints.

- Send a report back to the supplier, letting them know what you imported.

Since this process is key to your business's success, you need to make sure that it keeps running! So, you’ll also:

- Run a script on your web server to monitor system health.

- Send an email with an alert if the server is ever unhealthy.

## How to Approach the Problem

**Break the problem down into smaller pieces.** If you’re not sure how to solve a piece of the puzzle, look for an even smaller piece that you can solve. Build up those smaller pieces into a larger solution!

**Make one change at a time.** Write unit tests to make sure that each new part of the solution works the way you think it does. Run your unit tests frequently to make sure that each part of your solution keeps working as you make changes.

**Use version control.** Check each part of your solution into version control as you complete it, so you can always roll back to a known version of your code if you make a mistake.

**Review module documentation!** You are going to need to use these modules to complete the final project. Reading the documentation takes time, but as you become more familiar with the APIs provided by these modules, it could save you from writing a bunch of custom code that could have just been a call to a module function! Remember, we’ve covered these modules in previous lessons too, so feel free to go back and review them if you need a refresher!

- [Python Image Library (PIL)](https://pillow.readthedocs.io/en/stable/) - [Tutorial](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html)

- [Requests](https://requests.readthedocs.io/en/latest/) (HTTP client library) - [Quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/)

- [ReportLab](/resources/reportlab-userguide.pdf) (PDF creation library)

- [email](https://docs.python.org/3/library/email.examples.html) (constructing email)

- [psutil](https://psutil.readthedocs.io/en/latest/) (processes and system utilization)

- [shutil](https://docs.python.org/3/library/shutil.html) (file operations)

- [smtplib](https://docs.python.org/3/library/smtplib.html) (sending email)

---

- [Project directory](/6-Automating_Real-World_Tasks_with_Python/Module-4/project/)