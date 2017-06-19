all: nose-intro.html source-html

%.html : %.txt
	rst2html.py $< $@

%.py.html: %.py
	source-highlight -f html $<

source-html: \
	./basic/tests/test_package/__init__.py.html \
	./basic/tests/test_package/submodule2.py.html \
	./basic/tests/test_package/submodule1.py.html \
	./basic/tests/test_package/testmodule1.py.html \
	./basic/tests/test_package/testmodule2.py.html \
	./basic/tests/test_package/test_subpackage/__init__.py.html \
	./basic/tests/test_module.py.html \
	./basic/app_package/__init__.py.html \
	./basic/app_package/stuff.py.html \
	./attr/test_attr.py.html \
	./attr/test_attr2.py.html \
	./multihome/home1/test_in_home1.py.html \
	./multihome/home2/test_in_home2.py.html \
	./simple/tests/test_stuff.py.html
