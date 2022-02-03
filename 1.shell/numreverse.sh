#!/usr/bin/env bash

if [ -z $1 ] || [ $1 -lt 0 ]
then
	echo "Usage: ./numreverse.sh <number>"
	echo "	<number> must be a number greater than or equal to 0."
	echo "Example:"
	echo "./numreverse.sh 12345"
	echo "54321"
	echo
	exit 1
fi

num=$1  # original number
rev=""  # reversed number

while [ $num -ne 0 ]
do
	ones=$(( $num % 10 ))  # get the one's digit
	num=$(( $num / 10 ))  # remove the one's digit
	rev=$rev$ones
done

echo $rev
