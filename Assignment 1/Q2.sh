#!/bin/bash
grep . quotes.txt > quotes.temp
file='quotes.temp'
awk '
	{
		n=split($file,a,"~");
		for (i=0;i<=n;i=i+3) 
		{
			print a[i+2] " once said,\"" a[i+1]"\""
		}
	}
' $file > speech.txt
rm quotes.temp
