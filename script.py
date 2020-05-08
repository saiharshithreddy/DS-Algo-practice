import fileinput
import sys
from pathlib import Path
import git
readme = 'README.md'

def add_content(topic, filename, difficulty):

    leetcode = 'https://leetcode.com/problems/'
    category = "### " + topic

    try:
        new_file_path = 'Python/' + topic + '/' + filename
        Path(new_file_path).touch()
    except: pass
    def content(count):
        s_no = "| " + str(count)
        question = "| [" + filename[:-3] + "]"
        question_link = "(" + leetcode + filename[:-3] + ") |"
        solution = "[" + topic + "]" + "(" + new_file_path + ") |"
        diff = difficulty + "| | |"
        text = s_no + question + question_link + solution + diff
        return text
    with open('README.md', 'r') as f:
        lines = f.readlines()
        f.close()
    with open('README.md', 'w') as f:

        found = False
        count = 0
        for line in lines:

            if category in line.strip():
                count = 1
                found = True

                f.write(line)


            elif (found and len(line.strip()) == 0) or filename[:-3] in line.strip():
                f.write(content(count-2))
                f.write('\n')
                if len(line.strip()) == 0:
                    f.write('\n')
                found = False
                count = 0

            else:
                if count != 0:
                    count += 1
                f.write(line)
        f.close()
        git.add()
            

if __name__ == "__main__":
    add_content(sys.argv[1], sys.argv[2], sys.argv[3])
