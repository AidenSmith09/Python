# /bin/etc/env Python
# -*- coding: utf-8 -*-

from survey import AnonymousSurvey

question = "What languafe did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time quit.\n")
while True:
    response = input("Langeuage:")
    if response == 'q':
        break
    my_survey.store_response(response)

print("\nThank you to everyone who participated in the survey!")
my_survey.show_question()
