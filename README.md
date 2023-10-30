# Bug Reporting Application
This is a bug reporting application built with Python, Django and SQLite. A user can report a bug, view all reported bugs and view the details of a bug.

This project is a compilation of four microtasks towards the  Outreachy Contribution for Wikimedia's CapX project.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/ikeadeoyin/Bugsite.git
   ```

2. Navigate to the project directory:

   ```
   cd Bugsite
   ```

3. Setup a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate (Linux/Mac) # On Windows use venv\Scripts\activate 
   ```
   
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```
   python manage.py migrate
   ```
5. Create a superuser:
   
   ```
   python manage.py createsuperuser
   ```

6. Start the development server:
    ```
    python manage.py runserver
    ```
By default, the server will start on `http://127.0.0.1:8000/bug/`. Open this URL in your browser.

## Usage

### Access the admin portal 
  Navigate to `http://127.0.0.1:8000/admin` to create, update and delete bugs via a user interface.
  
<img width="1510" alt="Screenshot 2023-10-04 at 18 07 57" src="https://github.com/ikeadeoyin/Bugsite/assets/36523905/4e0c1549-45f3-4515-8d5d-ba6aedcdf687">

### Create a bug
Navigate to `http://127.0.0.1:8000/bug/register/`. Enter the required details and submit the form.

### View all bugs

Navigate to `http://127.0.0.1:8000/bug/bug_list/` You can click on each bug item to view the details.

### View the details of a bug
Navigate to `http://127.0.0.1:8000/bug/<int:pk>/`. Replace <int:pk> with the bug's id, for example: `http://127.0.0.1:8000/bug/1/`

## Tests
Run tests with: `python manage.py test bug`
