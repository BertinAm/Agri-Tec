# Agri-Tec
Agri-Tec is a GitHub repo for an agricultural tech project, streamlining and modernizing the industry. It connects farmers, buyers, and delivery services through an integrated platform.

## Installation
1. To install Python on your machine, you can follow these steps:
    Visit the official Python website: ```https://www.python.org/```
    Click on the "Downloads" tab.
    Choose the appropriate Python version for your operating system. For example, if you're using Windows, select the Windows installer.
    Once the installer is downloaded, run the installer executable.
    In the installer, make sure to check the box that says "Add Python to PATH" (on Windows) or "Install Python to the system or user environment variables" (on macOS).
    Follow the prompts and complete the installation process.
    After the installation is complete, you can open a command prompt (or terminal) and verify that Python is installed by running the following command:

2. Clone the repository:
   ```git clone https://github.com/BertinAm/Agri-Tec.git```

## Configuration

1. Open the cloned project  in your code editor for example:
  ```Vscode``` or ```Pycharm```

2. After opening the cloned project  in your editor open the terminal in your code editor

3. Proceed to installing the virtual environment using the pip command in your terminal:
    ``` pip install virtualenv ```

4. Next acting the virtual environment of the project by using the following command:
   ```source venv/bin/activate ```

5. After the Venv is activated you can proceed to install all the necessary libraries the project needs with the following command:
    ```pip install requirements.txt```

6. After installing the requirements we then create a superuser or admin that can manage and authenticate users, products and other entities. To create an admin we use the following command:
    ``` python manage.py createsuperuser```

7. After installing all the required libraries your good to go

## Visualising the Project

1. We deployed the application to render which is a Paas(Platform as a service) that offers deployment and testing: 
   You can access via the following link: ``` https://app-wkkd.onrender.com```
    1. You can view the search product api by using the following link: ``` https://app-wkkd.onrender.com/api/search ```
    2. You can view the add product api by using the following link : ``` https://app-wkkd.onrender.com/api/add```
    3. You can log in as an admin to access the admin dashboard using this link: ``` https://app-wkkd.onrender.com/admin```
2. Since the database of the project is hosted on render you can access the project locally and still perform changes to the database online in other to do that do the following
   1. run the following command:
       ``` export DATABASE_URL=postgres://agritec_user:NMN1vbvo8n9Ky37xgdmW4haV1UgdoLJj@dpg-ci1qu767avj2t31ddsig-a.oregon-postgres.render.com/agritec``` to configure the database on your local machine such that you can do changes to it online
   2. After that command you can run the application using the following link:
       ``` python manage.py runserver ```
   3. You can check out the local deployed version on any browser using the link:
       ``` localhost:8000```
   4. To make use of the search api using type the following in your browser:
       ``` localhost:8000/api/search```
   5. TO make use of the add product api type the following in your browser:
      ``` localhost:8000/api/add```
   6. To make use of the admin dashboard you log in with the following link in your browser:
      ``` localhost:8000/admin```
   For all the above links to work make sure your project is running locally successfully 

That's how to setup our project locally and make use of api's we created