#!/usr/bin/env bash

if [ -z $1 ] || [ $1 -lt 0 ]
then
	echo "Usage: ./sumupto.sh <number>"
	echo "	<number> must be a number greater than or equal to 0."
	echo "Example:"
	echo "./sumupto.sh 5"
	echo "15"
	echo
	exit 1
fi

num=$1  # original number
total=0  # sum accumulator

for ((i=0; i<=$num; i++))
do
	total=$(( $total + $i ))
done

echo $total
