a=input()
a=a[::-1]
i=0
result=''
while(i<=len(a)-1):
  count=0
  if(a[i]=='<'):
    while(a[i]=='<'):
      count=count+1
      i=i+1
    i=i+count
  else:
    if(i<=len(a)-1):
      result=result+a[i]
      i=i+1
print(result[::-1])

