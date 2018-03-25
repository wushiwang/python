import difflib
import sys
def readfiLe(filename):
    try:
        fileHandle=open(filename,'rb')
        text=fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as e:
        print("Read file Error:"+str(e))
        sys.exit()

        
try:
    if sys.argv[1]=="" or sys.argv[2]=="":
        print("Usage:python simple3.py textfile1 textfile2 > diff.html")
        sys.exit()
    else:
        textfile1=sys.argv[1]
        textfile2=sys.argv[2]
        text1_lines = readfiLe(textfile1)
        text2_lines = readfiLe(textfile2)
        d=difflib.HtmlDiff()
        print(d.make_file(text1_lines,text2_lines))
except Exception as e:
    print("Error:"+str(e))
    print("Usage:python simple3.py textfile1 textfile2 > diff.html")





