#This file is used to add questions for specified subjects by the Teacher.
import os
K1=list(["define", "find", "how", "label", "list", "match", "name", "omit", "recall", "relate", "select", "show", "spell", "tell", "what", "when", "where", "which", "who", "why"])
K2=list(["classify", "contrast", "demonstrate", "extend", "illustrate", "infer", "interpret", "outline", "relate", "rephrase", "show", "summarize", "translate"])
K3=list(["apply","develop", "experiment with", "identify", "interview", "make use of model", "organize", "plan", "select", "utilize"])
K4=list(["analyze", "assume", "categorize", "classify", "compare", "conclusion", "contrast", "discover", "dissect", "distinguish", "divide", "examine", "function", "inference", "inspect" "list", "motive", "relationships", "simplify", "survey", "take part in", "theme"])
K5=list(["agree", "appraise", "assess", "award","compare", "conclude", "criteria", "criticize", "decide", "deduct", "defend", "determine", "disprove","evaluate", "explain", "importance", "influence", "interpret", "judge", "justify", "mark", "measure", "opinion", "perceive", "prioritize", "prove", "rate", "recommend", "rule on", "select", "support", "value"])
K6=list(["adapt", "build", "change", "choose", "combine", "compile", "compose", "construct", "create", "delete", "design", "develop",  "discuss", "elaborate", "estimate", "formulate", "happen", "imagine", "improve", "invent", "make up", "maximize", "minimize", "modify", "original", "originate", "plan", "predict", "propose", "solution", "solve", "suppose", "test", "theory"])
print("------------------Welcome To Automatic Question Paper Generation System---------")
print("---------------------------------------------------------------------------------")
print("Enter the Subject Name. eg: 'Operating System'")
subject_name=input().upper()
file_name=os.getcwd()+"\\Subjects\\"+subject_name+".txt"
file=open(file_name,'a')
with open(file_name,'r') as file1:
    data = file1.read().split("\n")
print("Do you want to enter more questions? Yes/No")
choice=input().upper()
while(choice=="YES"):
    print("Enter Question?")
    quest=input()
    if quest in data:
        print("Question Already Present ! Enter a different Question.")
        continue;
    else:
        comp1=quest.split()
        for x in range(len(comp1)):
            if comp1[x].lower() in K1:
                quest1=quest+"::K1\n"
                file.write(quest1)
                print("The question is a K1 level question")
            if comp1[x].lower() in K2:
                quest2=quest+"::K2\n"
                file.write(quest2)
                print("The question is a K2 level question") 
            if comp1[x].lower() in K3:
                quest3=quest+"::K3\n"
                file.write(quest3)
                print("The question is a K3 level question") 
            if comp1[x].lower() in K4:
                quest4=quest+"::K4\n"
                file.write(quest4)
                print("The question is a K4 level question") 
            if comp1[x].lower() in K5:
               quest5=quest+"::K5\n"
               file.write(quest5)
               print("The question is a K5 level question") 
            if comp1[x].lower() in K6:
               quest6=quest+"::K6\n"
               file.write(quest6)
               print("The question is a K6 level question") 

        print("Do you want to enter more questions? Yes/No")
        choice=input().upper()
print("Questions Submitted Successfully.")
file.close()
file1.close()
