build/talk.pdf: talk.latex
	pdflatex -shell-escape -output-directory build/ talk.latex
