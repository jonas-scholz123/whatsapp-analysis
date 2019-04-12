import matplotlib.pyplot as plt
import datetime
import nltk
from nltk.corpus import stopwords

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def word_frequency_analysis(all_words_person1, all_words_person2, stopwords):

    word_count_dict_person1 = {}
    word_count_dict_person2 = {} 

    for word in all_words_person1:
        if word in word_count_dict_person1:
            word_count_dict_person1[word] += 1
        else:
            word_count_dict_person1[word] = 1

    p1_word_count_plot_x = []
    p1_word_count_plot_y = []

    stopwords = stopwords.words('english')
    stopwords.append('the, to, that, but, too, was, get, me, like, not, if, in')
    stopwords = set(stopwords)

    print("the" in stopwords)
    for key in word_count_dict_person1:
        if word_count_dict_person1[key] > 300 and word_count_dict_person1[key] not in stopwords:
            p1_word_count_plot_x.append(key)
            p1_word_count_plot_y.append(word_count_dict_person1[key])

    for word in all_words_person2:
        if word in word_count_dict_person2:
            word_count_dict_person2[word] += 1
        else:
            word_count_dict_person2[word] = 1

    p1_word_count_plot_x = []
    p1_word_count_plot_y = []
    p2_word_count_plot_x = []
    p2_word_count_plot_y = []


    for key in word_count_dict_person2:
        if word_count_dict_person2[key] > 150 and key  not in stopwords:
            p2_word_count_plot_x.append(key)
            p2_word_count_plot_y.append(word_count_dict_person2[key])


    for key in word_count_dict_person1:
        if word_count_dict_person1[key] > 100 and key not in stopwords:
            p1_word_count_plot_x.append(key)
            p1_word_count_plot_y.append(word_count_dict_person2[key])


    print("person1 most used: " ,p1_word_count_plot_x)
    print("person2s most used: ",p2_word_count_plot_x) 

    plt.figure(figsize=(24, 8))
    plt.bar(p1_word_count_plot_x, p1_word_count_plot_y)
    plt.show()

    plt.figure(figsize=(24, 8))
    plt.bar(p2_word_count_plot_x, p2_word_count_plot_y)
    plt.show()
    return

def parser(fpath):
        
    f = open(fpath, "r")
    lines = f.readlines()

    discarded_lines  = []
    valid_lines      = []
    participants     = []
    participant_data = {}

    for line in lines:
        split_line = line.split()
        if len(split_line) < 5:
            discarded_lines.append(split_line)
    #        print("case 1 ", split_line) 
            continue
        if not is_number(split_line[0][0]):
            discarded_lines.append(split_line)
    #        print("case 3 ", split_line) 
            continue
        if not (is_number(split_line[0][1]) or split_line[0][1] == "/"):
            discarded_lines.append(split_line)
    #        print("case 3 ", split_line) 
            continue
        valid_lines.append(split_line)
        date = split_line[0].replace(',', '')
        split_date = date.split("/")
        month = split_date[0]
        day = split_date[1]
        year = split_date[2]
        time = split_line[1]
        split_time = time.split(":")
        hour = split_time[0]
        minute = split_time[1]
        name = split_line[3]
        message = split_line[5:]

        if len(participants) < 2:
            if name not in participants and name != "Messages":
                participants.append(name)
        if name in participants:
            if not name in participant_data:
                participant_data[name] = []
            participant_data[name].append({
                'date': date,
                'datetime_date': datetime.datetime.strptime(date, "%m/%d/%y"),
                'year': year,
                'month': month,
                'day': day,
                'hour': hour,
                'minute': minute,
                'message': message
                })
    return participant_data

def messages_over_time(data, timeframe = "day"):
    messages_per_day = {}
    for message_dict in data:
        if message_dict["datetime_date"] in messages_per_day:
            messages_per_day[message_dict["datetime_date"]] += 1
        else:
            messages_per_day[message_dict["datetime_date"]] = 1
    messages_per_week = {}
    counter = 0
    for date in messages_per_day.keys():
        if counter == 0:
            current_entry = date
            messages_per_week[current_entry] = messages_per_day[date]
            counter += 1
        else:
            messages_per_week[current_entry] += messages_per_day[date]
            counter += 1
            if counter == 7:
                counter = 0

    plt.show()
    if timeframe == "day":
        return messages_per_day
    elif timeframe == "week":
        return messages_per_week
    return

participant_data = parser(fpath = "chat_histories/archive_juan.txt") #TXT FILE FPATH HERE
for p in participant_data.keys():
    msg_vs_time_dict = messages_over_time(participant_data[p])
    ax = plt.subplot(111)
    ax.bar(msg_vs_time_dict.keys(), msg_vs_time_dict.values(),width = 10) #NR OF DAYS PER BAR = width
    ax.xaxis_date()
    plt.xticks(rotation=70)
    plt.title(p)
plt.show()
