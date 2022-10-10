# Windows MP3 Downloader Using Python

This personal project helped me to easily download any YouTube's video audio as a MP3 file.

### User Guide

To use the downloader on your system you just need to have Python installed, open Windows CMD 
or PowerShell on the directory where yt_mp3.py is located and type as follows:

py yt_mp3 {link} -o {path-to-directory (optional)}

You should insert the arguments without brackets and the path must be between quotation marks. If _py_ do not work for you try _python_ instead. 
When no directory is specified, the script automatically saves the MP3 to your Music folder.

It is also interesting to pack the Python program as a Windows executable (.exe) with packages like _pyinstaller_ 
(https://stackoverflow.com/questions/5458048/how-can-i-make-a-python-script-standalone-executable-to-run-without-any-dependen), so the program can run
on PCs that do not even have Python, and it is even better when you add the executable file location to system path 
(https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/), so you can call it from any Windows directory.

I will not share my .exe file because no one should ever run suspicious executables on their PC.

#### Example
py yt_mp3.py https://youtu.be/fqsMCEgHMrE -o "C:\Users\MyUser\Desktop\MP3 downloader"

### Limitations and Thoughts

- It is still not possible to download playlists with this script;
- No option to also download the videos;
- It would be nice to search videos by name to download then without the need to open YouTube (potentially a GUI listing options).
