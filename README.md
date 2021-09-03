Python version is 3.9.5

Postgres DB version is 13.3

Instruction for start local server:
1. Configure environment variables. Set in path new env var as DJANGO_ENV=LOCAL if you want to up project in local machine, DJANGO_ENV=DEVELOP for develop and DJANGO_ENV=PRODUCTION for prod.
2. Install python version 3.9.5.
3. Download repository from github.
4. Create virtual environment in project directory with command python3.9 -m venv <directory name> and active virtual envorinment with comment source <directory name>/bin/activate.
5. Install python packages from requirements.txt file with command pip install -r requirements.txt.
6. After configuring postgres db run command python manage.py migrate to apply migration in db.
7. Create superuser with typing command python manage.py createsuperuser
8. Run local server with typing command python manage.py runserver

Project contain 2 apps: users, quiz

App users response for creating user account and authorization functionality.
users app endpoints:
  1. http://localhost:8000/api/users/ with POST request response for creating new user:
    required fields: email, password, re_password
    optional fields: first_name, last_name
    response example:
        {
          "id": "<your id number>",
          "email": "<your email>"
        }
  
  2. http://localhost:8000/api/token/login/ for login user:
    required fields: email, password
    response example: 
      {
        "auth_token": "<your token>"
      }
    User this token in your Authorization header with prefix Token like Authorization: Token <your token> to authorize your requests
 
quiz app endpoints:
  1. Get quizzes list:
    http://localhost:8000/api/quizzes/
    authorization is optional
    response example:
      [
        {
          "id": "<quiz_id>",
          "title": "<quiz_title>"
        },
        {
          "id": "<quiz_id>",
          "title": "<quiz_title>"
        }
      ]
  
  2. Get quiz detail:
    http://localhost:8000/api/quizzes/<quiz_id>/
    authorization is optional
    response example:
      {
        "id": "<quiz_id>",
        "title": "<quiz_title>",
        "description": "<quiz_description>",
        "start_date": "<quiz_start_date>",
        "end_date": "<quiz_end_date>",
        "questions": [
          {
            "id": "<question_id>",
            "text": "<question_text>",
            "type": "<question_type>", # type field return integer value, posibile values is 0, 1, 2. 0 value means that required single answer for question, 2                                            # requered multiple answers for question, 3 required text as answer
            "answers": [
              {
                "id": "<answer_id>",
                "text": "<answer_text>"
              },
              {
                "id": "<answer_id>",
                "text": "<answer_text>"
              }
            ]
          },
          {
            ...
          }
        ]
      }
  
  3. Submit quiz answer:
    http://localhose:8000/api/answers/ with POST request
    send in cookies field user_id numeric id if user is not authorized else user token
    Example: In request headers add Cookie field like below:
      Cookie: user_id=<numeric_user_id>
    else if user has token:
      Authorization: Token <user_toke>
    request data example:
    {
      "quiz": "<quiz_id>",
      "user_answers": [
        {
          "question": "<question_id>",
          "answers_ids": "<answerd_ids>" # Example: [1, 2]
        },
        {
          "question": "<question_id>",
          "text": "<user answer text>" # If question required text answer
        }
      ]
    }
  
  4. Get user answers list

