#!/usr/bin/env python3

import argparse
import lxml
import lxml.html.diff


def get_raw_diff(file_a, file_b):
    return lxml.html.diff.htmldiff(file_a, file_b)

def diff_files(file_a, file_b, ins_color='#c70606', del_color='#57b205', hide_ins=False, hide_del=False):

    # Process diff
    raw_diff = get_raw_diff(file_a, file_b)

    # Generate css
    css = ""
    if hide_ins == False:
        css += "ins, ins a {"
        css += "  color: "+ins_color+";"
        css += "}"
        css += "ins {"
        css += "  text-decoration: none;"
        css += "}"
    else:
        css += "ins {"
        css += "  display: none;"
        css += "}"
    if hide_del == False:
        css += "del {"
        css += "  color: "+del_color+";"
        css += "  text-decoration: line-through;"
        css += "}"
        css += "del a, del a:visited {"
        css += "  color: "+del_color+";"
        css += "  text-decoration: line-through underline;"
        css += "}"
    else:
        css += "del {"
        css += "  display: none;"
        css += "}"
    css_tag = lxml.etree.XML("<style>"+css+"</style>")

    # Get head and insert css
    head = lxml.html.fromstring(file_b).head
    head.append(css_tag)
    head_str = lxml.html.tostring(head)

    # Generate output
    return '<html>'+head_str.decode("utf-8")+'<body>'+raw_diff+'</body></html>'

def main():
    # Prepare parser
    parser = argparse.ArgumentParser(
        description='Show diferences between two html files.')
    parser.add_argument('file_a', metavar='file_a', type=str, nargs=1,
        help='an HTML file')
    parser.add_argument('file_b', metavar='file_b', type=str, nargs=1,
        help='an HTML file')
    parser.add_argument('output', metavar='output', type=str, nargs=1,
        help='the HTML output')
    parser.add_argument('--del_color', type=str, default='#c70606',
        help='the deleted text color in hex rgb format')
    parser.add_argument('--ins_color', type=str, default='#57b205',
        help='the inserted text color in hex rgb format')
    parser.add_argument('--hide_ins', action="store_true", default=False,
        help='hide the inserted text')
    parser.add_argument('--hide_del', action="store_true", default=False,
        help='hide the deleted text')
    args = parser.parse_args()

    # Open files
    file_a = open(args.file_a[0], 'r').read()
    file_b = open(args.file_b[0], 'r').read()
    file_c = open(args.output[0], 'w')

    # Process
    output = diff_files(file_a, file_b, ins_color=args.ins_color,
        del_color=args.del_color, hide_del=args.hide_del, hide_ins=args.hide_ins)

    # Save
    file_c.write(output)



if __name__ == "__main__":
    main()