### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

PostgreSQL is a versatile and powerful database management system suitable for a wide range of applications, from small projects to large-scale enterprise deployments.

- What is the difference between SQL and PostgreSQL?

SQL is a language standard for querying and managing relational databases, while PostgreSQL is a specific implementation of an RDBMS that supports SQL and provides additional features and capabilities beyond the standard.

- In `psql`, how do you connect to a database?

psql -U username -d database_name

You replace username with the username that you want to be used and you replace databease_name with the name of your database you want to connect to


- What is the difference between `HAVING` and `WHERE`?

**WHERE** filters individual rows before grouping, while **HAVING** filters groups of rows after grouping has occurred.

- What is the difference between an `INNER` and `OUTER` join?

the main difference between INNER JOIN and OUTER JOIN is that **INNER JOIN** returns only matching rows, while **OUTER JOIN** returns all rows from one or both tables, with optional matching rows from the other table.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

With a **LEFT OUTER JOIN**, all rows from the left table are preserved, and with a **RIGHT OUTER JOIN**, all rows from the right table are preserved.

- What is an ORM? What do they do?

Object Relational mapping or **ORM** systems simplify database interactions and make it easier for developers to build and maintain applications by allowing them to work with database entities using familiar object-oriented paradigms.

- What are some differences between making HTTP requests using AJAX
  and from the server side using a library like `requests`?
  
Both **AJAX** requests and server-side requests serve the purpose of fetching data from external sources over **HTTP**, they operate in different contexts (client-side vs. server-side) and have different considerations in terms of performance, security, complexity, and maintainability.

- What is CSRF? What is the purpose of the CSRF token?

the purpose of a **Cross-Site Request Forgery** or CSRF token is to protect against CSRF attacks by verifying the origin of requests and ensuring that they come from trusted sources within the web application.


- What is the purpose of `form.hidden_tag()`?

A **form.hidden_tag()** is used to include a hidden input field with a CSRF token in Flask forms to protect against CSRF attacks. It's an important security measure for web applications that use forms to handle sensitive operations.