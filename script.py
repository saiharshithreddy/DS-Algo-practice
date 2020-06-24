import fileinput
import sys
from pathlib import Path
readme = 'README.md'

def add_content(*args):

    def content(count, tags):
        s_no = "| " + str(count)
        filen = ' '.join(filename[:-3].split('-'))
        question = "| [" + filen + "]"
        question_link = "(" + leetcode + filename[:-3] + ") |"
        solution = "[" + topic + "]" + "(" + new_file_path + ") |"
        diff = difficulty + " | "
        
        try:
            if tags != " | |": 
                s = tags.split('-')
                tags = "`" + " ` `".join(s) + "`| |"
        except:
            tags = " | |"    
        text = s_no + question + question_link + solution + diff + tags
        return text
    
    topic = args[0][1]
    filename = args[0][2]
    difficulty = args[0][3]
    
    try:
        tags = args[0][4]
    except:
        tags = " | |"   
    
    leetcode = 'https://leetcode.com/problems/'
    category = "### " + topic
    # if tags == "" tags
    try:
        new_file_path = 'Python/' + topic + '/' + filename
        Path(new_file_path).touch()
    except: pass
    
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
                f.write(content(count-2, tags))
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
        
            

if __name__ == "__main__":
    add_content(sys.argv)
