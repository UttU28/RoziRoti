# WHAT ? WHERE ? HOW
**What did you do in it as a PIPELINE Guy???**


Here is the list of all the technologies and tools mentioned in the provided prompt:

1. **Azure Cloud**
2. **Azure Storage**
   - Blob Storage
   - Azure SQL Database
3. **Azure DevOps**
4. **Azure VPN**
5. **ExpressRoute**

## What was the conflict in your role and how did you resolve it.
-  Last September when we were rolling update on our application which we were Migrating from On-Prem to Azure, So while pushing an application to the production

## **Resource Creation**
- **Terraform**
	- It is an IaC tool, used for deploying and maintaining the infrastructure on the cloud.
	- In my current role, I have worked on creating Terraform Scripts to Deploy and Manage Infra on Azure. Have worked on scripting VMs, VNet, RG, Functions and many more.
	- My main role was to Automate the creation of Infra using DevOps pipeline, integrating Azure Policy to manage all the resources deployed and added Code Scanning Tools like Checkov and TerraScan to scan for any vulnerabilities in the code.
	- Send an automatic report of the PLAN generated from ```Terraform PLAN``` using an SMTP Server in Azure Pipeline.
	- Once it has Passed the Manual Validation then the Pipeline Generates the STATE file on ```Terraform APPLY``` and stores the state file into the Azure Blob Storage and then encrypting it storing the Service Principal Key in Azure Key Vault. Making the state file secure and accessible in the cloud.
	- Implemented Azure Security Center, Azure Policy, NSG, and Azure Firewall to secure the infrastructure by providing unified security management, enforcing compliance, controlling traffic, and filtering threats.
	- Also Imported and Managed already existing infrastructure on the cloud and adding it in the state file.

- **Bicep Templates**
	- Some of the features requires them to have their own infrastructure. So we created Bicep files for **Provisioning** and **Configuration** of the infrastructure and added it to the pipeline. And managed them in the main Terraform code by using ```Data Source Block``` to get the resource data automatically.

- **ARM Templates**
	- Earlier some of the Legacy Applications used ARM Templates, so worked on them but mostly it was migration from ARM to Bicep templates.
	- Written ARM Templates for writing AKS wihich allows definition and configuration of Kubernetes clusters
	- Integrated Azure Monitoring for Logging and Monitoring, Azure Key Vault for Secrets Management and Active Directory for Authentication and Authorization.
	- VMSS, Node Pools, 

- **Ansible**
	- Ansible is a Software Provisioning and Configuration Management Tool used in cloud for setting the desired state on the host infra.
	- All the HOST information of Terraform Deployed Infrastructure is stored in an Inventory file in Blob Storage.
	- Integrated Ansible with CI/CD pipelines to automate the Software Provisioning and Configuration Management of infrastructure, ensuring consistent and repeatable environments.
	- The Azure DevOps Pipeline then accesses all the host information and performs various configuration tasks, such as installing necessary packages, configuring system settings, deploying application code, and ensuring that the infrastructure is in desired state as defined in the Ansible playbooks.
	-	Utilized Jinja2 templates within Ansible playbooks to dynamically generate configuration files based on variables and conditions.

- **Docker**
	- Created Docker FIles to create Docker Images for the application by encapsulating the Code, Dependencies and OS Configuration into portable Containers.
	- Utilized Docker Compose to define and manage multi-container applications, simplifying the orchestration of complex setups. This saved us a lot of hassle of writing the Network Code for forwarding all the container requests to the Database Server.
	- Setting up Azure Security Centre, Aqua Security for Continuous Security and Code Monitoring tools.
	- Using different Environment Variables in Pipeline for each environment to manage configuration settings, ensuring that lower settings are used in test environments while applying optimized or stricter configurations for production environments.
	- Leveraging it's portability to run on Any Environment, even on Azure CI/CD Pipeline it runs the Docker code without provisioning of additional Infra.

- **Azure Container Registry (ACR)**
	- ACR serves as a private repository for Docker container images, providing a secure location to store and manage images used by AKS.
	-	These Containers are later tagged on the build number and are stored as Artifacts in Azure Container Registry maintaining accessibility and version-control using Azure DevOps Pipeline
	- Automated the building and pushing of Docker images to ACR using CI/CD pipelines, ensuring updated images are available for deployment.
	- Before pushing images to the Azure Container Registry (ACR) for deployment on the production server, they undergo verification and signing to ensure their integrity and authenticity, leveraging the Content Trust, Built-In Repo/Image Scanning and RBAC feature in ACR for enhanced security.
	- Configured ACR WebHooks that triggers the CI/CD Pipeline whenever there is new image push.
	- Ans Utilized ACRs Geo_Replication for getting higher availability by .... 

- **Kubernetes (AKS)**
	- AKS integrates seamlessly with ACR, allowing easy access to container images during deployment, which makes the CI/CD Pipeline automatically Access and Use the image in the ACR Securely, it then pulls the latest version of the image and uses in the AKS for making clusters.
	- AKS authenticates with ACR using service principals or managed identities stored in Key Vault, ensuring secure access to container images.
	- Worked on Creating ARM Templates for Cluster Definition using parameters like k8s version, node size, node count, and N/W Config.
	-	Setting up Resource Dependencies b/w Resources and also between Clusters and Networking Resources.
	-	Defined AKS clusters with scalable configurations, allowing for automatic scaling of node pools based on workload demands.
	- Integrated Azure Key Vault for Secrets Management and Active Directory for Authentication and Authorization using ARM Templates, in the DevOps Pipeline.
	- Used Azure Monitor and Azure Log Analytics, providing insights into cluster performance, resource utilization, and application health.
	- Implemented blue-green deployment strategies in AKS to minimize downtime and risk during application updates.
	- Networking: Configured advanced networking features, such as VNet integration and private link, to securely connect AKS clusters and ACR, ensuring that all communications occur within the Azure network.

- **Azure Boards**
	- 

- **Python**
11. **Bash**
12. **Shell**
13. **PowerShell**
14. **CRON Jobs**
18. **Helm**
19. **SonarQube**
20. **Snyk**
21. **Checkmarx**
22. **JIRA**
23. **Kanban Boards**
25. **Selenium**
26. **Azure Virtual Networks (VNets)**
27. **Azure Active Directory (Azure AD)**
28. **Azure Monitor**
29. **Azure Log Analytics**
30. **Azure Key Vault**
31. **Git**
32. **Azure Repos**
33. **OWASP ZAP**
34. **Veracode**
35. **Agile Methodologies**