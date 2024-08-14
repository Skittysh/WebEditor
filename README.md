# Web-based File Manager

## Overview

This project provides a web-based application for managing and editing files from your browser.  
The app allows users to create, edit, delete, and save files through an intuitive user interface.  
It was created with the goal of simplifying file management in web environments.   

Created by [Skittysh](https://github.com/skittysh) with Python and Flask for the back-end and DHTML for the front-end. 
 
 Currently supports Linux and Windows operating systems. 

## Key Features
* File Management: Create and delete files directly from the web interface.
* File Editing: Edit your files' contents in a simple and performance-focused editor.
* File Saving: Save your changes directly to the server using an efficient POST request.

## Getting Started
### Requirements
To run this application, ensure the following are installed on your machine:
* Python 3.x
* Flask

### Installation

1. Clone the repository to your computer.    

2. Navigate to the project directory.    

3. (Optional) Install Python and Flask: 

    3a - Installing Python    
    For Windows: [Official Python website](https://www.python.org/downloads/windows/)  
    For Linux: `sudo apt install python3` 
    
    3b - Installing Flask   
    `pip install -U Flask`
    
4. Run the application:   
`flask --app app.py run`   

5. Open the highlighted link in your browser of choice.

## Directory Structure
`templates/`: contains the main, "index" page - *index.html*  
`app.py`: the main application file containing the Flask server setup and route handling.  
`FileManager/`: module that handles operations on the files server-side.  
`Notes/`: directory responsible for containing the edited files.  

## Customization
The appearance can be customized through editing the CSS in the *index.html* file.  
Functionality can be changed in *app.py* and *FileManager.py*. 
