[![Build Status](https://travis-ci.org/bl4ck4ndbr0wn/recipe-api.svg?branch=master)](https://travis-ci.org/bl4ck4ndbr0wn/recipe-api) [![Maintainability](https://api.codeclimate.com/v1/badges/11b390b6347be061c407/maintainability)](https://codeclimate.com/github/bl4ck4ndbr0wn/recipe-api/maintainability)

Recipe APi - A Social platform for the creative at heart with there recipe management.
=======

## Running the app.
Authors Haven app can be run by:
### STEP 1:
    Git clone this repository: `git clone https://github.com/bl4ck4ndbr0wn/recipe-api`

### STEP 2: 
    Change your working directory to the app's root. `cd recipe-api`

### STEP 3:
    Create a virtual environment and activate it.
    Install all the requirements by running `pip install -r requirements.txt`
    Create an environment file with environment variables in the following format:
  
      SECRET_KEY=supersecretkey
      DEBUG=True
      DB_NAME=yourdbname
      DB_USER=yourname
      DB_PASSWORD=yourstrongpassword
      DB_HOST=127.0.0.1
      DB_PORT=5432

### STEP 4:
    Run the app according to the environment you need:

   #### Development environment:
    `python manage.py makemigrations`

    `python manage.py migrate`

    `python manage.py runserver`

   #### Testing environment:
    `python manage.py test`

   #### Production environment:
     The run the app on a production environment:
     Use Postman to acccess the app by using this url as your domain:
     `https://my-recipe-api.herokuapp.com`

     Input appropriate endpoint urls, enjoy.

With Love.
