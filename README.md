# image-to-ascii
The ASCII output is intended for viewing in Python's IDLE! I can't guarantee it will be as pretty anywhere else.

## dependencies

All you need is Python and IDLE. If you don't have one or both, try:

`brew install python`
and/or
`brew install idle`.

Alternatively, [download Python](https://www.python.org/downloads/).

Linux: `apt-get install python idle`

## usage

Once you're in IDLE, open `image_to_ascii.py` and run the script (`<F5>`).

IDLE will ask you to input a URI as `raw_text` (no need for quotes) and will start working.

Some URIs:

* `http://goo.gl/UcP4Dx`
* `/home/username/Downloads/hotpants.png`
* `http://goo.gl/QrYTNC`

### Notes

* High contrast works best.
* Be wary of large images. When the source has a height and width in the thousands of pixels, you will have to do a lot of `zout`s before you can see anything.
* You can adjust the default zoom in the script.
<hr>

#### TODO

* Obviously, the spectrum could be cleaner and less dependent on IDLE

* Save file names

* Export a pixel-ey grayscale image

* Make more practical use of `clock()`

* Consider a switch over `if`, `elif`, `elif`, and so on

* &c.
