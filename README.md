# srv_zero

Micro http-server that allow just to download files.

## Usage

1. Place files you want to deliver to `srv/app/static` directory.

2. (optional) Change `PORT` variable in `srv/main.py` script. By default,
`PORT=20202`.

3. Run `srv/run.sh`. Download files via link
"http://\<address>:\<port>/\<file name>". Quit the server.

## License

***srv_zero*** is released under the Creative Commons License. See the
[LICENSE](https://github.com/fostroll/srv_zero/blob/master/LICENSE) file for
more details.
