FORCE:

%.view: %.eps FORCE
	gv $<

%.ghost%: %.eps FORCE
	gs $<

%.eps: %.ps
	ps2eps -f $<

hadamard_%.ps: %.fake ../src/generate_ham_vis.py
	python ../src/generate_ham_vis.py $* --dump $@

%.fake:
	echo fake made target $@
