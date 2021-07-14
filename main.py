import sys

from subtitle import Subtitle


def main(argv):
    if len(argv) != 2:
        return -1
    try:
        file_path = argv[0]
        output_name_file = argv[1]
        fromManyLinesToOneLine(file_path, output_name_file)
    except FileNotFoundError:
        print("Error: source file inaccessible")
        return -1


def fromManyLinesToOneLine(file_path, output_name_file):
    subtitles = getAllSubtitles(file_path)
    writeSubtitleFile(subtitles, output_name_file)


def writeSubtitleFile(subtitles, output_name_file):
    file = open(output_name_file, 'w')
    for subtitle in subtitles:
        file.write(subtitle.index + '\n')
        file.write(subtitle.time_interval + '\n')
        file.write(subtitle.subtitleText + '\n')
        file.write('\n')
    file.close()


def getAllSubtitles(file_path):
    subtitles = []
    subtitle = Subtitle()
    subtitle_line_index = 0

    with open(file_path, 'r') as subtitlesFile:
        for line in subtitlesFile:
            line = line.strip()

            if not line:
                # add current subtitle and create a new subtitle object
                subtitles.append(subtitle)
                subtitle = Subtitle()
                subtitle_line_index = 0

            elif subtitle_line_index == 0:
                subtitle.addIndex(index=line)
                subtitle_line_index += 1

            elif subtitle_line_index == 1:
                subtitle.addTime(line)
                subtitle_line_index += 1

            else:
                subtitle.addTextFragment(line)
                subtitle_line_index += 1

    return subtitles


main(sys.argv[1:])
