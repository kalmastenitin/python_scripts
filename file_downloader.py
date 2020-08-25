import requests,datetime,os


def download_file(url):
    extension = url.split('.')[-1]
    now = datetime.datetime.now()
    timestamp = now.strftime("%d%m%Y%H%M")
    filename = timestamp+'.'+extension
    print(filename)
    r = requests.get(url,stream=True)
    with open(filename,'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return filename


download_file('https://file-examples-com.github.io/uploads/2017/04/file_example_MP4_1920_18MG.mp4')
