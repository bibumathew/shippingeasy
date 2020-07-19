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


##### MakeFile commands

```
usage: make {target}
Available development targets

  install        - install required packages
  clean          - clean python cache
  wpe_merge      - i=<input_file> o=<output_file> input and output csv file
  testall        - run all of the tests
  unittest       - run all of  unit tests
  functionaltest - run all functional tests
```

