

def handle_uploaded_file(f):
    with open('app\DataFiles\File.xlsx','wb+') as destination:
        for chunk in f.chunks():
             destination.write(chunk)


