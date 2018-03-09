.PHONY: dissertation_open
open: dissertation.pdf clean
	gnome-open dissertation.pdf

.PHONY: source_open
source_open: sources.pdf clean
	gnome-open sources.pdf

.PHONY: diary_open
diary_open: diary.pdf clean
	gnome-open diary.pdf

.PHONY: clean
clean:
	touch *.tex *.bib
	rm -f *.aux *.log *.toc *.bbl *.blg *.dvi *.lol *.out *.lof

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

diary.pdf: diary.tex
	pdflatex diary.tex
	pdflatex diary.tex
	pdflatex diary.tex
