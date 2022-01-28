import os
import re
import glob
from editfrontmatter import EditFrontMatter


def main():

    INPUT_PATH = "Real/"
    OUTPUT_PATH = "out/"

    for filename in glob.glob(os.path.join(INPUT_PATH, "*.md")):
        with open(os.path.join(os.getcwd(), filename), "r") as f:
            fileCommands(OUTPUT_PATH, filename)


def canPublish_func(val):
    print(val)
    return True


def fileCommands(OUTPUT_PATH, filename):
    # # initialize `template_str` with template file content
    template_str = "".join(open(os.path.abspath("template1.j2"), "r").readlines())

    # instantiate the processor
    proc = EditFrontMatter(file_path=filename, template_str=template_str)

    # set fields to delete from yaml
    proc.keys_toDelete = [
        "description",
        "source",
        "created",
        "modified",
        "up",
        "tags",
        "down",
        "type",
    ]

    # add a filter and callback function
    proc.add_JinjaFilter("context", canPublish_func)

    # print filename
    titleMD = filename.split("/")[-1]
    title = titleMD.split(".")[0]
    titleLowerMD = titleMD.lower()
    titleLower = titleLowerMD.split(".")[0]

    # if titleLower contains "," then split
    parent = titleLower.split(",")[0]

    # populate variables and run processor
    proc.run(
        {
            "title": title.replace("'", " "),
            "domain": [""],
            "parent": parent,
            "aliases": titleLower,
        }
    )

    # delete everything between and including every "[[" and the next "|"
    beforeRegex = proc.dumpFileData()
    new = re.sub(r"\[\[.*?\|", "", beforeRegex).replace("]]", "")

    # create markdown file and fill with proc.dumpFileData()
    with open(os.path.abspath(OUTPUT_PATH + titleLowerMD), "w") as f:
        f.write(new)


if __name__ == "__main__":
    main()
