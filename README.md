# Mc Files

## Table of contents

- [Overview](#overview)
  - [The Challenge](#the-challenge)
  - [Screenshot](#screenshot)
- [Features](#features)
  - [User Registration and Authentication](#user-registration-and-authentication)
  - [File Management](#file-management)
  - [User Roles](#user-roles)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Installation Steps](#installation-steps)
- [Usage](#usage)
  - [Starting the Application](#starting-the-application)
  - [Stopping the Application](#stopping-the-application)
  - [Creating a Superuser](#creating-a-superuser)
- [Development](#development)
  - [Built With](#built-with)
- [Author](#author)

## Overview
### The Challenge

The Mc Files project is a comprehensive web application aimed at providing efficient file management capabilities for users. The primary challenges addressed in this project are:

1. **User Registration and Authentication**:
   - Implement a secure user registration system using Django.
   - Allow users to log in, log out, and reset their passwords.
   - Ensure proper authentication mechanisms to protect user data.

2. **File Management**:
   - Enable users to create folders and subfolders for better organization.
   - Provide functionality for users to upload and download files seamlessly.
   - Implement intuitive navigation to allow users to easily browse through folders and files.

3. **User Roles and Permissions**:
   - Differentiate between two types of users: Staff and User.
     - **Staff**: Have only access to the backoffice and can manage user accounts.
     - **User**: Can only manage their own files within the application.
   - Ensure that each user can only access and manage their own files.

4. **Optional Features**:
   - Implement a quota system to limit each user to 50MB of storage.

5. **User Interface and Experience**:
   - Create an intuitive and user-friendly graphical interface.
   - Ensure the application is responsive and works well on various devices.

6. **Best Practices**:
   - Apply web development best practices throughout the project.
   - Use Docker for containerization to improve integration between the backend and frontend.
   - Provide a Makefile with targets for common tasks to streamline development and deployment processes.

### Screenshot

![](/screenshots/landing_page.png)
![](/screenshots/register.png)
![](/screenshots/login.png)
![](/screenshots/empty_dashboard.png)
![](/screenshots/used_dashboard.png)
![](/screenshots/empty_root.png)
![](/screenshots/root_folder.png)
![](/screenshots/empty_folder.png)
![](/screenshots/folder_tab.png)
![](/screenshots/file_tab.png)

## Features

### User Registration and Authentication

The Mc Files project includes robust user registration and authentication features to ensure secure access and management of user accounts. The key functionalities are:

1. **User Registration**:
   - New users can create an account by providing necessary details such as username, email, and password.
   - The registration process includes validation to ensure the uniqueness and correctness of user details.

2. **User Login**:
   - Registered users can log in using their email and password.
   - The login system includes security measures to prevent unauthorized access.

3. **User Logout**:
   - Users can securely log out of the application to end their session.

4. **Password Reset**:
   - Users who forget their password can request a password reset.
   - The system sends a password reset link to the user's registered email.
   - Users can set a new password using the reset link.

5. **Authentication Mechanism**:
   - The system uses Django's built-in authentication framework to handle user authentication securely.
   - Passwords are hashed before storage to enhance security.


### File Management

The Mc Files project provides comprehensive file management capabilities to enable users to organize and handle their files effectively. The key functionalities include:

1. **Create Folders**:
   - Users can create new folders to organize their files.
   - Supports the creation of nested folders, allowing for a hierarchical folder structure.

2. **Upload Files**:
   - Users can upload files to their designated folders.
   - The system supports various file types and ensures secure file storage.

3. **Download Files**:
   - Users can download their files from the application.

4. **Navigate Between Folders**:
   - Users can easily navigate through their folder structure.
   - The interface provides intuitive navigation options to move between different folders and subfolders.

5. **Delete Files and Folders**:
   - Users can delete files and folders they no longer need.
   - Ensures efficient management of storage space by removing unnecessary files.

6. **Optional Storage Quota**:
   - Optionally, each user can be limited to a 50MB storage quota.
   - Helps manage storage resources effectively and prevents overuse.

### User Roles

The Mc Files project distinguishes between two types of users to ensure appropriate access and management capabilities within the application:

1. **Staff**:
   - **Access Level**: Staff users have elevated permissions.
   - **Backoffice Access**: Staff only can access the backoffice interface, which includes administrative functionalities.
   - **User Management**: Staff can manage user accounts, including creating, updating, and deleting users.

2. **User**:
   - **Access Level**: Regular users have standard permissions.
   - **File Management**: Users can only access and manage their own files and folders.
   - **Application Access**: Users do not have access to the backoffice or administrative functionalities.


## Installation

### Prerequisites

Before running this project locally, ensure you have the following installed:

- **Docker**: Follow the installation instructions for [Docker](https://docs.docker.com/get-docker/).
- **Docker Compose**: Ensure Docker Compose is installed as it's used for managing multi-container Docker applications. Installation guide can be found [here](https://docs.docker.com/compose/install/).
- **Poetry**: This project manages dependencies with Poetry. If not already installed, refer to the Poetry installation guide [here](https://python-poetry.org/docs/#installation).


### Installation Steps

Use this steps for installation :
1. **Clone the repository:**
   ```bash
   git clone https://github.com/mccartheney/file-manager-in-django
   cd file-manager-in-django
   ```

3. **Create and configure the .env file:**<br/>
   This credentials is for the email sender (password recover)
   ```bash
   EMAIL_SENDER="emailSender@email.com"
   PASS_EMAIL_SENDER="123"
   ```

2. **Run the setup:**
   ```bash
   make all
   ```

## Usage

### Starting the Application

Use this step to start application (needed to run 'make all' before)

1. **Run the setup:**
   ```bash
   make all
   ```

### Stopping the Application

Use this step to stop application (needed to run 'make all' before)

1. **Run the command:**
   ```bash
   docker-compose down
   ```

### Creating a Superuser

Use this step to create a super user (needed to run 'make all' before), and credentials will be :
   - name : admin
   - email : admin@admin.com
   - pass : admin

1. **Run the command:**
   ```bash
   createsuperuser
   ```

## Development

### Built With

- HTML5
- JavaScript
- Css3

- Django

- Docker
- Makefile


## Author

- **[Mccartheney Mendes](https://github.com/mccartheney)** 
- [LinkedIn](https://www.linkedin.com/in/mccartheney-mendes-892709292/)
- GitHub - [@mccartheney](https://github.com/mccartheney)
- Email - mccartheney@gmail.com