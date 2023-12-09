# Overview

This repository showcases the two projects that I have created. One is an end-to-end CI/CD pipeline for deploying a Java-based dummy application. The other is python utility for backing up remote PostgreSQL databases locally and to AWS S3. 

## CI-CD Pipeline project:

This project showcases an end-to-end CI/CD pipeline for deploying a Java-based dummy application. The pipeline harnesses a suite of technologies, including Terraform, Ansible, Jenkins, Docker, Kubernetes (AWS EKS), Git/GitHub, JFrog, Helm, Prometheus, and Grafana. It streamlines development, testing, and deployment processes.

Before getting started, I ensured that my local system has the following prerequisites:-

Code Editor: Any preferred code editor (e.g., VSCode).
Version Control: Git and a GitHub account.
Cloud Platform: AWS account and AWS CLI.
Infrastructure as Code: Terraform.
SSH and Telnet Client: Utilize a client like MobaXterm.


Comprehensive steps to set up the Java CI/CD pipeline:-

1. Setup Terraform
Installed Terraform on your local machine.

2. Provision Infrastructure with Terraform
Utilized the Terraform script to provision AWS EC2 instances for Jenkins master, build node, and Ansible node.

3. Configure Ansible
Configured the Ansible server and configure it to automate the provisioning of Jenkins master and build node.

4. Configure Jenkins Pipeline
Configured a Jenkins pipeline job tailored for your Java application.

5. Create Jenkinsfile
Configured a Jenkinsfile from scratch, defining the stages of your CI/CD pipeline.

6. Multibranch Pipeline and GitHub Webhook
Configured a multibranch pipeline and enable a webhook on GitHub for automated builds.

7. Integrate SonarQube and SonarScanner
Integrated SonarQube with Jenkins for comprehensive code quality analysis.

8. Artifactory Integration
Established an Artifactory account on JFrog Artifactory and configured Jenkins to seamlessly publish artifacts.
Also, generated an access token and add it as credentials in Jenkins.

9. Docker Integration
Created a Dockerfile, build, and publish a Docker image to Artifactory.
Integrated Docker with Jenkins, installing necessary plugins.

10. Provision Kubernetes Cluster (EKS) with Terraform
Utilized Terraform to provision an AWS EKS cluster.

11. Kubernetes Deployment with Helm
Created Kubernetes objects and manifest files, set up Helm charts, and deploy the Java application to the Kubernetes cluster.

12. Monitoring with Prometheus and Grafana
Implemented Prometheus and Grafana using Helm charts for in-depth monitoring of the Kubernetes cluster.

Additional Considerations:-
We also need to ensure that necessary credentials and tokens are properly configured in Jenkins for seamless integration with GitHub, SonarQube, Artifactory, and Docker.
Customize the Jenkinsfile according to your project structure and specific requirements.
Regularly update your CI/CD pipeline configuration to accommodate changes in your application and infrastructure.

## Python Project:

Python utility for backing up remote PostgreSQL databases locally or to AWS S3.

Preparing for Development

1. Ensure ``pip`` and ``pipenv`` are installed
2. Clone repository: ``git clone git@github.com:example/pgbackup``
3. ``cd`` into repository
4. Fetch development dependencies ``make install``
5. Activate virtualenv: ``pipenv shell``

Usage:
-
Pass in a full database URL, the storage driver, and destination.

S3 Example w/ bucket name:

 ::

    $ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups

Local Example w/ local path:

 ::

    $ pgbackup postgres://bob@example.com:5432/db_one --driver

local /var/local/db_one/backups

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

$ make 

If virtualenv isn’t active then use:

::

 $ pipenv run make
