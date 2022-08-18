**Q5. Write a MongoDB query to display all the restaurant which is in the borough 
Bronx**

> db.tyit.find({"borough":"Bronx"}, {"name":1});