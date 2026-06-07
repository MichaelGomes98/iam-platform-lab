# IAM Platform Lab Roadmap

## Phase 1 - Frontend Portal
- [x] Dashboard
- [x] Users page
- [x] Groups page
- [x] Audit page

## Phase 2 - Backend API
- [x] FastAPI installation
- [x] GET /users
- [x] GET /groups
- [x] GET /audits
- [x] POST /users
- [x] POST /groups
- [x] POST /audits
- [x] PUT /users/{username}
- [x] PUT /groups/{group_name}
- [x] DELETE /users/{username}
- [x] DELETE /groups/{group_name}
- [x] GET /health

## Phase 3 - Frontend ↔ Backend Integration
- [x] Connect Users page to API
- [x] Connect Groups page to API
- [x] Connect Audits page to API
- [x] Connect Dashboard to API
- [x] Create User from frontend
- [x] Create Group from frontend
- [x] Update User from frontend
- [ ] Delete User from frontend
- [ ] Delete Group from frontend

## Phase 4 - Keycloak
- [ ] Install Keycloak
- [ ] Configure realm
- [ ] Configure groups
- [ ] Sync users from Keycloak

## Phase 5 - Authentication
- [ ] OIDC login
- [ ] JWT validation
- [ ] Logout

## Phase 6 - Audit Database
- [ ] PostgreSQL
- [ ] Store audit logs in database

## Phase 7 - Docker
- [ ] Dockerize frontend
- [ ] Dockerize backend
- [ ] Dockerize Keycloak

## Phase 8 - Docker Compose
- [ ] Local platform deployment

## Phase 9 - Kubernetes
- [ ] Deploy frontend
- [ ] Deploy backend
- [ ] Deploy Keycloak

## Phase 10 - CI/CD
- [ ] GitHub Actions
- [ ] Automated tests
- [ ] Automated deployment

## Phase 11 - Cloud
- [ ] Terraform
- [ ] Azure deployment