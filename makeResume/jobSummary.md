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
-  Last September, during a major project to migrate 
 application from an on-premises setup to Azure
 conflict while rolling out updates to the production environment
 The application had been thoroughly tested in the staging environment, but issues arose during the final push to production. 
	made it worse, the stakeholders wanted some quick actions on this matter.
- Since, everything BROKEN, everyone PANIK. I CALM them DOWN.
- Immidiately organized Virtual Meeting 
the objective was to make it up and running, and tracking progress on slack channel dedicated.
- App team said "Might be issue with some dependency or misconfig in application"
- Ops team said "Might be the NSG is acting lil funny
- Setup paired programming for App and Dev team to work together on this and address the issue
- Developed a rollback plan 
- Used Ansible to automate and standardize configuration changes across environments.
- misconfiguration in the Network Security Groups (NSGs) causing Blocking of Application Traffic.
- So we resolved it, tested the new build again in all the ENV, and then pushed to production.
- The sudden failure of system was overwhelming for the whole team, but I managed to resolve it by discussing possible issues, pair programming for better understanding of the infra. 



## A Day in your Life?
- Checking on emails, checking boards for any stories, bugs or report update.
- Attend daily stand-up meetings or other scheduled meetings with the team to discuss progress, blockers, and plans for the day. Collaborate with cross-functional teams to align on project goals and timelines.
- Review the logs and performance metrics of the DevOps pipelines using Azure Monitor and Log Analytics. Look for any failed builds, deployment issues, or performance bottlenecks.
- Conduct training sessions or knowledge-sharing meetings to help others understand new tools or processes. Writing Knowledge Transfer Documentation for future Use.
- Using Monitoring and Log Analytics to Analyze the usage data of virtual machines and other resources. Adjust configurations based on usage patterns, such as scaling up or down instances to optimize performance and cost-efficiency.
- Last week, the application team was working on an application, so my role is to provide infra pipeline for creation of the resource and setting basic network config, where I used Terraform, in test Environment
- Collaborate with the application development team to understand their infrastructure requirements for new projects or updates.
	- **Resource Creation**: Write and execute Terraform scripts to provision necessary resources such as VMs, storage accounts, and databases.
	- **Network Configuration**: Set up VNets, subnets, and network security groups (NSGs) to ensure secure and efficient communication between resources.
	- **Version Control**: Use Git to version control Terraform scripts, ensuring changes are tracked and can be rolled back if needed.
- Respond to any infrastructure-related incidents or outages. Investigate root causes, implement fixes, and document the incident resolution process.

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

## **Resource Configuration**
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

-	**Azure Virtual Networks (VNets)**
	- Virtual Networks are essential for securely connecting various components of infrastructure, communication between resources, ensuring isolation and segmentation of network traffic.

	- **Configuration**: 
		-	**Defining Network Segments**
			-	**Subnets**: VNets can be divided into multiple subnets, each representing a different segment of the network. Subnets help in organizing resources logically and controlling traffic flow between different parts of the application.
			-	**Address Space**: VNets require an IP address range in CIDR notation. Subnets within a VNet will have their own address ranges carved out of the VNet’s address space.
			-	**Network Security Groups (NSGs)**: NSGs are used to control inbound and outbound traffic to network interfaces (NIC), VMs, and subnets. They contain security rules that define allowed or denied traffic.
	- **DNS Settings**:
		- **Private DNS Zones**: VNets can be linked to Azure DNS private zones for name resolution within the VNet, which helps in managing DNS records for VMs and other resources.
	- **Peering**:
		- **VNet Peering**: VNets can be peered to enable resources in different VNets to communicate with each other. This is essential for multi-tier applications where components might reside in different VNets for isolation or scaling purposes.
	
	- Created Terraform scripts to define and deploy VNets, subnets, NSGs, and VNet Peering Configurations. Which all is managed in the Terraform State Files.
	-	VNets are integrated into the Azure DevOps Pipeline, so it can be used for repeatable and consistent deployments.
	- **Ansible** Playbooks are further used to configure the VMs and other Resources within **VNets Post-Deployment**
	- We used ansible for setting up routing, DNS Configuration and Firewall Rules.
	- The inventory file generated by Terraform in the Blob Storage is used by Ansible to create the dynamic host file to access VMs and configure Network Settings.
	- VNets are Networking Backbone of **Azure Kubernetes Services** Clusters ensuring secure and efficient communication between containerized applications.
	- AKS can be configured to use VNet integration, allowing pods to receive IP addresses from the VNet, ensuring seamless communication with other Azure resources.
	-	**Azure Container Registry** access can be restricted to specific VNets using private endpoints, ensuring that only resources within the VNet can pull images from the registry. 
	- **Docker** containers running in VMs or AKS clusters will utilize the VNet to communicate with each other and other Azure services.
	-	Network configurations defined at the VNet level ensure that Docker containers can access necessary resources while maintaining isolation and security.

-	**Azure Active Directory (Azure AD)**
	- Azure Active Directory (Azure AD) is a cloud-based identity and access management service. Providing authentication and authorization for users, applications, and services.
	- I implemented RBAC for the resources on the infra, serving each team having their own set of infra they can access rest they cant. It uses Service principal for verification of the user.
	- In the DevOps Pipeline the Terraform code creates and manages Azure AD **Service Principals** and assign roles.
	- Once the Infra is Created with Azure AD configured and if there is any need to update the roles or manage anything on all the resources, we use **Ansible Scripts** that uses **Service Principal** to connect to Azure AD and can manage roles and permissions. And can also do Dynamic user creation and group assignments based on inventory data.
	- Integrated **AKS with Azure AD** to enable secure access to the Kubernetes API, allowing role-based access control within the cluster based on Azure AD identities.
  

-	**Azure Monitor**
	- 

-	**Azure Log Analytics**
	- 

-	**Azure Key Vault**
	- 

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
31. **Git**
32. **Azure Repos**
33. **OWASP ZAP**
34. **Veracode**
35. **Agile Methodologies**