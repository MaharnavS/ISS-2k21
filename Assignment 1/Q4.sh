#!/bin/bash
echo "Enter the Array as CSV"
read -p "-> " in
in="${in//,/ }"
read -a array <<< $in
len=${#array[*]}
for((i=0 ; i<$len ; i++))
do
{
	for((j=0 ; j<$len-i-1 ; j++))
	do
	{
		if [ "${array[$j]}" -gt "${array[$((j+1))]}" ]
		then
		{
			temp=${array[$j]}
			array[$j]=${array[$((j+1))]}
			array[$j+1]=$temp
		}
		fi
	}
	done
}
done
echo -e "Sorted Array is :"
echo ${array[*]}
