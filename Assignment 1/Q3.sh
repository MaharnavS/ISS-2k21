#!/bin/bash
size=$(wc --bytes < $1)
echo "Size of file is $size Bytes" 
lines=$(wc --lines < $1)
echo "No of lines is $lines"
words=$(wc --words < $1)
echo "No of words is $words"
count=0
while read line 
do 
	line_word=$(echo $line | wc -w)
	echo "Line No: $count - Count of Words: $line_word"
	let count=$count+1
done < $1
grep -wo '[[:alnum:]]\+' $1 | sort | uniq -d -c | awk '{print "Word: " $2 " - Count of repitition: " $1}'
