# Catalog for newsdata

### Pre-install

1. virtual machine based on the udacity course

2. vagrant environment 

3. newsdata.sql downloaded and  news successfully created

To create user and table use command
```
psql -d news -f newsdata.sql
```

4. python 2.7 installed correct in vm


### How to use

1. unzip the catalog.zip under /vagrant directory



2. access the catalog directory

```
vagrant@vagrant:/vagrant$ cd catalog/
```

3. run catalog.py

use command
```
vagrant@vagrant:/vagrant/catalog$ python catalog.py
```

or if you chmod 775 to catalog.py

```
vagrant@vagrant:/vagrant/catalog$ ./catalog.py
```

4. open outputfile out.txt  

Then you can find the answer to question


### More

All code have been formated by pep8 and added comment.

