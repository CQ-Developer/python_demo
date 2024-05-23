from typing import List


class AnonymousSurvey:
    """收集匿名调查问卷的答案"""

    def __init__(self, question: str):
        """存储一个问题并为存储答案做准备"""
        self.question: str = question
        self.responses: List[str] = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self, new_question: str):
        """存储单份调查问卷"""
        self.responses.append(new_question)

    def show_results(self):
        """显示收集到的所有答案"""
        print("Survey Question:")
        for resp in self.responses:
            print(f"- {resp}")
