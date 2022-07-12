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

* `db.insert(varName)`
```mongodb
user1 = {fname:"user1", Lname:"test", age:29, Gender:"M", Country:"US"}

db.insert(user1)

```
* `db.createCollection("users")`

Used to create collection users.


**How to troubleshoot?**

* Open services then go to mongodb services and make sure the service is running.