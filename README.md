## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone git@github.com:smrityku/time-tracker.git
```

Install the requirements:

```bash
sudo pip install -r requirements.txt
```

Create the database:

```bash
python manage.py migrate
```

Create Admin user:

```bash
python manage.py createsuperuser
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**
