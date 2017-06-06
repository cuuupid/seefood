import sys, os
f=open('label_map.pbtxt','r')
lines = f.readlines()
x=4
while x<len(lines):
    lines[x]="  target_class_string: \"n00000000\"\n"
    x=x+4
lines[3740]="  target_class_string: \"n00000001\"\n"
f.close()
f=open('label_map.pbtxt','w')
for line in lines:
    f.write(line)
f.close()
print("[+] Successfully created label map.")