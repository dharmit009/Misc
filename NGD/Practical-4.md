**Q5. Write a MongoDB query to display all the restaurant which is in the borough 
Bronx**

> db.tyit.find({"borough":"Bronx"}, {"name":1, _id:0, "borough":1}); 

**Q6. Write a MongoDB query to display the first 5 restaurant which is in the borough 
Bronx.
**

> db.tyit.find({"borough":"Bronx"}, {"name":1, _id:0, "borough":1}).limit(5); 

**Q7. Write a MongoDB query to display the next 5 restaurants after skipping first 5 
which are in the borough Bronx**

> db.tyit.find({"borough":"Bronx"}, {"name":1, _id:0, "borough":1}).skip(5).limit(5); 

**Q8. Write a MongoDB query to find the restaurants who achieved a score more than 
90**

> db.tyit.find({"grades.score":{$gt:90}}, {"_id":0, "name":1, "grades.score":1})                                                                                                                                                                             

