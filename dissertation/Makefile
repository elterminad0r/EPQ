.PHONY: open
open: dissertation.pdf
	gnome-open dissertation.pdf

.PHONY: clean
clean:
	touch *.tex *.bib
	rm *.aux *.bbl

.PHONY: source_open
source_open: sources.pdf
	gnome-open sources.pdf

dissertation.pdf: dissertation.tex sources.bib $(wildcard ../src/*.py)
	pdflatex dissertation.tex
	pdflatex dissertation.tex
	bibtex dissertation
	pdflatex dissertation.tex
	bibtex dissertation
	pdflatex dissertation.tex

sources.pdf: sources.tex sources.bib
	pdflatex sources.tex
	pdflatex sources.tex
	bibtex sources
	pdflatex sources.tex
	bibtex sources
	pdflatex sources.tex
