# Practical 2

**How to import the json file?**

First, move the `restaurants.json` file from your downloads folder to `C:\Program Files\MongoDB\Server\4.0\bin` folder then execute the following in the **windows cmd** itself:

```mongodb

mongoimport --host localhost --db demo --collection tyit < restaurants.json

```

After that start the mongo shell by executing `mongo` and continue with the following:

``` 

show dbs
use demo 
show collections
db.tyit.find()
db.tyit.find().pretty()

```