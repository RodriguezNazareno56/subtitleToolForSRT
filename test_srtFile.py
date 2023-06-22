import os
import unittest
import tempfile
from io import StringIO
import logging

from srtFile import SrtFile


def create_srt_test_file_one_paragraph():
    temp_file = tempfile.NamedTemporaryFile(suffix=".srt", delete=False)
    content = """7
    00:03:38,993 --> 00:03:49,086
    My mama always said, “life was like a box of chocolates
    You never know what you’re gonna get”
    """
    temp_file.write(content.encode())
    temp_file.close()
    return temp_file


def create_srt_test_file_two_paragraph():
    temp_file = tempfile.NamedTemporaryFile(suffix=".srt", delete=False)
    content = """5
    00:03:21,559 --> 00:03:31,819
    My name's Forrest. Forrest Gump.
    Do you want a chocolate?
    
    6
    00:03:29,776 --> 00:03:37,825
    Do you want a chocolate?
    I could eat about a million and a half of these.
    """
    temp_file.write(content.encode())
    temp_file.close()
    return temp_file


class TestSrtFile(unittest.TestCase):

    def test_bad_path_no_existing_file_log_error_message(self):
        nonexistent_file_path = "path/a/b/nonexistent_file.srt"

        # Captura el registro de logs en un objeto StringIO
        log_stream = StringIO()
        logger = logging.getLogger()  # Obtiene el logger raíz
        logger.setLevel(logging.ERROR)
        logger.addHandler(logging.StreamHandler(log_stream))

        srt_file = SrtFile(nonexistent_file_path)
        self.assertIn(f"Could not found file: {nonexistent_file_path}", log_stream.getvalue())

    def test_get_subtitles_file_with_only_one_paragraph(self):
        file = create_srt_test_file_one_paragraph()
        srt_file = SrtFile(file.name)
        subtitles = srt_file.get_subtitles_list()
        self.assertEqual(subtitles[0].subtitleText,
                         "My mama always said, “life was like a box of chocolates You never know what you’re gonna get”")
        os.remove(file.name)

    def test_get_subtitles_file_with_only_two_paragraph(self):
        file = create_srt_test_file_two_paragraph()
        srt_file = SrtFile(file.name)
        subtitles = srt_file.get_subtitles_list()
        self.assertEqual(subtitles[0].subtitleText,
                         "My name's Forrest. Forrest Gump. Do you want a chocolate?")
        self.assertEqual(subtitles[1].subtitleText,
                         "Do you want a chocolate? I could eat about a million and a half of these.")
        os.remove(file.name)

    def test_time_interval_correct_extract(self):
        file = create_srt_test_file_one_paragraph()
        srt_file = SrtFile(file.name)
        subtitles = srt_file.get_subtitles_list()
        self.assertEqual("00:03:38,993 --> 00:03:49,086", subtitles[0].time_interval)
        os.remove(file.name)

    def test_time_interval_correct_index(self):
        file = create_srt_test_file_one_paragraph()
        srt_file = SrtFile(file.name)
        subtitles = srt_file.get_subtitles_list()
        self.assertEqual("7", subtitles[0].index)
        os.remove(file.name)
