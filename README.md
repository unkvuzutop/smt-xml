### Simple element searcher in Html documents. 

Tested  with  Python 3.7


## Usage:
- Install requirement.  
```bash
pip install -r requirements.txt

```
- Run one of the following command.  (Paths to files can be different(not just relative) 
I just put everything to one folder
```bash
python main.py -orig=./crawler-target/sample-0-origin.html -other=./crawler-target/sample-1-evil-gemini.html
python main.py -orig=./crawler-target/sample-0-origin.html -other=./crawler-target/sample-2-container-and-clone.html
python main.py -orig=./crawler-target/sample-0-origin.html -other=./crawler-target/sample-3-the-escape.html
python main.py -orig=./crawler-target/sample-0-origin.html -other=./crawler-target/sample-4-the-mash.html

```
OR just run simple shell script with all test commands.
```bash
 sh run.sh 
```



-----------
RESULTS:
```
(proj_env_2) ➜  smt-xml git:(master) ✗ sh run.sh                     
2019-03-31 08:28:03,785 - __main__ - INFO - PROCESS file_name ./crawler-target/sample-1-evil-gemini.html
2019-03-31 08:28:03,787 - __main__ - INFO - Get info about element with ID = make-everything-ok-button
2019-03-31 08:28:03,788 - __main__ - INFO - Found by class_name ||=>> btn btn-success
2019-03-31 08:28:03,788 - __main__ - INFO - Path to founded element||=>> /html/body/div/nav/ul/li[1]/ul/li[7]/a
2019-03-31 08:28:03,789 - __main__ - INFO - <--END-->
2019-03-31 08:28:03,859 - __main__ - INFO - PROCESS file_name ./crawler-target/sample-2-container-and-clone.html
2019-03-31 08:28:03,861 - __main__ - INFO - Get info about element with ID = make-everything-ok-button
2019-03-31 08:28:03,862 - __main__ - INFO - found by text [<Element a at 0x107ee0a08>, <Element a at 0x107ee0a88>]
2019-03-31 08:28:03,862 - __main__ - INFO - Found by parent block class ||==> col-lg-8
2019-03-31 08:28:03,862 - __main__ - INFO - Path to founded element||=>> /html/body/div/div/div[3]/div[1]/div/div[2]/div/a
2019-03-31 08:28:03,862 - __main__ - INFO - <--END-->
2019-03-31 08:28:03,933 - __main__ - INFO - PROCESS file_name ./crawler-target/sample-3-the-escape.html
2019-03-31 08:28:03,936 - __main__ - INFO - Get info about element with ID = make-everything-ok-button
2019-03-31 08:28:03,936 - __main__ - INFO - Found by class_name ||=>> btn btn-success
2019-03-31 08:28:03,936 - __main__ - INFO - Path to founded element||=>> /html/body/div/div/div[3]/div[1]/div/div[3]/a
2019-03-31 08:28:03,936 - __main__ - INFO - <--END-->
2019-03-31 08:28:04,007 - __main__ - INFO - PROCESS file_name ./crawler-target/sample-4-the-mash.html
2019-03-31 08:28:04,010 - __main__ - INFO - Get info about element with ID = make-everything-ok-button
2019-03-31 08:28:04,010 - __main__ - INFO - Found by class_name ||=>> btn btn-success
2019-03-31 08:28:04,010 - __main__ - INFO - Path to founded element||=>> /html/body/div/div/div[3]/div[1]/div/div[3]/a
2019-03-31 08:28:04,010 - __main__ - INFO - <--END-->


```


Script can take addition  parameter ```--el``` for changing target element in original file.
