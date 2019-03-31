#!/usr/bin/env bash

python main.py -orig=./crawler-target/sample-0-origin.html -other=./crawler-target/sample-1-evil-gemini.html
python main.py -orig=./crawler-target/sample-0-origin.html -other=./crawler-target/sample-2-container-and-clone.html
python main.py -orig=./crawler-target/sample-0-origin.html -other=./crawler-target/sample-3-the-escape.html
python main.py -orig=./crawler-target/sample-0-origin.html -other=./crawler-target/sample-4-the-mash.html
