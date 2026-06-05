# IAM Platform Lab

## Overview

IAM Platform Lab is a personal project designed to learn and practice Identity & Access Management (IAM) concepts and modern backend/frontend development.

The project aims to simulate an IAM portal capable of managing:

- Users
- Groups
- Audit Logs
- Authentication
- Authorization

## Tech Stack

### Frontend
- Streamlit

### Backend
- FastAPI

### Future Components
- Keycloak
- PostgreSQL
- Docker
- Kubernetes
- Azure

---

## Current Features

### Dashboard
- User statistics
- Group statistics
- Audit statistics

### User Management
- Create users
- Read users
- Update users
- Delete users

### Group Management
- Create groups
- Read groups
- Update groups
- Delete groups

### Audit Logs
- Read audit events
- Create audit events

### Health Check
- API health endpoint

---

## API Endpoints

### Users

| Method | Endpoint |
|---------|---------|
| GET | /users |
| POST | /users |
| PUT | /users/{username} |
| DELETE | /users/{username} |

### Groups

| Method | Endpoint |
|---------|---------|
| GET | /groups |
| POST | /groups |
| PUT | /groups/{group_name} |
| DELETE | /groups/{group_name} |

### Audits

| Method | Endpoint |
|---------|---------|
| GET | /audits |
| POST | /audits |

### Health

| Method | Endpoint |
|---------|---------|
| GET | /health |

---

## Roadmap

- [x] Streamlit frontend
- [x] FastAPI backend
- [ ] Connect Streamlit to FastAPI
- [ ] Keycloak integration
- [ ] PostgreSQL
- [ ] Docker
- [ ] Kubernetes
- [ ] CI/CD
- [ ] Azure deployment

---

## Project Goal

The objective of this project is to build a complete IAM platform while learning modern development and infrastructure technologies commonly used in enterprise environments.