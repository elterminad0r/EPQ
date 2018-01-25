diary.html: diary.csv make_table.py
	python make_table.py diary.csv -o diary.html

.PHONY: view
view:
	make diary.html
	firefox diary.html
