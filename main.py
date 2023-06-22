import sys

from srtFile import SrtFile


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
    srt_file = SrtFile(file_path)
    srt_file.write_subtitle_srt_file(output_name_file)



main(sys.argv[1:])
