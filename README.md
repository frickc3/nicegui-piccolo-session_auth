# Example NiceGUI Project with Piccolo ORM with modified session-auth.

## Example NiceGUI Project using Piccolo as the ORM and Piccolo-api for session authentication.

1.  Clone this repository to your local device.
    git clone https://github.com/frickc3/nicegui-piccolo-session_auth.git

2.  cd nicegui-piccolo-session_auth

3.  Create a virtual environment.
    python -m venv .venv

4.  Activate that environment.
    .venv\scripts\activate

5.  Install the required packages.
    pip install -r requirements.txt

6.  Copy .env-example to .env and make modifications.

7.  Create the database.

7.  Create migrations for our tables.
    piccolo migrations create app --auto

8.  Run all the migrations.
    piccolo migrations forward all
    piccolo migrations forward user
    piccolo migrations forward session_auth

9.  Create the new administrator user.
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

10. Startup the web server.
    python main.py

11. Goto http://localhost:8080

12. To view the defined tables use http://localhost:8080/admin/.

