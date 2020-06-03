#!/bin/bash

./bash/server.sh -D
status=$?

if [ $status -ne 0 ]; then
  echo "Failed to start server: $status"
  exit $status
else
  echo "Server started successfully"
fi

./bash/cron.sh -D
status=$?

if [ $status -ne 0 ]; then
  echo "Failed to start cron: $status"
  exit $status
else
  echo "Cron started successfully"
fi

while sleep 60; do
  ps aux |grep gunicorn |grep -q -v grep
  PROCESS_1_STATUS=$?
  ps aux |grep cron |grep -q -v grep
  PROCESS_2_STATUS=$?

  if [ $PROCESS_1_STATUS -ne 0 -o $PROCESS_2_STATUS -ne 0 ]; then
    echo "One of the processes has already exited."
    echo "Server is: $PROCESS_1_STATUS"
    echo "Cron is: $PROCESS_2_STATUS"
    exit 1
  fi
done
