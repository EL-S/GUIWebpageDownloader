import requests #to make the http request
import os #to access the operating systen commands to read and create folders
from tkinter import *

def download_url():
    url = url_field.get()
    if url != "":
        try:
            
            req = requests.get(url) #make the page request
            html = req.text #read the html and save it in a variable
            remove_http = url.split("//")[-1] #remove the http:// or https:// prefix
            if remove_http != html: #if there was a http prefix, print that it was removed
                status = "Removed http prefix"
                status_label1 = Label(window, text=status)
                status_label1.grid(row=2,columnspan=2)
            folders = remove_http.split("/")[1:-1]  #create a list of the folders for this page
            file_name = url.split("/")[-1] #get the name of the page with the extension
            if "." not in file_name: #if there is no extension
                file_name = file_name+".html" #assume it is a .html
                status = "No extension, assumed html"
                status_label2 = Label(window, text=status)
                status_label2.grid(row=2,columnspan=2)
            directory = "/".join(folders) #recreate the directory from the url
            try:
                os.stat(directory) #check if the directory exists on your pc
                status = "Directory already exists"
                status_label3 = Label(window, text=status)
                status_label3.grid(row=2,columnspan=2)
            except:
                os.mkdir(directory) #if it doesn't exist, create it
                status = "Made directory"
                status_label4 = Label(window, text=status)
                status_label4.grid(row=2,columnspan=2)
            path = directory+"/"+file_name #create the path for the file to be saved
            with open(path, "w") as file: #create and open the file with write permissions
                file.write(html) #write the html to the file (or what ever it is, image, etc..)
            status = "Saved: " + path
            status_label5 = Label(window, text=status)
            status_label5.grid(row=2,columnspan=2)
        except:
            status = "Error"
            status_label6 = Label(window, text=status)
            status_label6.grid(row=2,columnspan=2)
    else:
        status = "Blank Field!"
        status_label7 = Label(window, text=status)
        status_label7.grid(row=2,columnspan=2)

window = Tk()
frame = Frame(window, width=800, height=600)
frame.grid(row=0, column=2)
url_field = Entry(window)
url_label = Label(window, text="Url:")
download_button = Button(window, text="Download Url", command=download_url)

url_label.grid(row=0, column=0)
url_field.grid(row=0, column=1)
download_button.grid(row=1,columnspan=2)


