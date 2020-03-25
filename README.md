# django-rest-apis

Install packages
The easiest way to install the python modules and keep them up-to-date is with a Python-based package manager called Pip
Download <a href="https://bootstrap.pypa.io/get-pip.py">get-pip.py</a> to a folder on your computer. Open a command prompt window and navigate to the folder containing get-pip.py. Then run python get-pip.py. This will install pip

Create virtual environment<br>
<code>pip install virtualenv</code>

activate environment<br>
for windows<br>
<code>myenv\Scripts\activate</code>

for Mac<br>
<code>source myenv/bin/activate</code>

Install all requirements of this project<br>
<code>pip install requirement.txt</code>
<br><br>
<br><br>

Set the database to store data >> <br>
Default database is 'django.db.backends.sqlite3'. which is file based database<br>
To create table in database<br>
<code>python manage.py makemigrations</code><br>
<code>python manage.py migrate</code>
<br><br>

then run the apis using<br>
<code>python manage.py runserver localhost:8000</code>
<br><br>

APIs are ready to use now<br>
Apis can be accessed with url<br>
Get Request >><br>
http://localhost:8000/leads/
<br><br>
POST Request >><br>
http://localhost:8000/leads/
<br>
Headers : Content-Type: application/json
<br>
Body: <code>{
"first_name":"Example",
"last_name":"Lead",
"email":"example@email.com",
"notes":"This is example notes",
"is_contacted":true
}
</code>
<br><br>
Update Request >><br>
http://localhost:8000/leads/<lead-id>/
 <br>
 Body: <code>{
"first_name":"Update",
"last_name":"Lead",
"email":"newemail@email.com",
"notes":"This is example notes",
"is_contacted":true
}
</code>
  <br><br>
Delete Request >>
http://localhost:8000/leads/<lead-id>/
