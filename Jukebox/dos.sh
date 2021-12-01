#!/bin/bash
random()
{
 start_time=$1
 end_time=$2
 DIFF=$(($end_time-$start_time+1))
 echo $(($(($RANDOM%$DIFF))+$start_time))
}
start_time=1
end_time=25
RANDOM=$$
cat /home/sans/Desktop/html/users.txt | while read songname creditCardNum
do
 sleep_time=`random $start_time $end_time`
 sleep $sleep_time
 wget "http://localhost:8000/cgi-bin/songlist.py?song=${songname}&creditCardNum=${creditCardNum}"
done
