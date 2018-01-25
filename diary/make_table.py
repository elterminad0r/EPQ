"""
Format the diary tsv file
"""

import csv
import argparse
import tabulate
import textwrap

from bs4 import BeautifulSoup as bs

generic_docu = """\
<?doctype HTML>
<html lang="en">
	<head>
        <meta charset="utf-8"/>
		<style>{style}</style>
	</head>
	<body>
		<table>
			<thead>{thead}</thead>
			<tbody>{tbody}</tbody>
		</table>
	</body>
</html>"""

# adapted from http://cssmenumaker.com/blog/stylish-css-tables-tutorial/

generic_style = """\
table {  
    color: #333;
    font-family: Helvetica, Arial, sans-serif;
    width: 100%;
    border-collapse: 
    collapse; border-spacing: 0; 
    empty-cells: show;
}

td, th {  
    border: 1px solid transparent; /* No more visible border */
    height: 30px; 
    transition: all 0.3s;  /* Simple transition for hover effect */
}

th {  
    background: #DFDFDF;  /* Darken header a bit */
    font-weight: bold;
}

td {  
    background: #FAFAFA;
    text-align: center;
    padding: 15px;
}

/* Cells in even rows (2,4,6...) are one color */        
tr:nth-child(even) td { background: #F1F1F1; }   

/* Cells in odd rows (1,3,5...) are another (excludes header cells)  */        
tr:nth-child(odd) td { background: #FEFEFE; }  

tr td:hover { background: #666; color: #FFF; }  
/* Hover cell effect! */
"""

def get_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=argparse.FileType("r"))
    parser.add_argument("-o", "--output", type=argparse.FileType("w"))
    return parser.parse_args()

def get_diary(diary):
    with diary:
        return list(csv.reader(diary))

def get_htmltab(heads, data):
    return bs(generic_docu.format(style=generic_style,
                      thead="".join("<th>{}</th>".format(h) for h in heads),
                      tbody="".join("<tr>{}</tr>".format(
                                "".join("<td>{}</td>".format(d) for d in datum))
                                        for datum in data)),
              "html.parser").prettify()

if __name__ == "__main__":
    args = get_args()
    head, *data = get_diary(args.input)
    args.output.write(get_htmltab(head, data))
