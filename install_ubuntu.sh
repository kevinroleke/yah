if [ "$EUID" -ne 0 ]
  then echo "I'm Special, Run Me As Root."
  exit
fi

printf "Shell (zsh/bash): "
read shell

repo=https://github.com/bobmcdouble3/opensourcetester.git
folder=$(pwd)

apt-get install python -y

wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
rm get-pip.py

pip2 install requests
if [ -d "/opt/yahweh" ]; then
  rm -r /opt/yahweh
fi
mkdir -p /opt/yahweh

cd /opt/yahweh && git clone $repo
cd /opt/yahweh && mv opensourcetester/* ./ && rm opensourcetester -r
cd /opt/yahweh && mv yahweh.py yahweh
cd /opt/yahweh && chmod +x yahweh

if [ $shell = "zsh" ]
then
  if grep -q "export PATH=\$PATH:/opt/yahweh" "/home/kevin/.zshrc";
  then
    echo "Already Installed, Updating"
  else
    echo "export PATH=\$PATH:/opt/yahweh" >> ~/.zshrc
    source ~/.zshrc
  fi
fi
if [ $shell = "bash" ]
then
  if grep -q "export PATH=\$PATH:/opt/yahweh" "/home/kevin/.bashrc";
  then
    echo "Already Installed, Updating"
  else
    echo "export PATH=\$PATH:/opt/yahweh" >> ~/.bashrc
    source ~/.bashrc
  fi
fi

printf "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
echo "[*] Installed"
