#!/bin/bash
echo -n "Enter string: "
read string
strlen=${#string}
for (( i=$strlen-1; i>=0; i-- ));
do
    revstr=$revstr${string:$i:1}
done
echo "Reversed String : $revstr"

for (( i=0; i<$strlen; i++ ));
do
    substr=$substr${revstr:$i:1}
done
echo "Reversed String with subsequent letters : $substr"

for (( i=$strlen/2-1; i>=0; i-- ));
do
    halfrev=$halfrev${string:$i:1}
done
for (( i=$strlen/2; i<$strlen; i++ ));
do
    halfrev=$halfrev${string:$i:1}
done
echo "Half string in reverse : $halfrev"
