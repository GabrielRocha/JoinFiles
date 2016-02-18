import argparse
import os


def join(path, file):
    with open(file, "w") as opened_new_file:
        for file in os.listdir(path):
            path_file = "{}/{}".format(path, file)
            if not file.startswith(".") and not os.path.isdir(path_file):
                with open(path_file, "r") as opened_file:
                    opened_new_file.writelines(opened_file.readlines())
                    opened_new_file.write("\n")


if __name__ == "__main__":
    app = argparse.ArgumentParser()
    app.add_argument("-p",
                     "--path",
                     required=True,
                     help="Directory Path")
    app.add_argument("-f",
                     "--file",
                     help="New file name",
                     default='join.csv')
    args = vars(app.parse_args())
    join(**args)
