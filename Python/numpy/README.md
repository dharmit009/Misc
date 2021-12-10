# What is NumPy: 

NumPy is a commonly used Python data analysis package. NumPy was originally
developed in the mid 2000s, and arose from an even older package called
Numeric. This longevity means that almost every data analysis or machine
learning package for Python leverages NumPy in some way.

## Limitation of NumPy: 

* All the elements in the array should be of same data type. 

## Zero's Array:

An array with all the elements as zero. 

**Code:**

```
import numpy as np 
zeroArray = np.zeros((3,3));
print("zeroArray = "); 
print(zeroArray);

# Note: 2 Arrays doesn't mean create 2 arrays it means it's a 
# list of lists i.e a list of 2 arrays with 3 rows and 2 columns.
# meaning it's an 3  dimensional list. 
# zeros(2 Arrays, 3 rows, 4 columns);

y = np.zeros((2, 3, 4));
print("y = "); 
print(y);
```

**Output:**

> zeroArray = 
> 
> [[0. 0. 0.]
> 
>  [0. 0. 0.]
> 
>  [0. 0. 0.]]
> 
> y = 
> 
> [[[0. 0. 0. 0.]
> 
>   [0. 0. 0. 0.]
> 
>   [0. 0. 0. 0.]]
> 
>  [[0. 0. 0. 0.]
> 
>   [0. 0. 0. 0.]
> 
>   [0. 0. 0. 0.]]]

## One's Array:
An array with all the elements as one. 

**Code:**

```
import numpy as np 
onesArray = np.ones((3,4));
print(onesArray);

```

**Output:**

> [[1. 1. 1. 1.]
> 
>  [1. 1. 1. 1.]
> 
>  [1. 1. 1. 1.]]


## Random Array: 

**Code:**
```
import numpy as np 
import random
randomArray = np.random.rand(3,3);
print(randomArray);

```

**Output:**

> [[0.45081217 0.92301296 0.3306152 ]
> 
>  [0.79870788 0.27694244 0.0169671 ]
> 
>  [0.22943038 0.84797384 0.49086549]]

## Random Array with range: [SUPER IMPORTANT]

**Code:**

```
import numpy as np 
randomArray = np.random.randint(0,100,(3,3)); # create a random array of 3x3 with values ranging from 0 to 100; 
print(randomArray);
```

**Output:**

> [[68 49  8]
> 
>  [60 21 65]
> 
>  [41 96 12]]

# NumPy Functions: 

### array():

The `array()` Function is used to create arrays by passing the values as a list.
Here is a small example: 

**Code:**

```
import numpy as np
x = np.array([1,2,3,4]); 
print(x);

```

**Output:**
 
> [1 2 3 4]

### type():

The `type()` function returns the data type. Here are some examples: 

**Code:**

```
import numpy as np
x = np.array([1,2,3,4]); 
print(type(x));

y = np.array(["V", "A", "M", "D"]); 
print(type(y));

a = [1,2,3,4,4,5];
print(type(a)); 

b = [.11,.2,0.3,4.4,4.4,0.5];
print(type(b)); 

c = ["Hello", "world"];
print(type(c)); 

```

**Output:**

> <class 'numpy.ndarray'>
>
> <class 'numpy.ndarray'>
>
> <class 'list'>
>
> <class 'list'>
>
> <class 'list'>


### ndim:

The `ndim` function is used to returns the dimensions of an array. 

**Code:**

```
import numpy as np
x = np.arange(9) 
print(x); 
print(x.ndim); 

x = np.arange(9).reshape(3,3); 
print(x); 
print(x.ndim); 

y = np.arange(10).reshape(5,2); 
print(y); 
print(y.ndim); 

y = np.zeros((2, 3, 4));
print(y); 
print(y.ndim); 

```

**Output:**

