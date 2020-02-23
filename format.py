
f1 = open("amazon v2.txt",'r')
f2 = open("out1.json",'w')

f2.write("[\n")
n = 0
f11 = f1.readlines()
for row in f11:
    n+=1
    str = ""
    if row.find('Answer this question') != -1:
        continue
    q1 = row.find('Question:')+9
    a1 = row.find('Answer:') 
    qst = " Acer Aspire 5  "+row[q1:a1]
    qst = qst.replace('"',"")
    qst = qst.replace('\\',"")
    #print(qst)
    s1 = row.find('</style>') + 8
    d1 = row.rfind('.')
    
    ans = row[s1:d1]
    ans = ans.replace('"',"")
    ans = ans.replace("\\","")
    if ans == "":
        continue
    
    #print(ans)
    
    str = "{\n\"type\": \"Faq\",\n\"faq\": {\n\"question\": \""
    str+= qst+"\",\n\"answer\": \""
    if n < 49 and n < len(f11)-1:
        str+= ans+"\"\n}\n},\n"
        f2.write(str)
    else:
        str+= ans+"\"\n}\n}\n"
        f2.write(str)
        break
        

    
f2.write("\n]")
