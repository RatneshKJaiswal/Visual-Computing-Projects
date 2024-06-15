# multi lined string

a = '''Sdufh ffhg
 gjg 
 gigigig iugi8fyg 
  gygigi gigeesgvjhg
  yrevg gv rsxrf  dds '''
print(a)

# indexing
print(a[1])

# lets use a for loop

name = "Ratnesh Kumar Jaiswal"
for character in name:
    print(character)

# length
print(len(name))

# STRING SLICING --> getting sub string
print(name[0:5])

# name[len(name)-3:len(name)-1]
print(name[-3:-1])

# Strings are immutable

# .upper() .lower()

# .rstrip()
print(name.rstrip("h"))

# .replace("old","new")

# .split() --> splits name when ever " " encounters
print(name.split(" "))

# .capitalize()

# .count()
print(a.count("g"))

# .find() --> returns index
# .index()
# .islower() .isupper()

