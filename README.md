# Yah
## What?
Yah is a tool, to combat the accidental leaking of API tokens, RSA keys and other credentials, on Github.
Yah is modular and expandable. You can easily, write a module and drop it into a folder. Yah will automatically detect the new addition and start parsing for it.
Yah comes with a few modules, that look for some of the most commonly, exposed credentials. The included parser modules look for, AWS tokens, Firebase keys, Googleapis tokens (eg. Google Maps,) and RSA + SSH keys.
## Why?
There is an endless amount of exposed credentials on Github. These credentials are being farmed by malicious bots. Run Yah, on all your Github accounts, before the bad bots reach your repositories.  
# Installing
## Ubuntu
`wget "https://rawgit.com/bobmcdouble3/opensourcetester/master/install_ubuntu.sh" && sudo bash install_ubuntu.sh && rm install_ubuntu.sh`
