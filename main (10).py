#File handing 
f = open('s.txt','w')# 'w' for write mode
f.write("hello\n")
f.write('hii\n')
f.write("bye bye")
f.close()

#'a' for appending 
g = open('s.txt','a')
g.write("  good to see you")
g.close()

#'r' for read
k = open('s.txt','r')
d = k.read()
print(d)
k.close()

print('basic fundamental clear: BOOM')
