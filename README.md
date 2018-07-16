## Running the Project Locally

First, setup python3 and pip and then clone the repository to your local machine:

```bash
git clone git@github.com:smrityku/time-tracker.git
```
```bash
cd time-tracker
```

Install the requirements:

```bash
sudo pip install -r requirements.txt
```

Open mysql console and create a empty database e.g 'timetracker_db'. Update settings.py in timetracker app and then run migration by following command:

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
