import urllib.request
import urllib.error
import re
import sys
import string
import webbrowser


cs61a = "https://cs61a.org/"

def execute():
    with urllib.request.urlopen(cs61a) as url_file:
        text = url_file.read().decode("UTF-8")

        q = re.findall("hw/hw[0-9]+.?",text,re.IGNORECASE)
        t= re.findall("lab/lab[0-9]+.?",text,re.IGNORECASE)
        q.extend(t)
        print(q)



def interface():
    execute()
    hw_or_lab = input("hw or lab:")
    assert hw_or_lab in ("hw","lab"),print("ERROR")
    value_string = input("#:")
    if(len(value_string)==1):
        value_string="0"+str(value_string)

    with urllib.request.urlopen( cs61a+hw_or_lab+"/"+hw_or_lab+str(
            value_string)+"/"+hw_or_lab+str(
            value_string)+".zip") as hw:
        information= hw.read()
        zip_file = open(hw_or_lab+str(value_string)+".zip","wb")
        zip_file.write(information)
        zip_file.close()

    webbrowser.open_new(cs61a + hw_or_lab + "/" + hw_or_lab + str(
        value_string) + "/")

    """
    with urllib.request.urlopen(cs61a + hw_or_lab + "/" + hw_or_lab + str(
        value_string) + "/") as instructions:
        text = instructions.read().decode("UTF-8")
        removeTags(text)
    """



def removeTags(text):
    i=0
    start = 0
    endpoint=0
    while(i<len(text)):
        if(text[i] in "<"):
            while(i<len(text) and text[i]!='>'):
                i+=1
            start = i+1

        while(i<len(text) and text[i] !="<"):
            i+=1
        endpoint=i

        chunk = text[start:endpoint]
        if(re.match(" *\n",chunk)):
            continue

        print(chunk)







interface()
