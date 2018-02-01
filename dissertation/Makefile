.PHONY: open
open: dissertation.pdf
	gnome-open dissertation.pdf

dissertation.pdf: dissertation.tex sources.bib
	pdflatex dissertation.tex
	pdflatex dissertation.tex
	bibtex dissertation
	pdflatex dissertation.tex
