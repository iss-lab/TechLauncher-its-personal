# Tech Topic News Article Filter Service

This repository contains the code for the tech topic news article filter service, hosted on heroku.

[Running Service Link](https://itspersonal-tech-newsfilter.herokuapp.com)

# Installation and Deployment Guide

Adapted from a [bottle heroku deployment guide](https://github.com/chucknado/bottle_heroku_tutorial) and the [heroku postgresql documentation](https://devcenter.heroku.com/articles/heroku-postgresql)

1. Download and install [Python version 3](https://www.python.org/downloads/) and [pip3](https://pip.pypa.io/en/latest/installation/).
2. Download and install [git](https://git-scm.com/downloads) and [heroku cli](https://devcenter.heroku.com/articles/heroku-cli).
3. Clone this directory on your local computer by running the following command:
```
git clone $this-repository-github-https-or-ssh-link
```
4. Go to the new directory by running the following command:
```
cd tech-topic-service
```

Alternatively, open the directory using your computer's file explorer and open a terminal there.

5. Install the required packages by running the following command (make sure the `requirements.txt` file exists in the directory):
```
pip install -r requirements.txt
```
6. To test the app locally, run the following command:
```
python3 app.py
```
Navigate to `http://localhost:8080/tech` and you should see several news articles listed alongside their information in the screen in a `JSON` format.

When you have finished testing it locally, press `ctrl + c` in the terminal to stop the app.

7. Create a [heroku account](https://signup.heroku.com/).
8. Login to your `heroku` account in the terminal using the following command:
```
heroku login
```
9. Create a new `heroku` app for the deployment by running the following command **(it cannot be the same name as an existing heroku app)**:
```
heroku create $app-name
```
10. Add `heroku` as a `git remote` link by running the following command:
```
heroku git:remote -a $app-name
```
Verify that the new `remote heroku` link is added by running the following command:
```
git remote -v
```
11. The following is an explanation about the remaining files:

    a. `Procfile` contains the instruction to be run in `heroku`.

    b. `runtime.txt` contains the Python version that is used in `heroku`.
    
    c. `requirements.txt` contains the required packages that must be installed in `heroku`.
    
    d. `training/model-best` contains the `spacy` NLP model that has been trained in the model repository. Replace the content with a new model to use that new model in the service.
12. Add a `postgresql addon` to `heroku` by running the following command:
```
heroku addons:create heroku-postgresql:hobby-dev
```
Check that the `addon` has been added correctly by running the following command:
```
heroku addons
```
If required, remove the `addon` by running the following command:
```
heroku addons:destroy $postgresql-name
```

13. Check the `postgresql` database info by running the following command (including the `postgresql` name which is `Add-on`):
```
heroku pg:info
```
14. Download and install [postgresql](https://devcenter.heroku.com/articles/heroku-postgresql#set-up-postgres-on-windows) and make sure it is added to the `PATH` environment variable if using windows.

15. Open the `postgresql` database by running the following command:
```
heroku pg:psql
```

16. The following is the list of relevant `psql` commands that may be helpful:

    a. Check what tables exist in the database by running the following command:
    ```
    \dt;
    ```
    b. Create a new `tech` table by running the following command:
    ```
    CREATE TABLE tech (
        title VARCHAR (200) PRIMARY KEY,
        relevant BOOL
    );
    ```
    c. Check the details of the `tech` table by running the following command:
    ```
    \d tech;
    ```
    d. Get entries from the `tech` table by running the following command:
    ```
    SELECT * FROM tech;
    ```
    You must manually copy the entries to a new / existing `JSON` file that contains the dataset collected from running the training command.

    e. Delete all entries from the `tech` table by running the following command:
    ```
    DELETE FROM tech;
    ```
    f. Delete the `tech` table by running the following command:
    ```
    DELETE TABLE tech;
    ```

17. (One time) Set the `APP_LOCATION` variable by running the following command:
```
heroku config:set APP_LOCATION=heroku
```

18. Deploy the app to `heroku` by running the following command:
```
git push heroku master
```
19. Open the deployment by running the following command:
```
heroku open
```
20. To update the deployment, commit the changes to the repository using `git` and repeat step 18 and 19.