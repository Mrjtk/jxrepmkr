banner='''                                                      
     _                                     _         
    | |_   _  ____ _____ ____   ___  ____ | |  _  ____ 
 _  | ( \ / )/ ___) ___ |  _ \ / _ \|    \| |_/ )/ ___)
| |_| |) X (| |   | ____| |_| | |_| | | | |  _ (| |    
 \___/(_/ \_)_|   |_____)  __/ \___/|_|_|_|_| \_)_|    
                        |_|                            '''
know='''       This tool is use to help in report writing 
                  Happy hacking Mr.Jtx'''
print(banner)
print(know)
f=open('report.txt','w')
a='''Hello Team,
I am jatin. I am bugbounty hunter'''
summery=input("Summery of the bug:- \n")
Description=input("Description of the bug:- \n")
f.write(a)
f.write("\n")
f.write(" ")
f.write("\n")
f.write("Summery :-")
f.write("\n")
f.write(summery)
f.write("\n")
f.write(" ")
f.write("\n")
f.write("Description :-")
f.write("\n")
f.write(" ")
f.write("\n")
f.write(Description)
f.write("\n")
f.write(" ")
f.write("\n")
f.write("Step to reproduce :-")
f.write("\n")
print("Step to reproduce:-  ")

c=0
while True:
    c+=1
    poc=input(c)
    ln=str(c)
    f.write(ln)
    f.write(".")
    f.write(poc)
    f.write("\n")
    if "EOF"in poc:
        break
    else:
        continue
f.write("\n")
f.write(" ")
f.write("\n")
impact=input("Impact :- \n")
f.write("Impact:-")
f.write("\n")
f.write(" ")
f.write(impact)
f.write("\n")
f.write(" ")
hassolu=input("Has solution [y/n]: ")
if hassolu=="y":
    solu=input("Solution :-")
    f.write("\n")
    f.write(solu)
else:
    print("okay")














    
f.close()