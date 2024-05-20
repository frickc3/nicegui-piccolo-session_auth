# Example NiceGUI Project with Piccolo ORM with modified session-auth.

## Example NiceGUI Project using Piccolo as the ORM and Piccolo-api for session authentication.

1.  Clone this repository to your local device.  
    **git clone https://github.com/frickc3/nicegui-piccolo-session_auth.git**

2.  Change into that directory.  
    **cd nicegui-piccolo-session_auth**

3.  Create a virtual environment.  
    **python -m venv .venv**

4.  Activate that environment.  
    **.venv\scripts\activate**

5.  Install the required packages.  
    **pip install -r requirements.txt**

6.  Run all the migrations (also creates the SQLite database).  
    ```
    piccolo migrations forward user  
    piccolo migrations forward session_auth  
    ```

7.  Create the new administrator user.  
    ```
    piccolo user create

        Enter username ():
        piccolo
        Enter email:
        piccolo@example.com
        Enter password:
        piccolo123
        Confirm password:
        piccolo123
        Admin user? Enter y or n:
        y
        Superuser? Enter y or n:
        y
        Active? Enter y or n:
        y
        Created User 1
    ```

8. Startup the dev web server.  
    **fastapi dev --port=8080**

9. Goto **http://localhost:8080**  

10. The Piccolo Admin application is available at **http://localhost:8080/admin/**  
