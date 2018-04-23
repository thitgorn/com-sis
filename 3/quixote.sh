#/bin/bash
curl http://www.textfiles.com/etext/FICTION/quixote > quixote.txt
sed -i '' 's/[tT][hH][aA][tT]/tthat/g' quixote.txt
grep 'tthat' quixote.txt -wc

grep -o -e '^[aA][cC][a-zA-Z]*[dD]' quixote.txt
grep -o -e '^[aA][cC][a-zA-Z]*[dD]' quixote.txt -wc