> [0 1 2 3 4 5 6 7 8]
> 
> 1
> 
> [[0 1 2]
> 
>  [3 4 5]
> 
>  [6 7 8]]
> 
> 2
> 
> [[0 1]
> 
>  [2 3]
> 
>  [4 5]
> 
>  [6 7]
> 
>  [8 9]]
> 
> 2
> 
> [[[0. 0. 0. 0.]
> 
>   [0. 0. 0. 0.]
> 
>   [0. 0. 0. 0.]]
> 
> 
>  [[0. 0. 0. 0.]
> 
>   [0. 0. 0. 0.]
> 
>   [0. 0. 0. 0.]]]
> 
> 3

## Parameters: 

### dtype:

The dtype parameter is used to initialize the datatype of the array. Here is an example: 

**Code:**

```
import numpy as np
x = np.array([1,2,3,4], dtype='int32'); 
print(x);
x = np.array([1.1,2,3,4], dtype='float'); 
print(x);

```

**Output:**

> [1 2 3 4]
>
> [1.1 2.  3.  4. ]

## Question: 

In this tutorial, we’ll walk through using NumPy to analyze data on wine
quality. The data contains information on various attributes of wines, such as
pH and fixed acidity, along with a quality score between 0 and 10 for each
wine. The quality score is the average of at least 3 human taste testers. As we
learn how to work with NumPy, we’ll try to figure out more about the perceived
quality of wine.

### Key Points Of Question: 

- Attributes Include: `pH`, `Fixed Acidity`, `Quality Score [0-10]`. 
- Atleast 3 testers for each wine. 
- There is a quality score for each and every wine. 
- To figure out the quality of the wine. 

### Statistics Of Data: 

File Name       : `winequality-red.csv`

File Extension  : `.csv`

Data Format     : `ssv` a.k.a `Semicolon Seperated Values`

Rows            : `winequality-red.csv`

Columns         : `.csv`

As the data is in Semicolon Seperated Values inside a `.csv` file we will need
import a python library in order to access the data. The package which we are
going to use is `csv`. We will read the data using `csv.reader` object. 

**Code:**

```
import csv
# opens the csv file in read-only mode. 
with open('winequality-red.csv', 'r') as f:  
  wines = list(csv.reader(f,delimiter=';'))

print(wines); # contains 1600 rows as a single list. 

```

**Output:**

_Note: The output has been truncated as there are 1600 rows of data stored
in variable `wines`. Here we are only listing out top 3 rows._

> [['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
> 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH',
> 'sulphates', 'alcohol', 'quality'],
> 
> ['7.4', '0.7', '0', '1.9', '0.076', '11', '34', '0.9978', '3.51', '0.56', '9.4', '5'],
> 
> ['7.8', '0.88', '0', '2.6', '0.098', '25', '67', '0.9968', '3.2', '0.68', '9.8', '5']]

### Extracting Data: 

Now let us extract quality of wine from the csv file. The quality of wine is
the last column in the dataset so we can use `array[-1]` to access the data but
remember the stored variable `wine` has 1600 rows in total stored as a list. So
first we will need to use a for loop and access each and every data row and
convert the data into float as list typically store the data in string format.
After that we will calculate the mean or average quality of wine. 

**Code:**

```
import numpy as np
import csv

# opens the csv file in read-only mode.
with open('winequality-red.csv', 'r') as f:  
    wines = list(csv.reader(f,delimiter=';'));

# creates a list of quality 
quality = [(float(eachRow[-1])) for eachRow in wines[1:]]; 

averageQuality = sum(quality)/len(quality);
print("Average Quality Of Wine: ", averageQuality); 

```

**Output:**

> Average Quality Of Wine:  5.6360225140712945

## Using NumPy To Read Files: 

It’s possible to use NumPy to directly read csv or other files into arrays. We
can do this using the `numpy.genfromtxt` function.

**Code:**

```
import numpy as np 
# Reads winequality-red.csv, seperates the data by ';' 
# and skips 1st row which are headers; 
# Doubt: What if i wanted to skip multiple lines do i
# specify skip_header=(1,5) or just skip_header=5
wines=np.genfromtxt("winequality-red.csv", delimiter=";", dtype=float, skip_header=1)
print(wines);

```

**Output:**

_Note: The output is truncated._


