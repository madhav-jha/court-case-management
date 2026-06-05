:::: Court Case Management System - DevOps Project ::::

 ==> Project Overview..
 
 <img width="1792" height="1120" alt="after docker run" src="https://github.com/user-attachments/assets/8cb7ffd1-2ae1-4daf-a0ad-f2762a983f11" />

 ==> This project demonstrates an end-to-end DevOps CI/CD pipeline for a Court Case Management System.
 
 ==> The application consists of:

  - Frontend (HTML, CSS, JavaScript)
  - Backend (Python Flask)
  - Docker Containers
  - Docker Compose
  - Jenkins CI/CD Pipeline
  - Docker Hub Integration
  - GitHub Source Control

        :: Project Architecture ::
              GitHub 
                ↓ 
         Jenkins Pipeline
                ↓
        Build Frontend Docker Image 
                ↓
        Build Backend Docker Image 
                ↓ 
        Push Images to Docker Hub 
                ↓ 
        Docker Compose Deployment 
                ↓
        Frontend Container 
                ↓ 
        Backend Container


:: Project Structure ::
  
    ├── Jenkinsfile 
   
    ├── docker-compose.yml
   
    ├── frontend 
    |   ├── Dockerfile 
    |   ├── index.html 
    |   ├── style.css
    |   └── app.js

    ├── backend  
    │   ├── Dockerfile 
    │   ├── app.py 
    │   └── requirements.txt

    └── scripts

 ==>  Technologies Used...
  - MacOS
  - Git
  - GitHub
  - Jenkins
  - Docker
  - Docker Compose
  - Docker Hub
  - Python Flask
  - Nginx
  - HTML
  - CSS
  - JavaScript
    
        ==> Frontend Features....
            . Court Case Management Interface
            . Case Status Search
            . Responsive User Interface

        ==> Backend Features....
            . Flask API provides case information.

        ==> API Endpoint....
             . GET /status

        ==> Sample Response....
             { "case_no": "12345",
               "status": "Pending Hearing" 
             }
    
<img width="1792" height="1120" alt="after docker run" src="https://github.com/user-attachments/assets/3ffd87e4-b389-4b0d-b104-907a10c643db" />

==> Docker Implementation...

    Frontend Image..
     Built using Nginx Alpine Image.

    Backend Image..
     Built using Python 3.13 Slim Image.

    Build Images..
     docker build -t court-frontend:v1 ./frontend
     docker build -t court-backend:v1 ./backend

    Docker Compose..
     Run complete application:
      docker compose up -d --build
      docker compose ps
      docker compose down
      
 <img width="1792" height="1120" alt="after docker run" src="https://github.com/user-attachments/assets/574d84ac-fc3a-48c0-b4e7-8a4d7e1cc8c3" />
 <img width="1792" height="1120" alt="Screenshot 2026-05-31 at 4 03 30 PM" src="https://github.com/user-attachments/assets/36a82684-0aa1-4212-97e3-9222a54b0e55" />
 <img width="1792" height="1120" alt="Screenshot 2026-05-31 at 4 03 46 PM" src="https://github.com/user-attachments/assets/62e4bacd-8635-4da1-abc6-90d90b868ebe" />
 <img width="1792" height="1120" alt="Screenshot 2026-05-31 at 4 04 19 PM" src="https://github.com/user-attachments/assets/9642a392-78e8-4d35-b7a0-03b3af38eb40" />
 <img width="1792" height="1120" alt="Screenshot 2026-05-31 at 8 25 01 AM" src="https://github.com/user-attachments/assets/83d605ea-7f5c-476a-8fb1-634900e3e0c3" />
 <img width="1792" height="1120" alt="Screenshot 2026-05-31 at 4 57 32 PM" src="https://github.com/user-attachments/assets/e3c63f7b-cd43-4964-a92a-49e0e6f8d0d5" />

    ==> Jenkins Pipeline Stages...
          SCM Checkout
 
            Pull source code from GitHub repository.

          Build Docker Images

             Build frontend and backend Docker images.

          Docker Hub Login

             Authenticate with Docker Hub.

          Push Images

             Push Docker images to Docker Hub.

          Docker Compose Deploy

             Deploy application using Docker Compose.
  
          Application Verification

             Verify running containers.

          Docker Hub Repositories

          Frontend Image:

            jhamadhav2025/court-frontend:v1

          Backend Image:

            jhamadhav2025/court-backend:v1

<img width="1792" height="1120" alt="Screenshot 2026-05-31 at 9 04 08 AM" src="https://github.com/user-attachments/assets/c683bd3d-bd2f-4dbb-b1a6-b7f6913da28f" />
<img width="1792" height="1120" alt="Screenshot 2026-05-31 at 4 57 13 PM" src="https://github.com/user-attachments/assets/b66db46c-6490-4f29-9fea-e063f5790247" />
<img width="1792" height="1120" alt="Screenshot 2026-05-31 at 4 56 40 PM" src="https://github.com/user-attachments/assets/0148c427-0706-4d44-b415-aed0f6c2baf3" />      

    ==> Challenges Faced and Resolutions..
          Docker Command Not Found

          Issue:
             Jenkins could not locate Docker binary.

         Resolution:
             Used absolute Docker path:

             /usr/local/bin/docker
             Port Conflict

         Issue:
            Jenkins and application were using the same port.

        Resolution:
            Application deployed on different port.

        Dockerfile Path Issue

        Issue:
            Docker build failed because COPY path was incorrect.

        Resolution:
            Updated Dockerfile according to new project structure.

        Docker Hub Authentication Issue

        Issue:
           Docker Hub token had insufficient permissions.

        Resolution:
           Created access token with Read and Write permissions.

    Learning Outcomes::::-
     Git and GitHub Workflow
     Jenkins Pipeline Creation
     Docker Image Creation
     Docker Compose Deployment
     Docker Hub Integration
     CI/CD Automation
     Troubleshooting DevOps Issues
                                                                                          Author

                                                                                         Madhav Jha

                                                                            DevOps Project - Court Case Management System
 





    

