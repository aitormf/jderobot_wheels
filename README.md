# Make Wheels

## Depencencies

<pre>
pip3 install wheel
</pre>

## Create

<pre>
	python setup.py sdist bdist_wheel
</pre>

more info in: [http://pythonwheels.com/](http://pythonwheels.com/)


## Make Jderobot python interfaces windows:
with cmd go to jderobot slice files directory
<pre>python -m slice2py

for /f %f in ('dir /b .\*.ice')do slice2py -I.. --all --output-dir dest %f
</pre>