# pathbuilder

The idea for this script came as a solution to an issue I was having: I wanted to add an "Open with VLC" entry to the context menu on an empty selection. I didn't want to rely on [Nemo Actions](https://askubuntu.com/questions/1030940/nautilus-actions-in-18-04) extension (mainly because it is not supported by the version of my current linux distro). So, I created a file at `/usr/share/nemo/actions` and added `vlc %U` as the `Exec` command (`%U` basically means current directory).

It worked perfectly until I tried on a folder which name included a space character. The script was executing `vlc /a folder`, instead of `vlc '/a folder'`. I tried many things to solve this: enclose `%U` in double (and, later, single) quotes, in a `$()` block (which basically means "the result of"), and even using backslashes (escape character). None of it worked.

So I created this Python script. When it's called, it expects the 1st argument to be the program name and the 2nd (and 3rd, 4th, nth) argument(s) to be the additional path arguments to be passed on to the given program. It basically joins ARGVs arguments using a space character and enclose it on quotes. Illustrating:
`python3 app.py vlc /some/place/theres a folder` results in `vlc "/some/place/theres a folder"`.

Originally, the VLC part was static (meaning it only supported VLC and there was no need to provide a first-script-name argument). But then I decided that someone might found it useful and decided to refactor it a little. Well, here we are. I hope you like it!
