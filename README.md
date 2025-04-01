# Mental Health Charbot

A simple Flask-based charbot that uses fuzzy string matching to provide responses based on predefined mental health-related data.

## Features
- Uses **Flask** for API handling
- Implements **Flask-CORS** for cross-origin requests
- Uses **FuzzyWuzzy** for text matching
- Loads charbot responses from a JSON file
- Returns relevant responses based on user input

## Installation

### Prerequisites
Make sure you have Python installed (preferably Python 3.7+). You can check your version with:
```sh
python --version
```

### Install Required Dependencies
Run the following command to install necessary packages:
```sh
pip install Flask Flask-CORS fuzzywuzzy python-Levenshtein
```

## Running the Application

1. Clone this repository:
```sh
git clone https://github.com/yourusername/mental-health-charbot.git
cd mental-health-charbot
```

2. Run the charbot API:
```sh
python app.py
```

The application will start on `http://127.0.0.1:5000/`

## Usage
Send a POST request to `/chat` with a JSON payload:
```json
{
  "message": "I feel anxious"
}
```
Response:
```json
{
  "response": "It's okay to feel this way. Try some deep breathing exercises."
}
```

## Project Structure
```
mental-health-charbot/
│── model/
│   └── a.json  # JSON file with charbot responses
│── app.py      # Main Flask application
│── README.md   # Documentation
```

## Contributing
Feel free to fork this repository and contribute to the project by submitting a pull request.

## License
This project is licensed under the MIT License.
