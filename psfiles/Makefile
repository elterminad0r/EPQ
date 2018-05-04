.PHONY: view ghost
view: hamming_visualisation.eps
	gv hamming_visualisation.eps

ghost:
	gs hamming_visualisation.ps

hamming_visualisation.eps: hamming_visualisation.ps routines.ps
	ps2eps -f hamming_visualisation.ps
