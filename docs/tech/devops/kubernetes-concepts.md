# Key Kubernetes Concepts

Kubernetes is a powerful container orchestration platform that automates deployment, scaling, and operations of containerised applications. Understanding its key concepts is essential for effectively managing modern cloud-native applications. Here are 15 of the most common Kubernetes concepts:

## 1. Cluster  
A Kubernetes cluster is the foundation of the system, consisting of multiple nodes (machines) that work together to run applications. It includes a control plane that manages the cluster and worker nodes that execute workloads.

## 2. Node  
A node is an individual machine (physical or virtual) in the cluster that runs containerised applications. Nodes include essential components such as a container runtime, kubelet, and networking capabilities.

## 3. Pod  
The smallest deployable unit in Kubernetes, a pod encapsulates one or more tightly coupled containers that share networking and storage resources. Pods ensure that containers communicate efficiently and are scheduled together.

## 4. Deployment  
A deployment defines how applications are managed, enabling automated rollouts, updates, and scaling. It ensures that the desired number of pods are running and can roll back changes if necessary.

## 5. ReplicaSet  
A ReplicaSet maintains a specified number of identical pod instances, ensuring high availability and resilience. Deployments typically use ReplicaSets to manage pod scaling.

## 6. Service  
A service abstracts and exposes a stable endpoint to connect applications, allowing communication between pods or external users. It provides load balancing and ensures that traffic reaches healthy pods.

## 7. Ingress  
Ingress is a Kubernetes resource that manages external access to services, typically via HTTP or HTTPS. It allows for path-based routing, SSL termination, and traffic management.

## 8. ConfigMap  
ConfigMaps store non-sensitive configuration data, such as environment variables and application settings, allowing configuration to be managed separately from application code.

## 9. Secret  
Secrets store sensitive data, such as API keys, passwords, and tokens, securely within the cluster, preventing exposure in application code.

## 10. Namespace  
Namespaces provide logical separation within a cluster, enabling multi-tenancy, resource allocation, and isolation for different teams or applications.

## 11. Persistent Volume (PV) & Persistent Volume Claim (PVC)  
- **Persistent Volumes (PV)**: Storage resources that exist independently of pods, enabling persistent data storage.  
- **Persistent Volume Claims (PVC)**: Requests for storage resources by applications, dynamically provisioning storage as needed.

## 12. StatefulSet  
StatefulSets manage stateful applications that require stable, unique network identities and persistent storage, such as databases.

## 13. DaemonSet  
A DaemonSet ensures that a copy of a specific pod runs on all (or some) nodes, commonly used for logging, monitoring, and networking functions.

## 14. Job & CronJob  
- **Job**: Executes a task to completion, ensuring successful execution of batch processing tasks.  
- **CronJob**: Runs scheduled tasks at specific intervals, similar to traditional cron jobs.

## 15. Horizontal & Vertical Pod Autoscaling (HPA & VPA)  
- **Horizontal Pod Autoscaler (HPA)**: Automatically scales the number of pods based on CPU/memory usage or custom metrics.  
- **Vertical Pod Autoscaler (VPA)**: Dynamically adjusts resource requests and limits for individual pods.

These concepts form the backbone of Kubernetes, enabling efficient container orchestration, scalability, and automation in modern cloud environments.
