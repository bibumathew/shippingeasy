#### Pre Requirements

```
Install python 3.6 or greater
Install pip

Install virtualenv
pip install virtualenv

```


#### *Installation and virtual environment Wrapper*
*To clone the application and create the virtualenv.*
```
cd /path/to/workspace
clone the application to your workspace

# virtual env
virtualenv -p python3 venv
source venv/bin/activate
```

##### Docs
```/docs/build/html/index.html```

*command to install the necessary packages*
```
make clean install
```

*command to run the merge script* 
```
make wpe_merge i=<input-csv-file-path> o=<ouput-csv-file-path>
```

*Command to run all tests*
```
make testall
```

*command to run all unit test*
```
make unittest
```

*command to run all functional test*
```
make functionaltest
```
