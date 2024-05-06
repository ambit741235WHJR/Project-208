# Importing the necessary libraries
import socket
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

# Declaring the global variables
IP_ADDRESS = '127.0.0.1'
PORT = 8000
BUFFER_SIZE = 4096
SERVER = None

# Setup function to initialize the client
def setup():
    # Getting the global variables along with its values
    global SERVER
    global IP_ADDRESS
    global PORT

    # Creating a socket for the client
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connecting the client to the server
    SERVER.connect((IP_ADDRESS, PORT))

    # Calling the music window function
    musicWindow()

# Creating the GUI for the music window
def musicWindow():
    # Creating a new window
    music_window = Tk()

    # Setting the title of the window
    music_window.title("Music Player")

    # Setting the geometry of the window
    music_window.geometry('300x300')
    
    # Setting the background of the window
    music_window.configure(bg='LightSkyBlue')

    # Creating a label for the select song option
    select_song_label = Label(music_window, text="Select Song", bg='LightSkyBlue', font=('Calibri', 8))
    select_song_label.place(x=2, y=1)

    # Creating a listbox widget to display the songs
    songs_listbox = Listbox(music_window, width=39, height=10, activestyle='dotbox', bg='LightSkyBlue', borderwidth=2, font=('Calibri', 10))
    songs_listbox.place(x=10, y=18)

    # Creating a scrollbar for the listbox
    scrollbar = Scrollbar(songs_listbox)
    scrollbar.place(relheight=1, relx=1)
    scrollbar.config(command=songs_listbox.yview)

    # Creating a button to play the selected song
    play_button = Button(music_window, text="Play", width=10, bd=1, bg='SkyBlue', font=('Calibri', 10))
    play_button.place(x=30, y=200)

    # Creating a button to stop the selected song
    stop_button = Button(music_window, text="Stop", width=10, bg='SkyBlue', font=('Calibri', 10))
    stop_button.place(x=200, y=200)

    # Creating a button to upload the song
    upload_button = Button(music_window, text="Upload", width=10, bd=1, bg='SkyBlue', font=('Calibri', 10))
    upload_button.place(x=30, y=250)

    # Creating a button to download the song
    download_button = Button(music_window, text="Download", width=10, bd=1, bg='SkyBlue', font=('Calibri', 10))
    download_button.place(x=200, y=250)

    # Creating an info label
    info_label = Label(music_window, text="", fg='Blue', font=('Calibri', 8))
    info_label.place(x=4, y=280)

    # Running the main loop
    music_window.mainloop()

# Running the setup function
setup()