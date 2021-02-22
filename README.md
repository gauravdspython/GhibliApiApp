# GhibliApi Test App
Python app which fetch a list of movies with people appeared in those movies from Ghibliapi
## STEPS TO RUN THE PROGRAM  ##

### Pre-requisite
The only pre-requisite is that python 3.7 or higher should be installed on your system

### Steps

1. Open Terminal window and point it to the ```GhibliApiApp``` directory in the repo.
2. Run the below command in the IDE terminal or the windows terminal
   ```
   pip install -r requirements.txt
   ```
3. In the terminal window, run:
    ```
   python app/app.py
   ```

If the program runs successfully, you would see something like this in the terminal window:
    
```
    * Serving Flask app "app" (lazy loading)
    * Environment: production
       WARNING: This is a development server. Do not use it in a production deployment.
       Use a production WSGI server instead.
     * Debug mode: on
     * Restarting with stat
     * Debugger is active!
     * Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)
```

This means that program is running. Now, open your browser and hit the below URL:
    
```
http://localhost:8000/movies/
```

## Unit Tests

For unit tests, I have used the pytest framework. In the ```tests``` directory, you would see the following things:

- ```conftest.py```

    This file contains the basic configurations to run the unit tests


- ```test_movies.py``` and ```test_people.py```

    These are two files contain the test cases.

> NOTE: For the sake of POC-only, and lack of time, I have kept test data for the unit tests, in the same file as the test cases themselves. One of the alternatives to this could be to keep the test data in a separatte ```data.py``` file

To run the unit tests, run this command in the already-opened terminal window:
```
pytest
```

## Thank you!
Thank you for the opportunity. If there are any questions regarding the assignment, feel free to mail me and I would be glad to provide the resolution


Thanks and Regards
