# GhibliApi Test App
Python app which fetch a list of movies with people appeared in those movies from Ghibliapi
## STEPS TO RUN THE PROGRAM  ##

  --- TO RUN ON YOUR LOCAL MACHINE ---
    [The only PRE-REQUISITE is that python should be installed on your system]
    

    1. Open Terminal window and point it to the "GhibliApiApp" directory in the repo.
    2. Run the below command in the IDE terminal or the windows terminal
        pip3 install -r requirements.txt
    3. in the terminal window, type
        python3 app.py
        
    Now the program would run and you would see something like this in your terminal window
    * Serving Flask app "app" (lazy loading)
     * Environment: production
       WARNING: This is a development server. Do not use it in a production deployment.
       Use a production WSGI server instead.
     * Debug mode: on
     * Restarting with stat
     * Debugger is active!
     * Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)


    This means that program is running. Now, open your browser and hit any of the below URLS:
    http://localhost:8000/movies/
