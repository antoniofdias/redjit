<h1 align="center">
    <img alt="redjit" title="Graphic design is my passion" src="redjit/.github/logo.png" width="250px" />
</h1>

<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/badge/languages-3-informational">
  
  <a href="https://github.com/antoniofdias/redjit/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/badge/last%20commit-december%202020-inactive">
  </a>

  <a href="https://github.com/antoniofdias/redjit/blob/master/LICENSE">
    <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">
  </a>
</p>

<p align="center">
  <a href="#rocket-built-with">Built with</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-about-the-project">About the project</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-how-to-contribute">How to contribute</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#memo-license">License</a>
</p>

<br>

<p align="center">
  <img alt="Frontend" src=".github/redjit.png" width="100%">
</p>

## Building

It is best to use the python `virtualenv` tool to build locally:

```sh
$ virtualenv env -p python3.8
$ source env/bin/activate
$ pip3 install -r requirements.txt
$ cd redjit
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```

Then visit `http://127.0.0.1:8000/` to view the app.