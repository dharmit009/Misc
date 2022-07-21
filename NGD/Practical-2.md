# Practical 2

**How to import the json file?**

First, move the `restaurants.json` file from your downloads folder to `C:\Program Files\MongoDB\Server\4.0\bin` folder then execute the following:

```mongodb

mongoimport --host localhost --db demo --collection tyit < restaurant.json

```