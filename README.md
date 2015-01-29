# Readme

diff4html is a simple python script for generating a diff between two html files.

## Usage

`diff4html.py [-h] [--del_color DEL_COLOR] [--ins_color INS_COLOR] [--hide_ins] [--hide_del] file_a file_b output`

* `file_a` the "original" file. (usually the oldest of the two)
* `file_b` the "newer" file.
* `output` the diff file to be generated.
* `--ins_color` the color of inserted text. Default: green.
* `--del_color` the color of deleted text Default: red.
* `--hide_ins` if set it will hide all inserted text on the output.
* `--hide_del` if set it will hide all deleted text on the output.

Please note that the output `<head>` contents will be the same as `file_b`'s `<head>`.

### Exemples

* `./diff4html.py -h`
* `./diff4html.py old_version.html new_version.html diff.html`
* `./diff4html.py old_version.html new_version.html diff.html --hide-del`
* `./diff4html.py old_version.html new_version.html diff.html --hide-ins`
* `./diff4html.py old_version.html new_version.html diff.html --hide-ins --del_color #76276C`
* `./diff4html.py old_version.html new_version.html diff.html --del_color #76276C --ins_color #AA8E39`
* `./diff4html.py old_version.html new_version.html diff.html --hide-ins --hide-del`

## Dependencies

* Python 3
* lxml
* argparse

## Installing

Just download and run the script.

You may have to install lxml via `pip install lxml`.


## License

This script is licensed under the MIT License.

Written by Gabriel Queiroz <<gabrieljvnq@gmail.com>>
