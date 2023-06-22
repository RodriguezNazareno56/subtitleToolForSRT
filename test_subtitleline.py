import unittest

from subtitleLine import SubtitleLine


class TestSubtitleLine(unittest.TestCase):

    def test_set_index(self):
        subtitle_line_text = SubtitleLine()
        index = 1
        subtitle_line_text.set_index(index)
        self.assertEqual(subtitle_line_text.index, index)

    def test_set_time(self):
        subtitle_line_text = SubtitleLine()
        time = "00:01:26,671 --> 00:01:28,339"
        subtitle_line_text.set_time(time)
        self.assertEqual(subtitle_line_text.time_interval, time)

    def test_add_one_text_fragment(self):
        subtitle_line_text = SubtitleLine()
        text = "My mama always said, “life was like a box of chocolates"
        subtitle_line_text.add_text_fragment(text)
        self.assertEqual(subtitle_line_text.subtitleText, text)

    def test_add_two_text_fragment(self):
        subtitle_line_text = SubtitleLine()
        first_text = "My mama always said, “life was like a box of chocolates"
        second_text = "You never know what you’re gonna get”"

        subtitle_line_text.add_text_fragment(first_text)
        subtitle_line_text.add_text_fragment(second_text)
        self.assertEqual(subtitle_line_text.subtitleText, first_text + ' ' + second_text)