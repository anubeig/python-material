import shutil

with open("sample.txt", "w") as fd:
    fd.write("Hello")

shutil.copy("sample.txt","Hello.txt")