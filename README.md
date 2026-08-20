# Kubernetes Assignment – BMI Application Deployment

## Project Overview

This project demonstrates an end-to-end **containerized application deployment and CI/CD pipeline using Docker, Kubernetes, Minikube, GitHub Actions, and Docker Hub**.

A Flask-based BMI Calculator is containerized with Docker and deployed to a **two-node Minikube Kubernetes cluster** running on Windows 11. The application is exposed through a NodePort Service and accessed through a browser.

### Architecture & Release Flow

```text
Source Change → Git Push → GitHub Actions
                         ↓
                  Docker Build & Push
                         ↓
                    Docker Hub
                         ↓
                 kubectl set image
                         ↓
               Kubernetes Deployment
                         ↓
                  Rolling Update
                         ↓
                   BMI Pods (2)
                         ↓
                  NodePort Service
                         ↓
                      Browser
```

## Technology Stack

**Windows 11 | Docker Desktop | Python/Flask | Docker | Kubernetes | Minikube | kubectl | GitHub | GitHub Actions | Self-Hosted Runner | Docker Hub**

## Kubernetes Environment

* **Minikube:** Two-node cluster — control-plane + worker
* **Deployment:** 2 BMI application replicas
* **Service:** NodePort
* **Container Port:** 5000
* **Health Checks:** Readiness & liveness probes
* **Resources:** CPU/memory requests and limits
* **Updates:** Kubernetes rolling updates using versioned Docker images

## CI/CD Pipeline

GitHub Actions is triggered on every push to `main`.

```text
Checkout
   ↓
Docker Hub Login
   ↓
Build Versioned Image
   ↓
Push Image to Docker Hub
   ↓
Apply Kubernetes Manifests
   ↓
Update Deployment Image
   ↓
Wait for Rollout
   ↓
Verify Deployment / Pods / Service
```

A **self-hosted GitHub Actions runner** is used because the Minikube cluster is running locally on the Windows host.


## Repository Structure

```text
k8s-assignment/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/index.html
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── scripts/
│   ├── log-original.sh
│   └── log-fixed.sh
├── .github/workflows/
│   └── deploy.yaml
├── Dockerfile
├── README.md
└── CHANGELOG.md
```

Access the application:

```bash
minikube service bmi-service -p k8s-assignment
```

## Final Outcome

A code change pushed to GitHub automatically **builds a new Docker image, pushes it to Docker Hub, updates the Kubernetes Deployment, performs a rolling Pod update, and serves the updated BMI application through the existing NodePort Service.**

**Docker → Kubernetes → GitHub Actions → Docker Hub → Rolling Deployment → Browser**
