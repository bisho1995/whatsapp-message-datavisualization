#!/usr/bin/python3

def format_number(str):
    w = ""
    for ch in str:
        if (ch>='0' and ch<='9') or (ch>='A' and ch<='Z') or (ch >='a' and ch <= 'z') or (ch == ' '):
            w+=ch

    if w.startswith("91"):
        w = w[2:]
    return "'"+w+"'"

def format_msg(msg):
    w=""
    msg = msg.lower()
    for ch in msg:
        _tmp = ord(ch)
        if _tmp < 128:
            if ch >= 'a' and ch <= 'z':
                w+=ch
            else:
                w+=" "
    return w

def process_text_file_to_csv(text_file_name, csv_file_name):
    raw_data = open(text_file_name, 'r')

    output_file = open(csv_file_name, "w")

    output_file.write("Date,Time,Sender,Message\n")

    sender_buf = ""

    for line in raw_data:
        parts = line.split('-')

        buff = ""

        if len(parts) > 1:
            date_raw = parts[0]
            raw_msg = parts[1]
            
            if len(date_raw.split(',')) == 2:
                date, time = list(date_raw.split(','))
                buff = buff +date.strip()+ ","  + time.strip() +","
            else:
                continue

            if len(raw_msg.split(":")) == 2:
                number, msg = list(raw_msg.split(":"))
                if len(number) < 4:
                    continue
                sender = format_number(number.strip())
                msg = format_msg(msg.strip())

                if len(sender) == 2:
                    sender = sender_buf
                if len(sender) == 3:
                    continue

                sender_buf = sender

                buff = buff + sender + "," + msg + "\n"
            else:
                continue
            
            output_file.write(buff)
            
            

        else:
            pass

    output_file.close()

process_text_file_to_csv('data2.txt', 'data2.csv')