#/bin/bash

DIRECTORY='http://www.textfiles.com/etext/FICTION/'

curl $DIRECTORY > FICTION.txt
grep -o -E '<A HREF="[a-zA-Z0-9]*.txt' FICTION.txt > raw.txt
cut -c 10- raw.txt > url.txt

touch allbooks.txt

while read url; do
    curl $DIRECTORY$url >> allbooks.txt
done < url.txt


