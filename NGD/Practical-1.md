# Practical-1: Installing MongoDB

**Aim:** To install MongoDB on your operating system and run some basic queries.

**Download Link:** https://www.mongodb.com/try/download/community

## Starting Point:

First let us start with how to start your mongodb server in order to do so run the following commands:

1. Open a command prompt and run `mongod` which is the daemon for mongodb system.
1. After that run `mongo` to start up the server itself.

## Basic Commands & Queries:

* `show dbs`

This shows list of all the databases.

* `show collections`

This list all the documents which the database has been holding.

* `use ankit`

This will create a database named "ankit" directly at runtime.

* `mongod`: 

Mongod is a daemon process which runs in background. The main purpose of this daemon is to manange your MongoDb tasks.

* `db.system.version.find()`


* `db.documentName.find()`

use to find the document.

* `db.documentName.insert(varName)`
```mongodb
user1 = {fname:"user1", Lname:"test", age:29, Gender:"M", Country:"US"}

db.insert(user1)

```
* `db.createCollection("users")`

Used to create collection users.

## Multiple Inputs:

``` mongodb
for (var i = 1, i <=20, i++) db.users.insert({fname: "test" + i, "age":10+i, "gender":"f", "country":"India"})

```

**Program Flow:**

1. mongod
1. mongo
1. use test
1. db.createCollection("actors")
1. user1={fname: "walter", lname: "white", age:29, gender: "m", country: "us"}
1. db.actors.insert(user1)
1. db.actors.find()

**How to troubleshoot?**

* Open services then go to mongodb services and make sure the service is running.


