**Q5. Write a MongoDB query to display all the restaurant which is in the borough 
Bronx**

> db.tyit.find({"borough":"Bronx"}, {"name":1, _id:0, "borough":1}); 

**Q6. Write a MongoDB query to display the first 5 restaurant which is in the borough 
Bronx.
**

> db.tyit.find({"borough":"Bronx"}, {"name":1, _id:0, "borough":1}).limit(5); 