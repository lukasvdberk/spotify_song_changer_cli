
### Use it with i3
To use it with i3 add the following desktop file in your ~/.local/share/applications. 
Make sure you installed the requirements globably with pip install requirements.txt

Example desktop file
```
#!/usr/bin/env xdg-open
[Desktop Entry]
Type=Application
Name=sp
GenericName=sp
Comment=Changes sets a new song for spotify
Exec=/usr/bin/python3 "/home/lukas/Documents/Programming Projects/change_song_spotify/app.py" master o>
Terminal=true
StartupNotify=true
Categories=Music;
Keywords=sp;
```

Replace the Exec with your python path and the path of the file to where you downloaded the app.yp