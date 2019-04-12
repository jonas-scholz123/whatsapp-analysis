# whatsapp-analysis
Python tool to show messages over time in whatsapp

# Use

1.In the whatsapp app go on a particular chat, options, export chat, without media. This is a txt file containing your entire chat history.

2. Save said textfile in a directory of your choosing

3. In the analysis.py file specify the filepath of the textfile at the bottom of the script.

4. The width option at the bottom of the file specifies the timeframe (nr of days) that go into one bar in the graph.

5. The word_frequency_analysis() function is at this stage not great.

6. The parser works well and can be used for more analysis than messages_over_time().
