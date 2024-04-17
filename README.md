# Universal Library
The Universal library is an answer to the rise of accessibility of information together with modern conveniences. A library without a website may have its charm but will not be noticed or used as opposed to a library with a website. In an age where attention spans are lower than ever but desire for information is still great, we want to bridge the gap and make it easier for anyone to pick up a book who hopes to learn more or enjoy a great book. This extends to our desire to similarly aid people find a quiet space to study or find a space for a group to collaborate together. Our product, the “Universal Library” , will allow users to expedite their business with the library to match the speed of our world today!

## User Guide
Expected to be installed:
```
Python (3.12.3 recommended)
npm (10.5.2 recommended)
pip (24.0 recommended)
Nodejs (21.7.2 recommended)
MySQL Workbench (8.0 Recommended)
```

First start MySQL Workbench and start a new connection, you can use whatever you want for the password but just remember it for later.

First git clone the repository at https://github.com/krjeo/CPSC471 and move into it

```
$ git clone https://github.com/krjeo/CPSC471.git
```
```
$ cd CPSC471
```
then make sure to change to the main2 branch by running the command:
```
$ git checkout main2
```
First we want to make sure django and django REST framework are installed:
```
$ pip install django djangorestframework
```
```
$ pip install pymysql django_filter django_tables2 Pillow
```

Then we have some more installations to be done for the project itself through:
```
$ npm i webpack webpack-cli --save-dev
$ npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
$ npm i react react-dom --save-dev
$ npm install @material-ui/core
$ npm install @babel/plugin-proposal-class-properties
$ npm install react-router-dom
$ npm install @material-ui/icons
```
Then make sure that the information about the database connection you started, matches up with the information in the file mysite/settings.py around lines 81-90 (the DATABASES variable).

At this point you can start the webserver and access the website by running both of these commands in separate shells:

This one in the base directory of the repository:
```
$ python manage runserver
```
This one in the frontend directory, just one level down from the base directory:
```
$ npm run dev
```

The runserver command will likely complain about missing migrations which we can remedy next. Some function of the website may be not working as it should without the database properly migrated and connected.

Then we’ll want to migrate database information:
```
$ python manage.py makemigrations
$ python manage.py migrate
```
	
We had a few issues with writing the migrations, especially the ones in the api/migrations directory (relative to the base repository directory). When running the above migrate command, errors may occur indicating problems with the database. Instead of leaning on django for database management, we used MySQL Workbench so we can recommend you use it too, in order to get the website working properly.

To start working with the workbench, after connecting to the previously made connection, create a new schema (if it is not already present under the Schemas tab) and name it to match the name present in the mysite/settings.py file mentioned earlier. After creating this new schema you may try the above migration commands again.

Depending on the error you may need to change the schema via the MySQL Workbench. You may need to create a table that is missing, remove or add a table attribute, etc.

Different errors gotten from the migrate command you may need to go to the file and remove a redundant operation. For your information the migration that may cause an error will have the form <app>.<filename-without-extension> so the migration api.0026_rename_floor_no_studyroom_floorno_and_more will be found in folder api/migrations , in the file 0026_rename_floor_no_studyroom_floorno_and_more.py. Each operation is an item in the operations list.

Apologies for these issues being present. We could not fix them in time.


