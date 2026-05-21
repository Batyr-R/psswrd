# psswrd - a washed password manager prototype


psswrd is **going** to be a password manager, but right now its just a password reliability checker, generator, and storage without encryption (dont use if u want to be safe)

## how to install


install uv with:

`pip install uv`


open terminal and open the program folder with:

`cd PROGRAMPATH`


sync the uv

`uv sync`


## features


### check


check your password (optional entropy estimation):

`uv run psswrd check 'YOURPASSWORD' [--entropy]`


### generate


generate a random reliable password (optional length choice, default 16):

`uv run psswrd gen [--length NUMBER]`


### store (no encryption yet **NOT SAFE**)

it will make a new json file for all of the passwords on first add


add service login password:

`uv run psswrd storage add`

rmv a login from a service

`uv run psswrd storage rm SERVICE LOGIN`
