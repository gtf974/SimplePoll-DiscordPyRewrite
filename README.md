# DiscordPy SimplePoll Command

# How to use it  

###### In your *Bot/Cog file*:
* Simply paste the command in your bot file; indented just like the other commands.

###### On *Discord*:
* Type `<YOURPREFIX>poll <"Question"> <"Answer1"> <"Answer2"> ... <"Answer9">`
* For example: `,poll "What's your favorite fruit ?" "Oranges" "Mangos" "Strawberries" "Pineapple" "Peaches"`  
* Don't forget the quote marks for each parameter : "Oranges" not Oranges, "What's your favorite fruit ?" not What's your favorite fruit ?

###### /!\ You can go up to 9 answers but you must have at least 2 answers.

###### How it works:
* When you type in your command, the bot embeds your question and your answers. Then, it will react from 1 to the number of your answers. Finally it will delete your message.
* The execution time is about 4 seconds for a poll with 9 answers (Tested on a bot with 100ms of latency)

# BOT PERMISSIONS    
* embed_links  
* read_messages  
* send_messages



You can contact me for further explanations on Discord: Idotcom#2197
