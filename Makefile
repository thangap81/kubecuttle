# vim: set noet sw=4 ts=4 fileencoding=utf-8:

# External utilities
PYTHON=python3
PIP=pip3
MKDOCS=mkdocs
PYFLAGS=
DEST_DIR=/


# Default target
all:
	@echo "make install - Install on local system"
	@echo "make doc - Generate HTML and PDF documentation"
	
install: $(SUBDIRS)
	$(PYTHON) $(PYFLAGS) setup.py install --root $(DEST_DIR)

doc:
	$(MKDOCS) build
