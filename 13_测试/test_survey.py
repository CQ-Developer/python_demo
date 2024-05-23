import unittest
from typing import List

from survey import AnonymousSurvey


class AnonymousSurveyTest(unittest.TestCase):
    """test AnonymousSurvey"""

    def setUp(self):
        """
        初始化单元测试
        注意: 会在每个单元测试方法执行前执行
        类比于 Junit 的 @BeforeEach
        """
        question: str = "What Language did you first learn to speak?"
        self.my_survey: AnonymousSurvey = AnonymousSurvey(question)
        self.responses: List[str] = ["English", "Spanish", "Mandarin"]

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_response(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == "__main__":
    unittest.main()
