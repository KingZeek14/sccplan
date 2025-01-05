#/bin/bash

echo "Make PATH caller?(y/n)"
read chkInstall

if [ $chkInstall == "y" ] 
then
    echo "Getting on that..."
    # touch /home/$USER/.local/bin/sccplan
    sleep 2
    echo "Making symlinks..."
    ln -s $PWD/sccplan.py /home/$USER/.local/bin/sccplan
    echo "Done! You can now run "sccplan" to run the script!"

elif [ $chkInstall == "n" ]
then
    echo "Ok"
fi
