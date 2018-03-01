.PHONY: open
open: dissertation.pdf
	gnome-open dissertation.pdf

.PHONY: source_open
source_open: sources.pdf
	gnome-open sources.pdf

dissertation.pdf: dissertation.tex sources.bib
	pdflatex dissertation.tex
	pdflatex dissertation.tex
	bibtex dissertation
	pdflatex dissertation.tex

sources.pdf: sources.tex sources.bib
	pdflatex sources.tex
	pdflatex sources.tex
	bibtex sources
	pdflatex sources.tex
    
