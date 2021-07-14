import sys

from subtitle import Subtitle


def main(argv):
    if len(argv) != 1:
        return -1
    try:
        print('hola')
        file_path = argv[0]
        fromManyLinesToOneLine(file_path)
    except FileNotFoundError:
        print("Error: archivo fuente inaccesible")
        return -1


def fromManyLinesToOneLine(file_path):
    subtitles = getAllSubtitles(file_path)
    writeSubtitleFile(subtitles)


def writeSubtitleFile(subtitles):
    file = open('subtitle.txt', 'w')
    for subtitle in subtitles:
        file.write(subtitle.index)
        file.write(subtitle.time_interval)
        file.write(subtitle.subtitleText)
        file.write('')


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
