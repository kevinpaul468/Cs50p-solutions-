f=input("File name: ")
f=f.lower()
f=f.strip(" ")
if f.endswith(".gif"):
    print("image/gif")
elif f.endswith(".jpg"):
    print("image/jpeg")
elif f.endswith(".jpeg"):
    print("image/jpeg")
elif f.endswith(".png"):
    print("image/png")
elif f.endswith(".pdf"):
    print("application/pdf")
elif f.endswith(".txt"):
    print("text/plain")
elif f.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
