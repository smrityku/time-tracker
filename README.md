## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone git@github.com:smrityku/time-tracker.git
```

Install the requirements:

```bash
sudo pip install -r requirements.txt
```

Install mysqlclient:

```bash
pip install mysqlclient
```

Create the database:

```bash
python manage.py migrate
```

Create Admin user:

```bash
python manage.py createsuperuser
```

Run test Code:

```bash
python manage.py test
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**
