import requests #to make the http request
import os #to access the operating systen commands to read and create folders
from tkinter import *

directory_folder = "webpages/"

def download_url():
    url = url_field.get()
    status_str = ""
    if url != "":
        req = requests.get(url) #make the page request
        html = req.text #read the html and save it in a variable
        remove_http = url.split("//")[-1] #remove the http:// or https:// prefix
        if remove_http != html: #if there was a http prefix, print that it was removed
            status_str += "\n" + "Removed HTTP Prefix"
        folders = remove_http.split("/")[1:-1]  #create a list of the folders for this page
        file_name = "-".join(url.split("/")[-1].split("?")) #get the name of the page with the extension
        if "." not in file_name: #if there is no extension
            file_name = file_name+".html" #assume it is a .html
            status_str += "\n" + "No Extension Found, Assumed HTML"
        directory = "/".join(folders) #recreate the directory from the url
        if directory != "":
            try:
                os.stat(directory_folder+directory) #check if the directory exists on your pc
                status_str += "\n" + "Directory Already Exists"
            except:
                os.makedirs(directory_folder+directory) #if it doesn't exist, create it
                status_str += "\n" + "Created Directory"
            path = directory_folder+directory+"/"+file_name #create the path for the file to be saved
        else:
            path = directory_folder+file_name
        os.makedirs(directory_folder, exist_ok=True)
        with open(path, "w", encoding="UTF-8") as file: #create and open the file with write permissions
            file.write(html) #write the html to the file (or what ever it is, image, etc..)
        status_str += "\n" + "Saved As: " + path
        string.set("")
    else:
        status_str += "\n" + "Blank Field!"
        string.set("")
    print(status_str)
    status.set(status_str[1:])

window = Tk()
window.geometry("800x600") #You want the size of the app to be 500x500
#window.resizable(0, 0) #Don't allow resizing in the x or y direction
window.wm_title("WebpageDownloader")
sp = r"assets/"
imgicon = PhotoImage(file=os.path.join(sp,'icon.ico'))
window.tk.call('wm', 'iconphoto', window._w, imgicon)

frame = Frame(window)
frame.grid(row=0, column=0)
string,status = StringVar(),StringVar()
url_field = Entry(frame, textvariable=string, width=100)
url_label = Label(frame, text="URL:")
download_button = Button(frame, text="Download URL", command=download_url)

url_label.grid(row=0, column=0)
url_field.grid(row=0, column=1, columnspan=30)
download_button.grid(row=1,columnspan=1, sticky=W)
status_label = Message(frame, textvariable=status, width=1000)
status_label.grid(row=2,columnspan=5,rowspan=5)

window.mainloop()


