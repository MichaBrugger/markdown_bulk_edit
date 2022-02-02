import os
import re
import glob
from editfrontmatter import EditFrontMatter


def main():

    INPUT_PATH = "../../../Fork my Brain/Brain/"
    OUTPUT_PATH = "../../../digital/brain/"

    for filename in glob.glob(os.path.join(INPUT_PATH, "*.md")):
        with open(os.path.join(os.getcwd(), filename), "r") as f:
            fileCommands(OUTPUT_PATH, filename)

# specific function that takes the type property (list/string) and returns some stuff specific to my vault
def getType(field):
  if type(field) == list:
    field = field[0]
  
  # return based on string
  match field:
    case 'People':
      return "'person'"
    case 'Company':
      return "'company'"
    case 'Software, Applications':
      return "'application'"
    # base case
    case _:
      return ['daily', 'thought']
    
    

def fileCommands(OUTPUT_PATH, filename):
    # tbh this is somewhat of a remnant of a time I used jinja templates for the frontmatter
    # the templates are currently read in, but nothing is really done with it, so best just leave it
    template_str = "".join(open(os.path.abspath("template1.j2"), "r").readlines())

    # instantiate the processor
    proc = EditFrontMatter(file_path=filename, template_str=template_str)

    # turns the frontmatter into a string
    beforeRegex = proc.dumpFileData()
    
    # from here onward it's basically up to you what you want to do with your stuff
    # ---------------------------------------------------------------------------------
    
    # remove yaml fields between `---`
    beforeRegex = re.sub(r"---\n(.*?)\n---", "", beforeRegex, flags=re.DOTALL)

    # find all lines that contain the string "source::" excluding the final "]"
    # once again this was specific for my vault
    source = re.findall(r"source::(.*?)\]", beforeRegex)
    if source == []:
        source = ""

    # print filename
    title = filename.split("/")[-1].split(".")[0]
    titleLower = title.lower()
    titleNoCommaTitleCase = title.replace(",", "").title()

    # tags
    if proc.fmatter.get("tags") == None:
        tags = ""
    else:
        tags = proc.fmatter.get("tags")

    # if titleLower contains "," then split
    if titleLower.find(",") != -1:
        parent = titleLower.split(",")[0]
    elif proc.fmatter.get("up") != None:
        parent = proc.fmatter.get("up")[0].lower()
    else:  # if no parent, then use title
        parent = ""

    # replace the title
    removeTitle = re.sub(r"\s# .*", "", beforeRegex)

    # replace the brackets (also looking at | because of aliases)
    replaceBrackets = (
        re.sub(r"\[\[.*?\|", "", removeTitle).replace("]]", "").replace("[[", "")
    )
    replaceBrackets = re.sub(r"\[\^.*?\]", "", replaceBrackets)

    # if line starts with ": [source::" then remove it
    replaceBrackets = re.sub(r": \[source::.*?\]", "", replaceBrackets)

   
    myType = getType(proc.fmatter.get("up"))
      
      
    def strList(list):
        # if list is string then return string
        if type(list) == str:
            if list == "":
                return "\n"
            else:
                return "['" + list + "']\n"
        string = ""
        for item in list:
            string += "\n- '" + item + "'"
        return string + "\n"

    # finally creating the yaml string from all those variables created above
    yaml = (
        "---\n"
        + "tags: "
        + strList(tags)
        + "type: "
        + myType + "\n"
        + "title: '"
        + titleNoCommaTitleCase
        + "'\n"
        + "domain: \n"
        + "parent: "
        + strList(parent)
        + "aliases: "
        + strList([title])
        + "children: \n"
        + "context: \n"
        + "source: "
        + strList(source)
        + "---\n"
    )

    finalString = yaml + replaceBrackets
    # create markdown file and fill with proc.dumpFileData()
    with open(os.path.abspath(OUTPUT_PATH + titleLower + ".md"), "w") as f:
        f.write(finalString)


if __name__ == "__main__":
    main()
