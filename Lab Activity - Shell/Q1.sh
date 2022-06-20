multiply=`expr $1 \* $2`
if [ $# -eq 2 ];
then
	echo $multiply
else  
	echo "Error: Wrong number of arguments"
fi
