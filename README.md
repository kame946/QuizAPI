# My Quiz API

## Description
This is a Django application that provides an API for quizzes. It includes features such as quiz creation, retrieving active quizzes, and retrieving quiz results.

## Installation
1. Clone the repository: `git clone <repository-url>`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Configure the database settings in `settings.py`
4. Run django-cron job: `python manage.py runcrons`
5. Start the Django development server: `python manage.py runserver`

## API Endpoints

### Quiz List/Create
- URL: `/quizzes/`
- Method: POST
- Description: Create a new quiz
- Parameters:
    - question (string): The quiz question
    - options (array): Array of options for the quiz
    - right_answer (integer): Index of the correct answer
    - start_date (datetime): Start date of the quiz
    - end_date (datetime): End date of the quiz

### Active Quiz
- URL: `/quizzes/active/`
- Method: GET
- Description: Retrieve the active quiz
- Response: The details of the active quiz

### Quiz Result
- URL: `/quizzes/<quiz-id>/result/`
- Method: GET
- Description: Retrieve the result of a finished quiz
- Parameters:
    - quiz-id (integer): ID of the quiz
- Response: The right answer of the quiz
- 
## Contributors
- Harsh Kumar(@kame946)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
