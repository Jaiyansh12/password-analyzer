*PASSWORD ANALYZER*

This repository hosts a Password Strength Analyzer, a utility designed to provide users with immediate and meaningful feedback on the strength of their passwords. It has a strong system for calculating the true security level of your password and assign a strength score, helping developers and users encourage the use of strong, unique passwords.
This Python-based command-line tool assesses the security level of a given password by evaluating factors like length, character diversity.

PROJECT OVERVIEW

Welcome to the Password Strength Analyzer ! This project is a simple command-line tool developed in Python to evaluate the security level of a password.
In today's digital world, strong passwords are the first line of defense against security breaches. This analyzer helps users understand why their password is weak or strong by scoring it based on some criterias and providing specific feedbacks for improvement. It's a great demonstration of basic security logic and programming fundamentals.
Our current password rules are like a simple checklist that says, "You must be 8 characters long and have a capital letter," which is easy for hackers to get around (like the weak password "school name 12"). The smarter approach uses Artificial Intelligence (AI), which acts like a highly trained expert. This expert doesn't just check the rules; it analyzes millions of cracked passwords to learn what really makes one strong, like the overall randomness and patterns. It then gives your password a real-world risk score—predicting how many years it would actually take a supercomputer to guess it—moving us from a basic, easily fooled security system to a dynamic defense that can spot and block even the newest, trickiest attacks.


FEATURES AND LOGICS

The analyzer scores a password out of a total of 100 points based on the following criteria:

* Length Bonus (25 points) -> Awarded if the password meets or exceeds the minimum length (10 characters). Partial points are given for lengths greater than 6 and 8. 

* Uppercase Letters (15 points) -> Awarded for the inclusion of at least one uppercase letter (A-Z). 

* Lowercase Letters (15 points) -> Awarded for the inclusion of at least one lowercase letter (a-z). 

* Digits (20 points) -> Awarded for the inclusion of at least one digit (0-9). 

* Special Characters (25 points) -> Awarded for the inclusion of at least one symbol/punctuation mark (e.g., !@#$%^&*). 

RATING SYSTEMS

The final score is translated into an easy-to-understand rating:

* 90 - 100 -> Strong Password

* 75 - 89 -> Moderate Strength 

* 50 - 74 -> Weak, needs more strength 

* 25 - 49 -> Very weak, need much more improvement 

* < 25 -> Not Valid, Retry 

HOW TO RUN ANALYZER

You only need **Python 3.x** installed on your computer.

** Step 1: Download the Code 

Clone the repository or download the source code file (`analyzer.py` or similar) to your local machine.

```bash
# Example: If you host it on GitHub
# git clone https://github.com/YourUsername/Password-Analyzer-Project.git
# cd Password-Analyzer-Project
```

** Step 2: Execute the Script **

Open your terminal or command prompt, navigate to the directory where you saved the file, and run the main script:
    
```bash
python your_script_name.py
```

** Step 3: Enter Your Password **

The program will prompt you to enter a password for analysis:

```
### Password Strength Analyzer ###
enter the password :
```

EXAMPLE OUTPUT

If you enter a password like `hello`:

```
### password analysis ###
analyzed password : hello
final score of the inputted password : 30 / 100
rating of the inputted password : very weak, need much more improvement

### suggestions for improvement ###
--> add some upper case words
--> add some digits
--> add some characters
--> length of password is too small, suggested length = 10 
```

PROJECT STRUCTURE

1.  `analyze(password)`: The core function that iterates through the password, checks for character types (upper, lower, digits, special characters), calculates the score based on the `weightage` dictionary, and generates detailed `feedback`.
2.  `rate(score)`: Translates the final numeric score into a readable string rating using defined `if/elif` logic.
3.  `result(password, score, feedback)`: Displays the final, formatted output to the user, including the score, rating, and all suggestions.
4.  `main()`: The entry point that takes user input and plans the calls to `analyze` and `result`.



