print ("Welcome to General Purpose Macro Preprocessor.\n")
f=open("Test.txt", "r")
f1=f2=f.readlines()
l=k=l100=len(f1)
def CProg():
    d={}
    d1={}
    d2={}
    d3={}
    d4={}
    d5={}
    ls=['printf(), scanf(), getc(), gets(), getchar(), fopen(), fclose(), remove(), putc(), putw()']
    lc=[]
    l2=[]
    lc1=[]
    lc2=[]
    lc3=[]
    lc4=[]
    lc5=[')',';','{','}']
    lc6=[]
    m12=[]
    s=''
    s1=''
    s23=''
    s34=''
    
    #Printing the C Code from file.
    
    print ("***************C Program Discovered***************\n")
    for i in range(l100):
        if f1[i]=="/C\n":
            l2.append(f1[i])
            for k in range(i+1,l100):
                if (f2[k]!="/P\n" and f2[k]!="/N\n"):
                    if f2[k]!='\n':
                        print f2[k],
                        l2.append(f2[k])
                    else:
                        continue
                else:
                    print ("End of C Code!\n")
                    print ('*'*50)

    #Identifying the Macro Definitions using the keyword #define and storing its value in a dictionary.
           
    for i in range(len(l2)):
        f3=l2[i].split(' ',1)
        m=len(f3)
        if f3[0]=='#ifdef':
            j12=f3
            j12[1]=j12[1].split(' ',1)
            if j12[1][0] in d:                
                for k12 in j12[1][1]:
                    if k12!=';' and k12!=' ' and k12!='\n':
                        s23=s23+k12
                f3=[]
                s23=s23+' ;\n'
                f3.append(s23)
                lc1.append(f3)
                del lc1[-1]
            else:
                print "Undefined!"

        if f3[0]=='#ifndef':
            j12=f3
            j12[1]=j12[1].split(' ',1)
            if j12[1][0] not in d:                
                for k12 in j12[1][1]:
                    if k12!=';' and k12!=' ' and k12!='\n':
                        s34=s34+k12
                f3=[]
                s34=s34+' ;\n'
                f3.append(s34)
                lc1.append(f3)
                del lc1[-1]
            else:
                print "Undefined!"
                
        if f3[0]=='#define':
            if 'v' not in f3[1]:
                f4=f3[1].split(' ')
                d1[f4[0]]=f4[1]                                                                 
                for i12 in f4[1]:
                    if i12.isalpha():
                        m12.append(i12)
                f5=f4[2].split('\n')[0]
                d2[f4[0]]=f5
                d3[d1[f4[0]]]=f5
                
            else:
                f3=f3[1].split(' v ')
                a=f3[0]
                b=f3[1]
                b=b.split('\n')[0]
                d[a]=b               
        else:
            lc1.append(f3)
            i=i+1
     
    #Removing Single Line Comments from the code.

    for j in lc1:
        for i in j:
            r=i.split(' ')
            k=r[-1]
            if k[0]=='/' and k[1]=='/':
                del r[-1]
                i=r
                for g in i:
                    if g!='' and g not in lc5:
                        lc2.append(g)
                    elif g in lc5:
                        g=g+'\n'
                        lc2.append(g)
                    else:
                        continue
                
            else:
                lc2.append(i)
                continue

    #Joining the elements of the list in the printable format.
            
    for s in lc2:
        lc3.append(s)
        lc4.append(lc3)
        lc3=[]
        
    for j in lc4:
        for i in j:
            i=i.split(' ')
            for k in i:
                if k in d:
                    lc.append(d[k])
                else:
                    lc.append(k)


    #Replacing the Macros with their values, also working for nested definitions.
                
    for i in range(len(lc)):
        while lc[i] in d:
            lc[i]=d[lc[i]]
        else:
            continue
        
    for i in range(len(lc)):
        if lc[i] in d2:
            lc[i+1]=lc[i+1].split('\n')[0]
            m=lc[i+1]
            m=m.split('(')[1]
            m=m.split(')')[0]
            m=m.split(',')
            
            for j in d1:
                if j==lc[i]:
                    if len(d1[j])==len(lc[i+1]):
                        for k in d3:
                            if k==d1[j]:
                                k=k.split('(')[1]
                                k=k.split(')')[0]
                                k=k.split(',')
                                dff=d3[d1[j]]

                                for i21 in range(len(m)):
                                    for j21 in range(len(m12)):
                                        if i21==j21:
                                            d4[m12[j21]]=m[i21]
                                        else:
                                            continue
                                for i3 in dff:
                                    if i3 in d4:
                                        s1=s1+d4[i3]
                                    else:
                                        s1=s1+i3
                                lc[i]=s1
                                lc[i+1]=''
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
        else:
            continue

    #Printing the Expanded version of the code.
        
    print ("After Expanding the Macro and Re-writing the Code.\n")            
    for i in range(len(lc)):
        if lc[i]=="/C\n":
            for k in range(i+1,len(lc)):
                if (lc[k]!="/P\n" and lc[k]!="/N\n"):
                    if (lc[k]!='\n' and lc[k]!=''):
                        print lc[k],
                    else:
                        continue
                else:
                    print ("\nEnd of Expanded C Code!")
                    print ('*'*50)
    d={}
    d1={}
    d2={}
    d3={}
    d4={}
    d5={}
                    
