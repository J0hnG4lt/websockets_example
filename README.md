# Django Websockets Example

This Django project showcases the use of the *channels* library to implement the websockets protocol.

#### Web App Requirements

Create a simple Django app that does the following:

1) You can create, edit, and delete users (basic CRUD operations).

2) From the root page, you can see a list of inactive users. 
    If you click one user, you become that user. 
    Let's call him user A.

3) If you open a new browser window, it creates another client session. 
    From the new window, you can see a list of inactive users. 
    If you click one, you become that user. Let's call her user B.

4) From user A's window, you can see user B is active. 
    From user B's window, you can see user A is active.

5) If you toggle a user between active or inactive, 
    the change will be visible to other users.

HINT: try to use websockets to share the active/inactive status.

# Requirements

- [Python](https://www.python.org/) (>= v3.5.2)
- [Django](https://www.djangoproject.com/) (>= v2.0)
- [Redis](https://redis.io/topics/quickstart) (>= v3.0.6)

# Django Requirements

- [Channels](https://channels.readthedocs.io/en/latest/index.html) (>= v2.0)
- [Channels Redis](https://github.com/django/channels_redis) (>= v2.1.1)


# Running Tests

Run the following commands in the root folder:

```sh
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```


