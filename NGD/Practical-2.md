# Practical 2

**How to import the json file?**

First, move the `restaurants.json` file from your downloads folder to `C:\Program Files\MongoDB\Server\4.0\bin` folder then execute the following in the **windows cmd** itself:

```mongodb
mongoimport --host localhost --db demo --collection tyit < path to restaurants.json file

```

After that start the mongo shell by executing `mongo` and continue with the following:

```mongodb
show dbs
use demo 
show collections
db.tyit.find()
db.tyit.find().pretty()

```

**Q1. Write a MongoDB query to display all the documents in the collection restaurants.**

> db.tyit.find()

**Q2. Write a MongoDB query to display the fields , restaurant_id, name, borough and cuisine for all the documents in the collection restaurant.**

> db.tyit.find({}, {restaurant_id: 1, name:1, borough:1, cuisine:1, _id:0})