def PProg():
    p0={}
    p1={}
    p2={}
    p3={}
    p4={}
    p5={}
    lp=[]
    lp1=[]
    lp2=[]
    lp3=[]
    lp4=[]
    lp5=[]
    lp6=[]
    p12=[]
    s=''
    s1=''
    s23=''
    s34=''
    
    print ("*************Python Program Discovered*************\n")
    for i in range(l):
        if f1[i]=="/P\n":
            for k in range(i+1,l):
                if (f2[k]!="/C\n" and f2[k]!="/N\n"):
                    if f2[k]!='\n':
                        print f2[k],
                        lp1.append(f2[k])
                    else:
                        continue
                else:
                    print ("\nEnd of Python Code!\n")
                    print ('*'*50)
                    break
                
    #Removing Single Line Comments.
                
    for j in lp1:
        if (' '*2) in j:
            r=j.split('  ')
            k=r[-1]
            if k[0]=='#':
                del r[-1]
                j=r
                for g in j:
                    if g!='':
                        lp2.append(g)
                    else:
                        continue                
            else:
                lp2.append(j)
                continue
        else:
            lp2.append(j)
            continue
        
    #Conditional Macro Check.
        
    for p in lp2:
        f3=p.split(' ',1)
        if f3[0]=='#ifdef':
            j12=f3
            j12[1]=j12[1].split(' ',1)
            if j12[1][0] in p0:                
                for k12 in j12[1][1]:
                    if k12!=' ' and k12!='\n':
                        s23=s23+k12
                f3=[]
                s23=s23+'\n'
                f3.append(s23)
                lp3.append(f3)
                del lp3[-1]

        if f3[0]=='#ifndef':
            j12=f3
            j12[1]=j12[1].split(' ',1)
            if j12[1][0] not in p0:                
                for k12 in j12[1][1]:
                    if k12!=';' and k12!=' ' and k12!='\n':
                        s34=s34+k12
                f3=[]
                s34=s34+'\n'
                f3.append(s34)
                lp3.append(f3)
                del lp3[-1]

        #Single Line Macro Definitions.
                
        if f3[0]=='#define':
            if 'v' not in f3[1]:
                f4=f3[1].split(' ')
                p1[f4[0]]=f4[1]                                                                 
                for i12 in f4[1]:
                    if i12.isalpha():
                        p12.append(i12)
                f5=f4[2].split('\n')[0]
                p2[f4[0]]=f5
                p3[p1[f4[0]]]=f5
                
            else:
                f3=f3[1].split(' v ')
                a=f3[0]
                b=f3[1]
                b=b.split('\n')[0]
                p0[a]=b     
        else:
            lp3.append(f3)
            i=i+1

    #Making it into printable format.
            
    for i in lp3:
        for j in range(len(i)):
            if j!=(len(i)-1):
                lp4.append(i[j])
            else:
                if '\n' not in i[j]:
                    i[j]=i[j]+'\n'
                    lp4.append(i[j])
                else:
                    lp4.append(i[j])

    #Replacing Single Line and Nested Macro Variables.
                    
    for k in lp4:
        if k in p0:
            if '\n' in k:
                k=k.split('\n')[0]            
                lp.append(p0[k])
            else:
                lp.append(p0[k])
        else:
            lp.append(k)

    for i in range(len(lp4)):
        lp4[i]=lp4[i].split('\n')[0]
        if lp4[i] in p0:
            while lp4[i] in p0:
                lp4[i]=p0[lp4[i]]
            lp4[i]=lp4[i]+'\n'
            lp5.append(lp4[i])
        else:
            lp5.append(lp4[i])

    #Macros with Arguments.
    
    for i in range(len(lp5)):
        if lp5[i] in p2:
            lp5[i+1]=lp5[i+1].split('\n')[0]
            m=lp5[i+1]
            m=m.split('(')[1]
            m=m.split(')')[0]
            m=m.split(',')
            for j in p1:
                if j==lp5[i]:
                    if len(p1[j])==len(lp5[i+1]):
                        for k in p3:
                            if k==p1[j]:
                                k=k.split('(')[1]
                                k=k.split(')')[0]
                                k=k.split(',')
                                dff=p3[p1[j]]
                                for i21 in range(len(m)):
                                    for j21 in range(len(p12)):
                                        if i21==j21:
                                            p4[p12[i21]]=m[i21]
                                for i3 in dff:
                                    if i3 in p4:
                                        s1=s1+p4[i3]
                                    else:
                                        s1=s1+i3
                                lp5[i]=s1
                                lp5[i+1]='\n'
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
        else:
            continue

    #Printing the Expanded Code.

    print ("After Expanding the Macro and Re-writing the Code.\n")            
    for i in lp5:
        if '\n' in i:
            i=i.split('\n')[0]
            print i
        else:
            print i,

    
def main():
    for i in range(l):
        if  f1[i]=="/C\n":
            CProg()
            print "\nThank You for using OUR Macro Processor!"
            print "*"*50
        if  f1[i]=="/P\n":
            PProg()
            print "\n\nThank You for using OUR Macro Processor!\n"
        
main()


