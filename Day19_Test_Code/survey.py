# /bin/etc/env Python
# -*- coding: utf-8 -*-

class AnonymousSurvey():
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self, new_responses):
        self.responses.append(new_responses)

    def show_results(self):
        print("Survey results:")
        for response in responses:
            print('- ' + response)
