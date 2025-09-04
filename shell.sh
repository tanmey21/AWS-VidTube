#!/bin/zsh

echo  "Starting shell script..."
echo "Current directory: $(pwd)"

#Creating the infrastructure
python3 -m src.infrastructure.sns
wait
python3 -m src.infrastructure.sqs_reader
wait
python3 -m src.infrastructure.sqs_writer
wait
echo "Infrastructure created."

#Starting the services
osascript <<EOF
tell application "Terminal"
    do script "echo 'Running in new terminal'; cd 'PycharmProjects/AWS-VidTube'; python3 -m src.sqs_messages.reader"
end tell
EOF

osascript <<EOF
tell application "Terminal"
    do script "echo 'Running in new terminal';cd 'PycharmProjects/AWS-VidTube'; python3 -m src.sqs_messages.writer"
end tell
EOF

