# Yah
## 2021 Retrospective
When I wrote Yah several years ago, the issue of API tokens being left in Github repositories was rampant. Attackers could easily find AWS keys, Bitcoin private wallets, or any number of sensetive keys. Nowadays Github has its own built-in protections for this, in addition to several third party bots (such as from DiscordApp) using similar software to Yah. All-in-all, this is not really a huge issue anymore, but I like to keep this up. :D 
## What?
Yah is a tool, to combat the accidental leaking of API tokens, RSA keys and other credentials, on Github.
Yah is modular and expandable. You can easily, write a module and drop it into a folder. Yah will automatically detect the new addition and start parsing for it.
Yah comes with a few modules, that look for some of the most commonly, exposed credentials. The included parser modules look for, AWS tokens, Firebase keys, Googleapis tokens (eg. Google Maps,) and RSA + SSH keys.
## Why?
There is an endless amount of exposed credentials on Github. These credentials are being farmed by malicious bots. Run Yah, on all your Github accounts, before the bad bots reach your repositories.  
