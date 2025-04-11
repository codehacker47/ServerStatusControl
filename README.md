<h1 align="center">ServerStatusControl (S.S.C)<br />
<div align="center">
</div></h1>

This project is a web application developed with Flask for apt-based Linux distros to monitor disk usage and temperature sensors on a server. It includes functionality to restart the Samba service and display detailed information about the server status.

## Features ✨

- Control temperature of a disk
- Restart Samba from your browser
- See how much space is occupied on the disk

## Installation

Clone the repository and change the directory to it's folder, then install the requirements
```shell
pip install requirements.txt
```
For this to work you have to install the lm-sensors package and detect sensors first!
## Configuration

There are some things you need to change in the main.py file in order to make it work.
In the file there are comments of where to change the parameters, you need to change the disk directory and optionally(but raccomended!) the app secret key.
You can change the port to connect with a browser(the default is 80).

## Future updates

- Email S.M.A.R.T report of the disk.
- Control the server via email(using an IMAP server)
- CSS for better user interface

## License

This software is licensed with the GNU General Public License V3.0

