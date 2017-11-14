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

Then open django admin (<http://127.0.0.1:8000/admin/>) in your browser, log-in and explore `MailingList` section to see `django-subadmin` in action.

## Screenshots

![alt text](/screenshots/subadmin_screenshot_1.png?raw=true)

 `SubAdmin` instances are accesible from edit view of the `ModelAdmin` instance they are nested in. In the screenshot above you can see links to _Subscribers_ and _Messages_ subadmins (marked with red rectangle) for `MailingList` instance _Mailing list 5_.

---

![alt text](/screenshots/subadmin_screenshot_2.png?raw=true)

 `SubAdmin` looks and behaves just like a regular `ModelAdmin`, but looking at breadcrumbs (marked with red rectangle), you can see it is nested within another `ModelAdmin`. Displayed `Subscribers` are limited to those related to `MailingList` instance _Mailing list 5_.

---

 ![alt text](/screenshots/subadmin_screenshot_3.png?raw=true)

When adding or editing objects with `SubAdmin`, `ForeignKey` fields to parent instances are removed from the form and automatically set when saving. In this example `mailing_list` field is removed and value is set to parent `MailingList` instance _Mailing list 5_.