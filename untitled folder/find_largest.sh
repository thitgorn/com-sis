#/bin/bash
curl http://www.textfiles.com/etext/FICTION/ > FICTION.txt
grep -o -E '<TD> [0-9]*<BR>' FICTION.txt > 1.txt
grep -o -E ' [0-9]*' 1.txt > 2.txt
cut -c 2- 2.txt > size.txt

while read size; do
	if [ $size -gt 266909 ] ; then
		grep $size FICTION.txt >> output.txt
		((count++)); fi
done < size.txt

while read result; do
	echo $result > temp.txt
	echo "Name"
	grep -o -E '"[A-Za-z0-9].*"' temp.txt > temp1.txt
	cut -c 2- temp1.txt > temp2.txt
	cat temp2.txt; x=$(cat temp2.txt)
	echo "Descriptions"
	grep -o -E "<BR><TD> [A-Za-z0-9 ,.():;/-\/']*" temp.txt | cut -c 10-
	echo "Link"
	echo "http://www.textfiles.com/etext/FICTION/$x"
	echo "------------------------------"
done < output.txt
