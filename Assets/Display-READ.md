 #~ cme --help
usage: cme [-h] [-v] [-t THREADS] [--timeout TIMEOUT] [--jitter INTERVAL]
          [--darrell] [--verbose]
          {http,smb,mssql} ...

     ______ .______           ___        ______  __  ___ .___  ___.      ___      .______    _______ ___   ___  _______   ______
    /      ||   _  \         /   \      /      ||  |/  / |   \/   |     /   \     |   _  \  |   ____|\  \ /  / |   ____| /      |
   |  ,----'|  |_)  |       /  ^  \    |  ,----'|  '  /  |  \  /  |    /  ^  \    |  |_)  | |  |__    \  V  /  |  |__   |  ,----'
   |  |     |      /       /  /_\  \   |  |     |    <   |  |\/|  |   /  /_\  \   |   ___/  |   __|    >   <   |   __|  |  |
   |  `----.|  |\  \----. /  _____  \  |  `----.|  .  \  |  |  |  |  /  _____  \  |  |      |  |____  /  .  \  |  |____ |  `----.
    \______|| _| `._____|/__/     \__\  \______||__|\__\ |__|  |__| /__/     \__\ | _|      |_______|/__/ \__\ |_______| \______|

                                        A swiss army knife for pentesting networks
                                   Forged by @byt3bl33d3r using the powah of dank memes

                                                     Version: 4.0.0dev
                                                    Codename: 'Sercurty'

optional arguments:
 -h, --help         show this help message and exit
 -v, --version      show program's version number and exit
 -t THREADS         set how many concurrent threads to use (default: 100)
 --timeout TIMEOUT  max timeout in seconds of each thread (default: None)
 --jitter INTERVAL  sets a random delay between each connection (default: None)
 --darrell          give Darrell a hand
 --verbose          enable verbose output

protocols:
 available protocols

 {http,smb,mssql}
   http             own stuff using HTTP(S)
   smb              own stuff using SMB and/or Active Directory
   mssql            own stuff using MSSQL and/or Active Directory
