# create files in different directories -> write information to them
contents = ["All carrots are to be sliced longways.",
            "The carrots were reportedly sliced.",
            "The slicing process was well presented."]

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)
