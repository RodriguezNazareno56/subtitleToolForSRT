import sys

from srtFile import SrtFile


def main(argv):
    if len(argv) != 2:
        return -1
    try:
        file_path = argv[0]
        output_name_file = argv[1]
        srt_file = SrtFile(file_path)
        srt_file.write_subtitle_srt_file_with_translate(output_name_file)
    except FileNotFoundError:
        print("Error: source file inaccessible")
        return -1


main(sys.argv[1:])
