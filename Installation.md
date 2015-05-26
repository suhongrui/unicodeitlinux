# Installation #

Assuming all requirements are installed and working properly...

  1. Fetch UnicodeItLinux source code from the subversion repository
```
svn checkout http://unicodeitlinux.googlecode.com/svn/trunk/ unicodeitlinux
```
  1. Move to the project directory
```
cd unicodeitlinux
```
  1. Get the latest UnicodeIt version from svenkreiss.com (check http://www.svenkreiss.com/UnicodeIt for the latest version of UnicodeIt library and replace the link below accordingly)
```
wget http://www.svenkreiss.com/wiki/images/d/d2/unicodeIt06py.zip
```
  1. Set correct permissions
```
chmod +x unicodeitlinux_v0.1/unicodeitlinux.py
```
  1. Configure your desktop shortcut
Setup your keyboard shortcuts using gconf-editor or any other tool that suits your Desktop Environment,
pointing the keybinding to the unicodeitlinux.py file (e.g. `<alt>+<shift>+u`).

Learn how to [UseIt](Usage.md)