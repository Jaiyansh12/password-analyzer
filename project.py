import string

# minimum length set for giving bonus score
min_length = 10

# score weightage
weightage = {"length_bonus":25, "upper":15, "lower":15, "digits":20, "characters":25}

# ading punctuations/symbols using string library 
characters = string.punctuation

#create a function for analysing the strength of the password
def analyze(password):
    score = 0
    feedback = []

    found = {                 # initially setting false value for the keys of weightage 
             "upper":False,
             "lower":False,
             "digits":False,
             "characters":False
             }
    
    for char in password:              # searching for the eligibility to be a strong password
        if char.isupper():             # if found then set the keys of weightage as true
            found["upper"] = True           
        elif char.islower():
            found["lower"] = True
        elif char.isdigit():
            found["digits"] = True
        elif char in characters:
            found["characters"] = True
        
    for char_type, is_present in found.items():   # using for loop to search the eligibility
        if is_present:                            # items in the 'found' list and calculating score
            score += weightage.get(char_type, 0)
        else:
            if char_type == "upper":                       # if the eligibility items are not found 
                feedback.append("add some upper case words") # then add those in the feedback list
            elif char_type == "lower":
                feedback.append("add some lower case words")
            elif char_type == "digits":
                feedback.append("add some digits")
            elif char_type == "characters":
                feedback.append("add some characters")

    length = len(password)           # counting length of the password

    if length >=min_length:
        score += weightage["length_bonus"]     # giving length bonus and feedbacks
    elif length > 8:
        score += weightage["length_bonus"] - 5
        feedback.append(f"length is good, but suggested for more than {min_length}")
    elif length > 6:
        score += weightage["length_bonus"] - 10
        feedback.append(f"length is okay, but suggested for more than {min_length}")
    else :
        feedback.append(f"length of password is too small, suggested length = {min_length} ")

    return score, feedback

# create a function for counting the resultant rating of the password using if else statements
def rate(score):
    if score >= 90:
        return "strong password"
    elif score >=75:
        return "moderate strength"
    elif score >=50:
        return "weak, needs more strength"
    elif score >=25:
        return "very weak, need much more improvement"
    else:
        return "not valid, retry"

# create a function to display the final results
def result(password, score, feedback):
    rating_string = rate(score)
    print("\n\n### password analysis ###")
    print(f"analyzed password : {password}")
    print(f"final score of the inputted password : {score} / {sum(weightage.values())}")
    print(f"rating of the inputted password : {rating_string}")

    if feedback:
        print("\n### suggestions for improvement ###")
        for suggestion in feedback:
            print(f"--> {suggestion}")
    else:
         print("\nFeedback : great work your password meets all of the criterias")

# create a function to take password frousaer and display the results ( main program)
def main():
    print("### Password Strength Analyzer ###")
    password = input("enter the password :")

    if not password:                            # if no passwrod enter exit the function
        print("password cannot be empty")
        return
    
    final_score, suggestions = analyze(password)
    result(password, final_score, suggestions)

if __name__ == "__main__":
    main()

