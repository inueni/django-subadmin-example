# django-subadmin-example

Sample application to demonstrate `django-subadmin` usage.

 ## Installation

Checkout code from GitHub

 ```
    git clone https://github.com/inueni/django-subadmin-example.git 
 ```

Switch to `django-subadmin-example` directory and run the following commands (you should do this in `virtualenv`).

```
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py fakedata
python manage.py runserver
``` 

Then open django admin (<http://127.0.0.1:8000/admin/>) in your browser, log-in and explore `MailingList` section to see `django-subadmin` in action. Once you navigate to a specific mailing list, look at _Subscribers_ and _Messages_ buttons next to _History_. Clicking those will open `SubAdmin` instances for those models. 