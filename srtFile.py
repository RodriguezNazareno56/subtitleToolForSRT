import logging

from subtitleLine import SubtitleLine
from translateService import TranslateService


class SrtFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.subtitles = self.__extract_subtitles_paragraph_to_line()

    def __extract_subtitles_paragraph_to_line(self):
        """
        Extract all subtitles from srt file, converting each paragraph to one line and storing it in a SubtitleLine
        Object with its respective index and time interval.

        from subtitle.srt format:

        '''

        7

        00:03:38,993 --> 00:03:49,086

        My mama always said, “life was like a box of chocolates

        You never know what you’re gonna get”

        '''

        to SubtitleLine object:

        SubtitleLine.index = 7

        SubtitleLine.time_interval = 00:03:38,993 --> 00:03:49,086

        SubtitleLine.subtitleText = My mama always said, “life was like a box of chocolates You never know what you’re gonna get”

        :rtype: list[SubtitleLine]
        """
        subtitles = []
        subtitle_line = SubtitleLine()

        subtitle_paragraph_index = 0

        try:
            with open(self.file_path, 'r') as subtitlesFile:
                for line in subtitlesFile:
                    line = line.strip()

                    if not line:  # empty line between subtitles
                        # add current subtitle and create a new subtitle object
                        subtitles.append(subtitle_line)
                        subtitle_line = SubtitleLine()
                        subtitle_paragraph_index = 0

                    elif subtitle_paragraph_index == 0:  # srt index
                        subtitle_line.set_index(index=line)
                        subtitle_paragraph_index += 1

                    elif subtitle_paragraph_index == 1:  # interval time
                        subtitle_line.set_time(line)
                        subtitle_paragraph_index += 1

                    else:
                        subtitle_line.add_text_fragment(line)
                        subtitle_paragraph_index += 1
        except FileNotFoundError:
            logging.error(f"Could not found file: {self.file_path}")

        return subtitles

    def get_subtitles_list(self):
        return self.subtitles

    def write_subtitle_srt_file(self, output_name_file):
        file = open(output_name_file, 'w')
        for subtitle in self.subtitles:
            file.write(subtitle.index + '\n')
            file.write(subtitle.time_interval + '\n')
            file.write(subtitle.subtitleText + '\n')
            file.write('\n')
        file.close()
        return file

    def write_subtitle_srt_file_with_translate(self, output_name_file):
        translate_service = TranslateService(source="en", target="es")
        file = open(output_name_file, 'w')
        for subtitle in self.subtitles:
            file.write(subtitle.index + '\n')
            file.write(subtitle.time_interval + '\n')
            file.write(subtitle.subtitleText + '\n')
            file.write("<font color=\"#ffff7f\">" + translate_service.translate(subtitle.subtitleText) + "</font>\n")
            file.write('\n')
        file.close()
        return file
