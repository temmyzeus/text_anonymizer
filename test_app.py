import unittest
from app import get_entity_positions


class TestApp(unittest.TestCase):
    def test_get_entity_positions(self):
        text_1 = ('The Taliban’s violent crackdown on protests against their hardline'
                ' rule has already led to four documented deaths, according to a UN'
                ' human rights official who said the group had used live ammunition,'
                ' whips and batons to break up demonstrations.Ravina Shamdasani, the'
                ' UN’s rights spokesperson, told a briefing in Geneva that it had also'
                ' received reports of house-to-house searches for those who participated in the protests.')

        text_2 = ('The protests against the Taliban’s return to power, many of which'
                ' have been led by women fearful of their status under the Islamist'
                ' group, have been the target of violence in a number of locations'
                ' and were formally banned this week without prior authorisation by the Taliban’s new interior ministry.')

        text_3 = ('Describing the crackdown on dissent as “severe”, Shamdasani also'
                ' described how journalists covering the demonstrations had faced'
                ' intimidation, including in one case the threat of “beheading”,'
                ' apparently a reference to an incident in which two Afghan journalists'
                ' were detained, flogged and threatened earlier this week.')

        # positions starts counting from 0
        # for text_1
        self.assertListEqual(
            list1=get_entity_positions(text_1),
            list2=[
                ('Taliban', 4, 10),
                ('four', 91, 94),
                ('UN', 130, 131),
                ('Ravina Shamdasani', 244, 260),
                ('UN', 267, 268),
                ('Geneva', 312, 317),
            ]
        )

        # for text_2
        self.assertListEqual(
            list1=get_entity_positions(text_2),
            list2=[
                ('Taliban', 25, 31),
                ('Islamist', 123, 130),
                ('this week', 222, 230),
                ('Taliban', 267, 273),
            ]
        )

        # for text_3
        self.assertListEqual(
            list1=get_entity_positions(text_3),
            list2=[
                ('Shamdasani', 49, 58),
                ('one', 156, 158),
                ('two', 239, 241),
                ('Afghan', 243, 248),
                ('earlier this week', 300, 316),
            ]
        )

test_app = TestApp()
test_app.test_get_entity_positions()
