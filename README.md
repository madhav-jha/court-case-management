:::: Court Case Management System - DevOps Project ::::

 ==> Project Overview..|
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
   │   ├── Dockerfile 
   │   ├── index.html 
   │   ├── style.css│ 
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

