# Generate and manage containers: VS Studio & Docker

Virtual Studio (VS) Code provides an [optional extension](https://code.visualstudio.com/docs/containers/overview) that integrates with Docker, making it possible to [build and manage container images](https://code.visualstudio.com/docs/devcontainers/containers) right inside the integrated development environment (IDE).

## Build a container using VS Code and Docker

[Steps to install:](https://learn.microsoft.com/en-us/visualstudio/docker/tutorials/docker-tutorial)

- In the VS Code menu, select View > Extensions.

- Search for “docker.”

- Install the verified Docker extension from Microsoft.

### When you’ve installed Docker, the extension adds a number of helpful features to VS Code. These include:

- Autocompletion and syntax highlighting when you’re editing a Dockerfile

- Scanning your Dockerfile for potential problems

- Commands to quickly generate Dockerfile and Compose file templates

- A new “Docker view” that shows containers and images on your machine and allows you to start and stop containers, launch a shell inside a container, and inspect the files in a running container

- Connections to DockerHub and other registries, allowing you to publish images by dragging and dropping them

- Debugging code inside a running container

- Access to pretty much every Docker command from the Command Palette

## DevContainer option
Microsoft supports  a new open-source standard called DevContainer that extends the use of Docker in the development cycle. Rather than build your container every time you want to test it, with DevContainer, you can actually develop and debug your code inside a container.

DevContainer is also compatible with GitHub Codespaces, which means you can run your IDE in the cloud. Instead of spending time setting up your local development environment just right, you can add a devcontainer.json file to your Git repository and develop in the cloud with a development environment that is fully version controlled.

You can read more about DevContainer [here](https://code.visualstudio.com/docs/devcontainers/containers)

## Key takeaways
VS Code's integration with Docker simplifies the process of container creation, orchestration, and management, enabling developers to build, test, and deploy applications more efficiently. Containers offer a consistent and isolated environment for development, eliminating the “it works on my machine” problem and ensuring seamless collaboration across teams.
