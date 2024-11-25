# Generate and manage containers

## Generating image containers

Generating image containers Up until now, you have been working with prepackaged container images.

To [build a container image](https://docs.docker.com/get-started/workshop/02_our_app/), you create a Dockerfile, which contains step-by-step instructions for Docker to package your application along with all its dependencies.

## Choose a base image

One important step is [deciding which base image to use](https://pythonspeed.com/articles/base-image-python-docker-images/). 

The base image provides all the operating system files inside the container; it’s a bit like trying to choose between different Linux distributions. The best base images provide just what your application needs to run, without a lot of extra bloat, such as extra command line tools, libraries, drivers, etc.

Here are some of the most popular base images:

- [`Debian`](https://hub.docker.com/_/debian) and [`Ubuntu`](https://hub.docker.com/_/ubuntu): containers that boot into a full-featured, general Linux environment 

- [`Alpine Linux`](https://hub.docker.com/_/alpine): a stripped-down image designed to result in small, fast containers

- [`Python`](https://hub.docker.com/_/python/): great for running Python apps

The base images make good use of tags to provide lots of choices. 

For example, you can choose among several versions of Debian or Ubuntu by providing the right tag. The Python base image not only includes every Python version since 3.7, but also includes variants based on the Debian or Alpine images.

## Create a Dockerfile

Now, you can create a Dockerfile in your project directory. Again, the Dockerfile lists the steps needed to generate your container image. 

Here’s a sample Dockerfile for a Python web app that uses Flask and SQLAlchemy:

```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 4000
CMD [ "flask", "run", "--host=0.0.0.0", "--port=4000"]
```

Here’s a line-by-line explanation of what this does:

- `FROM` sets the base image to use. In this case, we are using the Python 3.9 base image.

- `WORKDIR` sets the working directory inside the image.

- `COPY` requirements.txt ./ copies the requirements.txt file to the working directory.

- `RUN` pip install -r requirements.txt installs the requirements.

- `COPY` . . copies all the files in the current directory to the working directory.

- `EXPOSE` 4000 exposes the port 4000.

- `CMD` [ "flask", "run", "--host=0.0.0.0", "--port=4000"] tells Docker to run Flask when the container starts.

Your project probably already has a requirements.txt file. Here’s a minimal one that just installs Flask, SQLAlchemy, and the PyMysql driver:

```requirements.txt
flask
pymysql
Flask-SQLAlchemy
```

## Build a Docker image

Now that you have these files in your project directory, you can 
build a [Docker image](https://linuxize.com/post/how-to-build-docker-images-with-dockerfile/) with the `docker build` command. It’s important to 
[choose the best Docker image](https://www.techtarget.com/searchitoperations/tip/Choose-the-best-Docker-image-for-the-job-at-hand) for your specific project.


As we discussed previously in the section on containers and tags, you probably want to tag your container image. Most containers at least use tags for the version number. You do that by adding the `-t option` to the command. For example, you might use the following command:

```bash
docker build -t myname/myapp:1.0 .
```

In this command, `“myname”` is your registry username, and `“myapp”` is the name of your application.

This command usually produces a lot of output, as Docker downloads the base image, runs each of the commands in your Dockerfile, and tags the image.

If you plan to upload your image to a registry, you can do that by adding the `–push option`. Generally, though, you would build the container, test it, then push it to the registry in a separate step — ideally all as part of a CI/CD pipeline.

### Pro tip
Docker images are built from layers. You’ll notice that Docker adds a layer to the image for each command in your Dockerfile. Some of those layers can be quite large, if many files were changed from the previous layer. A common trick is to clean up at the end of a command that creates a bunch of temporary files.

## Manage images
When you’ve built your image, you can use it to start a container:

```bash
docker run -p 4000:4000 myname/myapp:1.0
```

In the above command, `myname/myapp:1.0` is the image you built earlier. The `-p` argument forwards port 4000 on the host to the webserver on port 4000 inside the container. (Note that it matches the `--port=4000` argument we included in the Dockerfile earlier.)

After you’ve been building containers for a while, you’re going to build up a lot of old, stale, or half-built images. To see what images are sitting around taking up hard drive space, you can use the ls command:

```bash
docker image ls -a
```

You can remove the unused images (images that are not associated with any container) with the `prune` command.

```bash
docker image prune
```

As mentioned in the section on generating images, you can also push your image to a repository like DockerHub:

```bash
docker image push myname/myapp:1.0
```

## Key takeaways
Developers choose to containerize their applications for several reasons, as containerization offers various benefits that make the development, deployment, and management of applications more efficient and scalable.