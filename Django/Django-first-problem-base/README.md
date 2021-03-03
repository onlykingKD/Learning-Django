# Django Assignment 1: Views

This assignment is to make you familiar with Django, you will be creating some routes (static and dynamic) and your first views.

## Initial Setup
- Make sure you have python and django installed.
- The project `first_project` and app `first_app` have already been created for you in this repository.
- To run the server use: `python manage.py runserver`.
- After server starts, you can visit `http://localhost:8000/` to see the changes.

## Part 1
The tasks are briefly listed as below:
- The index page (`http://localhost:8000/`) should have a corresponding index view in `first_app/views.py` that returns the following `HttpResponse`:
```
Hello World!
```
- The home page (`http://localhost:8000/home`) should return:
```
Welcome to home page!
```
- The scaler page (`http://localhost:8000/scaler`) should return:
```
Welcome to scaler page!
```

## Part 2

Now, in real applications, you notice that there are some dynamic routes as well, for example everyone has a username and if the URL has a different username, the profile for corresponding user opens.

You need to implement a simple dynamic route, that takes the name of the user and returns `Welcome <name>!` as the response.

For e.g.
`http://localhost:8000/rahul` should return the response as:
```
Welcome rahul!
```

## Part 3
As last part of the assignment, you have to create a simple **about me** page.

`http://localhost:8000/about` should return the following HTML page as a response:

```html
<h1> About Me </h1>
<p> Mention few lines about you... </p>
```

### Note:
- All the above responses are case sensitive, so please make sure you verify them as mentioned above, otherwise test cases will fail.
- Except that, In the paragraph tag, you are free to write about yourself :)