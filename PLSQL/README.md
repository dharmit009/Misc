----

# Temporal Database

```sql
create table emp (empid varchar2(20) primary key, empname varchar2(20), jdate date, rdate date);

```

```sql
insert into emp values(1, 'bency', to_date('07-08-1993', 'DD-MM-YY'), to_date('20-10-2025', 'DD-MM-YY'));
```

## Multiple Inputs

```sql
insert into emp values(&empid, '&empname', to_date('&jdate', 'dd-mm-yyyy'), todate('&rdate', 'dd-mm-yyyy'));
```

## Update Statements:

```sql
update emp set jdate='01-JAN-2001' where empid=1;
update emp set jdate=to_date('01-01-2001', 'DD-MM-YYYY') where empid=1;

```
----

# Country Table:

```sql
create table country (cid int, cname varchar(30), ctime date);
```

## Insert

```sql
insert into country values(&cid, '&cname', to_date('&ctime', 'hh24:mi'));
```

## select

```sql
select * from country where ctime=to_date('13:30', 'hh24:mi');
```

----

# Direct Multiplication:

The below line will create a new column as total which will hold
multiplication of (no_of_shares and * price_per_share)

``` sql
select (no_of_shares * price_per_share) as TOTAL
from shares where cname='google';
```

``` sql
select min(price_per_share), max(price_per_share), max(price_per_share)
from shares;
```


``` sql
select trans_time from shares where trans_time between to_date('11:00', 'hh24:mi')
and to_date('15:00', 'hh24:mi');
```

----

### Drop a table:

**SYNTAX:** DROP table tableName

```sql
DROP table emp
```

----

# Triggers:

This will create DEPT table ...

``` sql
create table dept(did int primary key, dname varchar(20), thrs int);
```

This will create EMP table ...

``` sql
create table emp(eid int primary key, ename varchar(20), ehrs int,
edid int, foreign key(edid) references dept(did));
```

## Insert Trigger ...

``` sql
CREATE OR REPLACE TRIGGER abc
AFTER INSERT ON emp
FOR EACH ROW
WHEN(New.edid is not null)
BEGIN
UPDATE dept SET thrs=thrs+:New.hrs
WHERE did=:New.edid;
END;
/

```
**Inserting values in TABLE 1:**

```sql
insert into dept values(&did, '&dname', &thrs);
```

**Inserting values in TABLE 2:**

```sql
insert into emp values(&eid, '&ename', &hrs, &edid);
```

## Update Trigger

**1 UPDATE:**

**2 UPDATES:**


## Delete Trigger ...

``` sql
CREATE OR REPLACE TRIGGER deleterr
AFTER delete ON emp
FOR EACH ROW
WHEN(Old.edid not null)
BEGIN
update dept
set thrs=thrs-:Old.hrs
WHERE did=:Old.edid;
end;
/
```

```sql
delete from emp where eid=1
```

