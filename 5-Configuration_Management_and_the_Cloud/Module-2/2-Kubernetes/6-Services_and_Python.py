'''
Here’s an example of some Python code that uses the Kubernetes Python client to create, list, and delete Kubernetes Services in a given namespace.
'''
from kubernetes import client, config

def create_service(api_instance, namespace, service_name, target_port, port, service_type):
    """
    Creates a Kubernetes service based on the provided parameters.

    Parameters:
    - api_instance: An instance of the Kubernetes API client.
    - namespace: The namespace in which to create the service.
    - service_name: The name of the service.
    - target_port: The port on the container to forward requests to.
    - port: The port to expose the service on.
    - service_type: The type of service to create (ClusterIP, NodePort, LoadBalancer, ExternalName).
    """
    # Define the Service manifest based on the chosen Service type
    service_manifest = {
        "apiVersion": "v1",
        "kind": "Service",
        "metadata": {"name": service_name},
        "spec": {
            "selector": {"app": "your-app-label"},
            "ports": [
                {"protocol": "TCP", "port": port, "targetPort": target_port}
            ]
        }
    }

    # Modify manifest based on the service type
    if service_type == "ClusterIP":
        # ClusterIP is the default service type, no changes needed
        pass
    elif service_type == "NodePort":
        # Set the NodePort field to expose the service on a specific port on each node
        service_manifest["spec"]["type"] = "NodePort"
    elif service_type == "LoadBalancer":
        # Set the LoadBalancer type to get an external load balancer provisioned
        service_manifest["spec"]["type"] = "LoadBalancer"
    elif service_type == "ExternalName":
        # Set the ExternalName type to create an alias for an external service
        service_manifest["spec"]["type"] = "ExternalName"
        # Set the externalName field to the DNS name of the external service
        service_manifest["spec"]["externalName"] = "my-external-service.example.com"

    # Create the service in the specified namespace
    api_response = api_instance.create_namespaced_service(
        body=service_manifest,
        namespace=namespace,
    )
    print(f"Service '{service_name}' created with type '{service_type}'. Status: {api_response.status}")


def list_services(api_instance, namespace):
    """
    Lists all services in the specified namespace.

    Parameters:
    - api_instance: An instance of the Kubernetes API client.
    - namespace: The namespace to list services from.
    """
    api_response = api_instance.list_namespaced_service(namespace=namespace)
    print("Existing Services:")
    for service in api_response.items:
        print(f"Service Name: {service.metadata.name}, Type: {service.spec.type}")


def delete_service(api_instance, namespace, service_name):
    """
    Deletes a specified service in the given namespace.

    Parameters:
    - api_instance: An instance of the Kubernetes API client.
    - namespace: The namespace where the service exists.
    - service_name: The name of the service to delete.
    """
    api_response = api_instance.delete_namespaced_service(
        name=service_name,
        namespace=namespace,
    )
    print(f"Service '{service_name}' deleted. Status: {api_response.status}")


if __name__ == "__main__":
    # Load Kubernetes configuration (if running in-cluster, this might not be necessary)
    config.load_kube_config()

    # Create an instance of the Kubernetes API client
    v1 = client.CoreV1Api()

    # Define the namespace where the services will be created
    namespace = "default"

    # Example: Create a ClusterIP Service
    create_service(v1, namespace, "cluster-ip-service", target_port=8080, port=80, service_type="ClusterIP")

    # Example: Create a NodePort Service
    create_service(v1, namespace, "node-port-service", target_port=8080, port=30000, service_type="NodePort")

    # Example: Create a LoadBalancer Service (Note: This requires a cloud provider supporting LoadBalancer)
    create_service(v1, namespace, "load-balancer-service", target_port=8080, port=80, service_type="LoadBalancer")

    # Example: Create an ExternalName Service
    create_service(v1, namespace, "external-name-service", target_port=8080, port=80, service_type="ExternalName")

    # List existing Services
    list_services(v1, namespace)

    # Example: Delete a Service
    delete_service(v1, namespace, "external-name-service")
