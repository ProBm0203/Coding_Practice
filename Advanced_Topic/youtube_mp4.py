from pytube import YouTube

link = input("Enter the link: ")
youtubeObject = YouTube(link)
youtubeObject = youtubeObject.streams.get_highest_resolution()
try:
    youtubeObject.download()
    print("Download is successful")
except:
    print("An error has occurred")