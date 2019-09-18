#!/bin/bash
month=$1
day=$2
for year in {1998..2100}; do
    week=$(cal $month $year | grep $day)
    count=0
    for i in $week; do
        if [ $i = $day  ]; then
            break
        fi
        let "count +=1"
    done
    DOW=(Sunday Monday Tuesday Wednesday Thursday Friday Saturday)
    #echo "Year: $year Day of week: ${DOW[$count]}"
    echo ${DOW[$count]}
done
