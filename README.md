# IAM Platform Lab

## Overview

IAM Platform Lab is a personal project designed to learn and practice Identity & Access Management (IAM) concepts while building a modern full-stack application.

The goal is to progressively build an enterprise-style IAM platform capable of managing:

* Users
* Groups
* Audit Logs
* Authentication
* Authorization
* Identity Federation

This project also serves as a learning platform for modern development, infrastructure, and cloud technologies.

---

# Current Architecture

Frontend (Streamlit)

↓

Backend API (FastAPI)

↓

Future Integrations:

* Keycloak
* PostgreSQL
* Docker
* Kubernetes
* Azure

---

# Tech Stack

## Frontend

* Streamlit

## Backend

* FastAPI
* Python

## Future Components

* Keycloak
* PostgreSQL
* Docker
* Kubernetes
* GitHub Actions
* Terraform
* Azure

---

# Current Features

## Dashboard

* User statistics
* Group statistics
* Audit statistics

## User Management

* Create users
* Read users
* Update users
* Delete users

## Group Management

* Create groups
* Read groups
* Update groups
* Delete groups

## Audit Logs

* Read audit events
* Create audit events

## Health Monitoring

* API health endpoint

---

# IAM Concepts Covered

* User Lifecycle Management
* Group Management
* Audit Logging
* REST API Development
* Backend Service Design
* Frontend / Backend Communication

Planned:

* Authentication
* Authorization
* Role-Based Access Control (RBAC)
* OpenID Connect (OIDC)
* JWT Validation
* Identity Federation

---

# API Endpoints

## Users

| Method | Endpoint          |
| ------ | ----------------- |
| GET    | /users            |
| POST   | /users            |
| PUT    | /users/{username} |
| DELETE | /users/{username} |

## Groups

| Method | Endpoint             |
| ------ | -------------------- |
| GET    | /groups              |
| POST   | /groups              |
| PUT    | /groups/{group_name} |
| DELETE | /groups/{group_name} |

## Audits

| Method | Endpoint |
| ------ | -------- |
| GET    | /audits  |
| POST   | /audits  |

## Health

| Method | Endpoint |
| ------ | -------- |
| GET    | /health  |

---

# Project Structure

iam-platform-lab/

├── backend/

│ └── main.py

│

├── frontend/

│ ├── Dashboard.py

│ ├── Users.py

│ ├── Groups.py

│ └── Audits.py

│

├── README.md

└── roadmap.md

---

# Run Locally

## Clone Repository

git clone https://github.com/your-username/iam-platform-lab.git

cd iam-platform-lab

## Create Virtual Environment

py -m venv .venv

## Activate Virtual Environment

### PowerShell

.venv\Scripts\Activate.ps1

### CMD

.venv\Scripts\activate

## Install Dependencies

pip install streamlit fastapi uvicorn pandas requests

---

# Start Backend

uvicorn backend.main:app --reload

Swagger UI:

http://127.0.0.1:8000/docs

---

# Start Frontend

streamlit run frontend/Dashboard.py

---

# Roadmap

## Phase 1 - Frontend Portal

* [x] Dashboard
* [x] Users Page
* [x] Groups Page
* [x] Audit Page

## Phase 2 - Backend API

* [x] FastAPI Installation
* [x] GET /users
* [x] GET /groups
* [x] GET /audits
* [x] POST /users
* [x] POST /groups
* [x] POST /audits
* [x] PUT /users/{username}
* [x] PUT /groups/{group_name}
* [x] DELETE /users/{username}
* [x] DELETE /groups/{group_name}
* [x] Health Check Endpoint

## Phase 3 - Frontend Integration

* [x] Connect Dashboard to API
* [x] Connect Users Page to API
* [x] Connect Groups Page to API
* [x] Connect Audits Page to API
* [ ] Connect POST Actions
* [ ] Connect PUT Actions
* [ ] Connect DELETE Actions

## Phase 4 - Keycloak

* [ ] Install Keycloak
* [ ] Configure Realm
* [ ] Configure Roles
* [ ] Configure Groups

## Phase 5 - Authentication

* [ ] OIDC Login
* [ ] JWT Validation
* [ ] Logout

## Phase 6 - PostgreSQL

* [ ] Database Setup
* [ ] Store Audit Logs
* [ ] Store Users
* [ ] Store Groups

## Phase 7 - Docker

* [ ] Dockerize Frontend
* [ ] Dockerize Backend
* [ ] Dockerize Keycloak

## Phase 8 - Kubernetes

* [ ] Deploy Frontend
* [ ] Deploy Backend
* [ ] Deploy Keycloak

## Phase 9 - CI/CD

* [ ] GitHub Actions
* [ ] Automated Tests
* [ ] Automated Deployment

## Phase 10 - Cloud

* [ ] Terraform
* [ ] Azure Deployment

---

# Project Goal

The objective of this project is to build a complete IAM platform while learning technologies commonly used in enterprise environments.

The project is intentionally developed step-by-step to gain practical experience with:

* Identity & Access Management
* API Development
* Authentication & Authorization
* Cloud Technologies
* Containerization
* Infrastructure as Code
* DevOps Practices
* Enterprise Architecture