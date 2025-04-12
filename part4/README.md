<img src="https://ml.globenewswire.com/Resource/Download/ea0a5220-97e2-43ce-acb7-038eecef6315?size=3" alt="Description of the image" width="417" />

# HbnB Project - Adrien Vieilledent

## 🔍  Project Overview

This project, part 4 of the **HBNB** (HolbertonBnB), is a web application designed to simulate a vacation rental platform. It provides users with functionalities such as viewing, filtering, and reviewing places, while also allowing owners to manage their listings. The backend API is built using **Flask**, and the frontend uses **HTML**, **CSS**, and **JavaScript**.


## ⚙️ Installation :

This installation guide is tailored for systems running **Ubuntu 24.04**. Make sure your environment is up to date by running 
```
sudo apt update && sudo apt upgrade
```
This ensures compatibility with dependencies and tools used during the installation.

---


### You will clone the repository to obtain and test the API / frontend project, part 4 of HbnB.

- You need to create an executable file **install.sh** :
```bash
touch install.sh &&
chmod u+x install.sh
```

- Then copy inside the **install.sh** this code:

<details>

```bash
#!/bin/bash

# Function to clone the 'part4' folder from the GitHub repository
clone_part4() {
echo "Cloning the 'part4' repository..."
git clone https://github.com/vlldnt/holbertonschool-hbnb.git

# Navigate into the 'part4' folder
cd holbertonschool-hbnb/part4
echo "The 'part4' folder has been cloned and you are now in that folder."

}

# Function to create a virtual environment and install dependencies
setup_venv_and_install_requirements() {
echo "Creating the virtual environment..."

# Create a virtual environment (venv)
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
echo "Installing dependencies from 'requirements.txt'..."

# Check if the requirements.txt file exists
if [[ -f "requirements.txt" ]]; then
pip install -r requirements.txt
echo "Dependencies installed successfully."
else
echo "'requirements.txt' file not found."
exit 1
fi
}

# Function to run the API
run_api() {
echo "Starting the API..."

# Run the Python file to start the API
python3 run.py
}

# Run the functions
clone_part4
setup_venv_and_install_requirements
run_api
```
</details>

### Step of the install.sh :

**First lauch the executable:**
```python
./install.sh
```

1. Clone the GitHub repository from vlldnt.
2. Navigate into the holbertonschool-hbnb/part4 folder.
3. Display a message confirming that the part4 folder has been cloned and the current directory is inside it.
4. Create a Python virtual environment using venv.
5. Activate the virtual environment.
6. Install the dependencies needed using `pip install -r requirements.txt`
7. Start the Python script `run.py` to launch the API.


## 🔧 Current Features
You can now launch the `index.html` file in your Visual Studio Code 

You can explore additional features by navigating through the site and interacting with different elements:
- User Authentication
    - Log in
    - Register (if you don’t have an account)
- Place Listings
    - Filter places by price (50€, 100€, 150€, or view all)
    - View detailed information by clicking on a place (image)
- Place Details
    - Photo gallery
    - Description
    - Available amenities
    - User reviews  
    - Option to add a new review

## 🚧 Upcoming Features
- Ability to create a new place listing
    - Owners will have the option to edit their listings
-Disable the "Add Review" button once a user has already submitted a review for a place 
- General improvements to overall functionality and design
- Enhanced responsive design for better compatibility across smartphones, tablets, and various screen sizes
- Enable registration and login using Apple, Google, or Facebook accounts
- Web deployement

## 🧱 Structure of the project and technologies:

The project consists of three main parts: Frontend, Backend, and Database.
- **Frontend:**
    - Languages: HTML (structure), CSS (layout & styling), JavaScript (interactivity)

- **Backend:**
    - Language: Python
    - Framework: Flask (for RESTful APIs)
        - Extensions:
            - Flask-RESTx (API structuring & documentation)
            - Flask-JWT-Extended (JWT authentication)
            - Flask-Bcrypt (password hashing)
            - Flask-CORS (cross-origin requests)

- **Database:**
    - Technology: SQLite (lightweight relational database)
    - ORM: SQLAlchemy (for database interaction)

- **Other Tools:**
    - Git (version control)
    - VS Code (IDE)
    - Mermaid (diagram generation)

## 👤 Authors


[Adrien Vieilledent](https://github.com/vlldnt) - C#25 - <img src="https://ml.globenewswire.com/Resource/Download/ea0a5220-97e2-43ce-acb7-038eecef6315?size=3" alt="Description of the image" width="100" />
