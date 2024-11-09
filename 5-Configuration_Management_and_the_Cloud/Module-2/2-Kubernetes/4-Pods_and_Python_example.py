'''
Pods and Python

To manage Kubernetes pods using Python, you can use the kubernetes library. 
Here is some example code of how to create, read, update, and delete a Pod using Python.
'''

from kubernetes import client, config

# Load the Kubernetes configuration from the default location (e.g., ~/.kube/config)
config.load_kube_config()

# Initialize the Kubernetes client
v1 = client.CoreV1Api()

# Define the Pod details
pod_name = "example-pod"
container_name = "example-container"
image_name = "nginx:latest"
port = 80

# Function to create a Pod
def create_pod(namespace, name, container_name, image, port):
    """
    Creates a Kubernetes Pod with the specified configuration.

    Parameters:
        namespace (str): The namespace to create the Pod in.
        name (str): The name of the Pod.
        container_name (str): The name of the container inside the Pod.
        image (str): The Docker image for the container.
        port (int): The port number for the container.

    Returns:
        response: The API response of the created Pod.
    """
    container = client.V1Container(
        name=container_name,
        image=image,
        ports=[client.V1ContainerPort(container_port=port)],
    )

    pod_spec = client.V1PodSpec(containers=[container])
    pod = client.V1Pod(
        api_version="v1",
        kind="Pod",
        metadata=client.V1ObjectMeta(name=name),
        spec=pod_spec,
    )

    try:
        response = v1.create_namespaced_pod(namespace, pod)
        print("Pod created successfully.")
        return response
    except Exception as e:
        print("Error creating Pod:", e)

# Function to read a Pod's details
def get_pod(namespace, name):
    """
    Fetches the details of an existing Pod.

    Parameters:
        namespace (str): The namespace of the Pod.
        name (str): The name of the Pod.

    Returns:
        None
    """
    try:
        response = v1.read_namespaced_pod(name, namespace)
        print("Pod details:", response)
    except Exception as e:
        print("Error getting Pod:", e)

# Function to update a Pod's container image
def update_pod(namespace, name, image):
    """
    Updates the container image of an existing Pod.

    Parameters:
        namespace (str): The namespace of the Pod.
        name (str): The name of the Pod.
        image (str): The new Docker image for the container.

    Returns:
        updated_pod: The API response of the updated Pod.
    """
    try:
        response = v1.read_namespaced_pod(name, namespace)
        response.spec.containers[0].image = image

        updated_pod = v1.replace_namespaced_pod(name, namespace, response)
        print("Pod updated successfully.")
        return updated_pod
    except Exception as e:
        print("Error updating Pod:", e)

# Function to delete a Pod
def delete_pod(namespace, name):
    """
    Deletes an existing Pod.

    Parameters:
        namespace (str): The namespace of the Pod.
        name (str): The name of the Pod.

    Returns:
        None
    """
    try:
        response = v1.delete_namespaced_pod(name, namespace)
        print("Pod deleted successfully.")
    except Exception as e:
        print("Error deleting Pod:", e)

# Main script execution
if __name__ == "__main__":
    namespace = "default"

    # Create a Pod
    create_pod(namespace, pod_name, container_name, image_name, port)

    # Read the Pod's details
    get_pod(namespace, pod_name)

    # Update the Pod's container image
    new_image_name = "nginx:1.19"
    update_pod(namespace, pod_name, new_image_name)

    # Read the updated Pod details
    get_pod(namespace, pod_name)

    # Delete the Pod
    delete_pod(namespace, pod_name)
