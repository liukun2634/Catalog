# Catalog Web APP


#### 1.Install Vagrant and VM

Set up your Vagrant and VM refer to https://classroom.udacity.com/courses/ud330/lessons/3967218625/concepts/39636486110923

#### 2.Get into the directory 

Cd into the downloaded catalog directory 

```
cd catalog
```
#### 3.Vagrant up and ssh

Using vagrant up and vagrant ssh for setting the vagrant enviroment. Then cd into the vagrant directory

```
cd /vagrant
```

#### 4. Run the project

You can easy to use 
```
python project.py
```
Or

```
chmod 755 project.py
./project.py
```
#### 5. Get the page
 
In your browser [localhost:8000](localhost:8000/) or [localhost:8000/catalog](localhost:8000/catalog) to visit my catalog web app.

PS. My VM can't login in to google because of the Chinese GFW
So I use my Ubuntu Desktop by using ipv6 proxy to test the login function. However, it should works fine if your VM can connect to google.

#### 6. More

1. python 2.7 is needed.(Haven't test in python 3.0)

2. screen shot is present in screenshot directory .

3. **Reset database just move category.db and run category_database_setup.py and insert_data_database.py
**
4. All the python, html, css file have been neat formatted and valided.

5. Bootstrap is used for different device command.

#### Update in 7.23

1. Add authorizate to different users to edit and delete its own items.

2. Formatted py code by sublime pep8 plugin (atom auto-pep8 package cannot check the code length).