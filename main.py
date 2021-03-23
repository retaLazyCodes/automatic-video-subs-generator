import set_path
import video_converter


def main():
    subdirs = set_path.get_all_subdirs()

    for directory in subdirs:
        video_converter.set_directory(directory)
        video_converter.convert_video_to_audio()


if __name__ == '__main__':
    main()
