fib-rest-sample
===============

Rackspace Screening.

As part of your screening, please provide a sample project for review:
1. The project should provide a RESTful web service.
  a. The web service accepts a number, n, as input and returns the first n Fibonacci numbers, starting from 0. I.e. given n = 5, appropriate output would represent the sequence "0 1 1 2 3".
  b. Given a negative number, it will respond with an appropriate error.
  c. The service should return the values in an XML document.  Create an XSD that can be used to validate the output.

\<fibonacci\>

            <value index="0">0</value>
            
            <value index="1">1</value>
            
            <value index="2">1</value>
            
            <value index="3">2</value>
            
\</fibonacci\>

2. Set this project up on Github.  Include whatever instructions are necessary to build and deploy/run the project, where "deploy/run" means the web service is accepting requests and responding to them as appropriate.
3. While this project is admittedly trivial, approach it as representing a more complex problem that you'll have to put into production and maintain for 5 years.


Directions:

(1). Pull from GitHub.

(2). python restwebservice.py 8080

Requires web.py

Cheers
