# Program to print from <html> to <html>

string = """Start<html>This file has an error ...........jdjsalkjdaslkjdlsajlkdjsklkdddsnd,msand,mnsa,dnsa,nd,sand,nsd,nsdn \\
line2ncncnxzcmnzx,cn,xzc,zmxnc,mnxz,cmnxz,,mcnndjcnxsncjdsncjxvndiddxc xzczx...............and this is the end........end<html>  \\
The e mail continues ..................................x,mnvoiirvknmcjvnkcvc................................................. \\
line4<html>This is the new error......................ivcnvcxnvidhvkncxnvjbxcivxczbvcxvifvncx................................ \\
......................mxnzc,mndknkdjsnnsdkfnds,mcn x,nvkjkcn....................................This is the end........end<html>Stop"""

count = string.count("<html>")

item = "<html>"
new = 0
number = 0

while (number < count):
    if item in string:
        a = string.find("<html>",int(new),len(string))      # 1st <html> start , # 3rd <html> start # checks for 5th <html> gets -1
        if a == -1:
            break
        else:
            b = a + 6                                       #1st <html> end    , # 3rd <html> end
            c = string.find("<html>",int(b),len(string))    # 2nd <html start  , # 4th <html> start
        
            print(string[int(b):int(c)],'\n')
            new = c + 6                                     # 2nd <html> end   , # 4th <html> end
            number +=1
            
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#        O/P
#        This file has an error ...........jdjsalkjdaslkjdlsajlkdjsklkdddsnd,msand,mnsa,dnsa,nd,sand,nsd,nsdn \
#        line2ncncnxzcmnzx,cn,xzc,zmxnc,mnxz,cmnxz,,mcnndjcnxsncjdsncjxvndiddxc xzczx...............and this is the end........end 

#        This is the new error......................ivcnvcxnvidhvkncxnvjbxcivxczbvcxvifvncx................................ \
#        ......................mxnzc,mndknkdjsnnsdkfnds,mcn x,nvkjkcn....................................This is the end........end 





