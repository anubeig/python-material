try:

    fd = open("sample.txt", "w+r")

    with open("test.txt", "w+r") as f:
        print type(f)
        f.write("Hello\nHow r u ??")
        print f.read()  # it prints empty string The file cursor has been moved to be after your writes. #
        # That is the natural consequence of writing.
        # If you want to read what you wrote, you need to reset the file cursor back to the beginning of the file:
        f.seek(0)
        print f.read()
        print f.tell()  # tell the cursor position

        f.seek(0)

        list1 = []
        
        for line in f.readlines():
            list1.append(line.split())
        print list1
    print type(fd)
finally:
    fd.close()

"""
sh-4.3$ python main.py
<type 'file'>

Hello
How r u ??
16
[['Hello'], ['How', 'r', 'u', '??']]
<type 'file'>
"""



