# Do It Now

"Do It Now" is a To-Do list web application built using Django, HTML, CSS, and PostgreSQL. This application allows users to organize their tasks by grouping them into sections (cards) based on categories like 'Work', 'Home', etc. Each group holds multiple related tasks, making it easy to manage tasks efficiently.

## Features

- **Group-based Task Management:** Users can create task groups like "Work", "Home", etc., and add multiple related tasks within each group.
- **Due Date Tracking:** Each task can be assigned a due date. Tasks that are overdue are automatically moved to the "Due Task" section.
- **Task Editing:** Users can edit both task descriptions and due dates.
- **Task Deletion:** Completed tasks can be deleted from the list. Once all tasks within a group are deleted, the entire group is automatically removed.
- **Responsive Design:** The frontend is built with HTML and CSS, making it mobile-friendly and user-friendly.

## Technologies Used

- **Frontend:** HTML, CSS
- **Backend:** Django
- **Database:** PostgreSQL
- **Other Tools:** Django ORM for database interactions

## How to Run This Project

Follow these steps to get the "Do It Now" application up and running on your local machine.

1. **Clone the Repository**
    ```bash
    git clone https://github.com/SambhavSurthi/Todo-List.git
    cd just-do-it
    ```

2. **Set Up the Virtual Environment**
   You need to create a virtual environment to install the dependencies without affecting the global Python environment.
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Windows, use venv\Scripts\activate
    ```

3. **Install Dependencies**
   Install the required Python packages using pip:
   ```bash
    pip install django
    ```
    ```bash
    pip install psycopg2
    ```

5. **Set Up PostgreSQL Database**
   Make sure PostgreSQL is installed on your machine. Then create a database for the project.
    ```sql
    CREATE DATABASE DoItNow;
    ```
   Update the `DATABASES` setting in `settings.py` with your PostgreSQL credentials:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'DoItNow',
            'USER': 'postgres',
            'PASSWORD': 'your_postgres_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

6. **Migrate Database**
   After configuring the database, apply the migrations to set up the database schema:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7. **Create Superuser**
   To access the Django admin panel, you need to create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

8. **Run the Development Server**
   Start the Django development server:
    ```bash
    python manage.py runserver
    ```
   Access the website by navigating to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

9. **Access Admin Panel**
   You can manage the application data via the Django admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) using the superuser credentials.

## Additional Notes

- **Managing Tasks:** Tasks are automatically grouped by their related category. Tasks that pass their due date are moved to the "Due Task" section.
- **Deleting Tasks:** Deleting all tasks from a group will automatically remove the entire group.

Feel free to fork the project, make your customizations, and submit pull requests. Enjoy organizing your tasks with Just Do It!
