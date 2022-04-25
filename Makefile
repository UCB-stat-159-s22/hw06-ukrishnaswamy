
.PHONY : env
env:
	conda env create -f environment.yml
	conda activate ligo

.PHONY: html
html:
	jupyterbook build .
	
	
.PHONY: html-build
html-build:
	jupyter-book config sphinx .
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
	@echo "Start the Python http server and visit:"
	python -m http.server
	@echo "https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html"
	
	