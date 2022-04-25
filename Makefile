
.PHONY : env
env:
	conda env create -f environment.yml
	conda activate ligo

.PHONY: html
html:
	jupyterbook build .
	
.PHONY: html-build
html-build:
	
		