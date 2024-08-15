# AssignTrack

AssignTrack is a Django-based web application designed to manage and assess academic assignments efficiently. This platform facilitates a streamlined process for user authentication, assignment submission, and grading, enhancing the academic management experience for both educators and students. It serves as a comprehensive solution that bridges the gap between students and educational staff by providing a centralized platform to manage coursework, feedback, and evaluations transparently.

## What is AssignTrack?

AssignTrack was developed to tackle common challenges faced by educational institutions in managing and evaluating student assignments. The traditional methods that involve paper-based assignments or disparate digital solutions can be cumbersome, error-prone, and inefficient. AssignTrack provides a unified approach to handle assignments from creation to completion, ensuring that all stakeholders—students, teachers, and administrative staff—have a seamless interaction with academic workflows.

### Key Challenges Addressed by AssignTrack:

- **Accessibility**: Ensures that assignments are accessible anywhere, anytime, thereby accommodating remote learning environments.
- **Efficiency**: Reduces the administrative burden on educators by automating submission tracking, deadline management, and grading processes.
- **Transparency**: Offers real-time updates on submission statuses and grades, which helps in maintaining clear communication between students and educators.
- **Scalability**: Capable of handling multiple classes and assignments simultaneously, making it suitable for both small classes and large educational institutions.


## Features

- **User Authentication**: Secure registration and login functionality, along with JWT token management for API interactions.
- **Assignment Management**: Teachers can create, update, and delete assignments.
- **Submission Handling**: Students can submit assignments digitally through a user-friendly interface.
- **Assessment Features**: Teachers can assess submissions and provide grades and feedback.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Python 3.x
- Django

### Installing

A step by step series of examples that tell you how to get a development env running:

#### 1. Clone the repository

```bash
git clone https://github.com/Blockment/AssignTrack
```

#### 2. Navigate to the project directory

```bash
cd AssignTrack
```


#### 3. Build the Docker containers

```bash
docker-compose up --build
```

#### 4. Create and apply migrations

```bash
docker exec -it <container_id> python manage.py makemigrations
docker exec -it <container_id> python manage.py migrate
```

#### 5. Start the server

```bash
docker-compose up
```

Now, your server should be running on [http://localhost:8000/](http://localhost:8000/).

## Maintainers

- [Soroush Jahanzad](https://github.com/SJahanzad)