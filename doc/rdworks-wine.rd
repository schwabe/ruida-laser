                                jw, Do 30. Nov 05:57:07 CET 2017

install RDWorks with wine
=========================
# see also https://stefan.schuermans.info/rdcam/wine.html

unrar x ~/Downloads/RDWorksV8.rar
wget https://dl.winehq.org/wine-builds/Release.key
sudo apt-key add Release.key
sudo apt-add-repository 'https://dl.winehq.org/wine-builds/ubuntu/'
sudo apt-get update
sudo apt-get install winetricks
winetricks mfc42
wine ~/RDWorksV8-2016-04-24/RDWorksV8Setup8.01.18.exe
 > exit
 > exit 
 > ...
wine ~/.wine/drive_c/RDWorksV8/RDWorksV8.exe
