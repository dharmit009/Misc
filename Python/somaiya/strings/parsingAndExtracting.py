a = "From stephen.march@somaiya.edu Thurday Jan 5 10:14:29 2010"

atposition = a.find('@') 
spposition = a.find(' ') 

beforeAt = a[:atposition].lstrip()
afterAt = a[atposition:]

username=beforeAt[spposition+1:atposition]
print(spposition);
hostname=afterAt[:spposition]

print(username)
print(hostname)