> [[ 7.4    0.7    0.    ...  0.57   9.4    5.   ]
>
>  [ 7.8    0.88   0.    ...  0.68   9.8    5.   ]
>
>  [ 7.8    0.76   0.04  ...  0.65   9.8    5.   ]
>
>  ...
>
>  [ 6.3    0.51   0.13  ...  0.75  11.     6.   ]
>
>  [ 5.9    0.645  0.12  ...  0.71  10.2    5.   ]
>
>  [ 6.     0.31   0.47  ...  0.66  11.     6.   ]]



## NumPy Array:

In a NumPy array, the `number of dimensions` is called the `rank`, and `each
dimension` is called an `axis`. So the rows are the first axis, and the columns
are the second axis.

Our task is to convert the `wine` list of lists into array using numpy. To
create an array we use the function `numpy.array()`. If we pass `wine` as an
argument to the function it will automatically create a numpy array. We will
need to convert each and every dataset into float as data type is string by
default. This conversion of each datatype into float can be achieved in
multiple ways: 

1. By passing each row and each data into a for loop and doing type casting. 
1. By passing `dtype` argument to `numpy.array()` function.

**Code:**

```
import csv 
import numpy as np 

with open('winequality-red.csv', 'r') as f: 
  wines=list(csv.reader(f, delimiter=";"));

wines = np.array(wines[1:], dtype=float);
print(wines.dtype)

```

**Output:**

> float64
> (1599, 12)


## Selecting Individual Cell: 

**Code:**

```
import numpy as np 
wines=np.genfromtxt("winequality-red.csv", delimiter=";", dtype=float, skip_header=1)
print(wines[2,3]);

```

**Output:**

> 2.3

## Slicing till Individual Cell: 

**Code:**

```
import numpy as np 
wines=np.genfromtxt("winequality-red.csv", delimiter=";", dtype=float, skip_header=1)
print(wines[1:2,3]);

```

**Output:**
[2.6]


## Understanding Slicer Properly: 

**Code:**
```
import numpy as np
a = np.arange(25).reshape(5,5);
print(a);

print("\n######### Solution #########\n");
print(a[2:4,1:4])

print("\na[x1:x2, y1:y2]")
comment = """
Where,
    x1 is the starting index for row; 
    x2 is the ending index for row; 
    y1 is the starting index of column; 
    y2 is the starting index of column;
""";
print(comment);

print(a[:,-1]);
print(a[3,:]);
```

**Output:**


> [[ 0  1  2  3  4]
> 
>  [ 5  6  7  8  9]
> 
>  [10 11 12 13 14]
> 
>  [15 16 17 18 19]
> 
>  [20 21 22 23 24]]
> 
> ######### Solution #########
> 
> [[11 12 13]
> 
>  [16 17 18]]
> 
> a[x1:x2, y1:y2]
> 
> Where,
>     x1 is the starting index for row; 
>     x2 is the ending index for row; 
>     y1 is the starting index of column; 
>     y2 is the starting index of column;
> 
> [ 4  9 14 19 24]
> 
> [15 16 17 18 19]


## Some more things to learn and checkout: 

sum();

sum(axis=0); # axis zero is x axis

sum(axis=1); # axis one is y axis 

mean(); 

std(); //standard deviation 

var(); //variance

arange() 

**vectors** 

vectors --> used to apply common operations 

a(0,1,2,3); 

a + 10; 

a(10, 11,12,13); 

``` 
a = np.arange(4); 
a = np.random.randint(100, size=(3,3))
``` 

### Misc: 

* My Python Version: Python 3.9.7
* My VIM Version: VIM - Vi IMproved 8.2
* My Bash Version: GNU Bash, version 5.1.8(1)-release 

**Credits:**

1. [Numpy Tutorial](https://www.dataquest.io/blog/numpy-tutorial-python/)
1. [NumPy Random Array With Range](https://www.studytonight.com/post/creating-random-valuedarrays-in-numpy#:~:text=We%20can%20create%20NumPy%20arrays,based%20on%20the%20uniform%20distribution)
1. [Python Basic](https://kaggle.com/learn/python);



