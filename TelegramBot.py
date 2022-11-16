from html.parser import HTMLParser
import telegram.ext
import telegram

with open("token.txt","r") as f:
    TOKEN = f.read()

def start(update,source):
    update.message.reply_text("<b> Hello, Welcome to My Telegram Page.\nWebSite:/site\nYoutube:/youtube </b>",parse_mode = telegram.ParseMode.HTML)

def site(update,source):
    update.message.reply_text("<b> Web Site:https://www.linkedin.com/ </b>",parse_mode = telegram.ParseMode.HTML)

def video(update,source):
    update.message.reply_text("<b> Youtube:https://https://www.youtube.com </b>",parse_mode = 
telegram.ParseMode.HTML,disable_web_page_preview=True)





update = telegram.ext.Updater(TOKEN,use_context=True)
disp = update.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start",start))

disp.add_handler(telegram.ext.CommandHandler("site",site))

disp.add_handler(telegram.ext.CommandHandler("youtube",video))


update.start_polling()
update.idle()








