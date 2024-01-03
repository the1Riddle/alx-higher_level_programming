# JavaScript - Web scraping

## Installation
**Install Node 10**
```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
**Install semi-standard**<br>
[Documentation](https://github.com/standard/semistandard)
```
$ sudo npm install semistandard --global
OR
$ sudo npm install semistandard --global --fix
```
**Install ``request`` module and use it**<br>
[Documentation](https://github.com/request/request)
```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```
**Notes:** Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).

***on more installaton guide you can check out on this*** [installations](https://github.com/the-1Riddle/packageInstallationHub/tree/master/alx-tools_installation)

## Files & Descriptions
| Files			     | Descriptions                                                                           |
| -------------------------- |:-------------------------------------------------------------------------------------- |
| 0-readme.js                | Read and prints the content of a file                                                  |
| 1-writeme.js               | Writes a string to a file                                                              |
| 2-statuscode.js            | Display the status code of a get request                                               |
| 3-starwars_title.js        | Prints the title of a Star Wars movie where the episode number matches a given integer |
| 4-starwars_count.js        | prints the number of movies where the character “Wedge Antilles” is present            |
| 5-request_store.js         | Gets the contents of a webpage and stores it in a file.                                |
| 6-completed_tasks.js       | Computes the number of tasks completed by user id.                                     |
| 100-starwars_characters.js | Prints all characters of a Star Wars movie                                             |
| 101-starwars_characters.js | Prints all characters of a Star Wars movie in the right order                          |
