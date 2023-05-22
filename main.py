import telebot
import pysndfx
import os
import BotInfo

bot = telebot.TeleBot(BotInfo.TOKEN)
infile = "audio.wav"
outfile = "output.wav"


@bot.message_handler(commands=['start'])
def on_message(message):
    bot.send_message(message.chat.id, BotInfo.START_MESSAGE)


# test f
@bot.message_handler(content_types=['document', 'audio'])
def get_file(message):
    try:
        match message.content_type:
            case 'audio':
                file_info = bot.get_file(message.audio.file_id)
            case 'document':
                file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(infile, "wb") as f:
            f.write(downloaded_file)
            bot.send_message(message.chat.id, "Готово! Аудиофайл готов к обработке.")
    except Exception as e:
        print(str(e))
        bot.send_message(message.chat.id, "Произошла ошибка в ходе загрузки файла")


@bot.message_handler(commands=['reverb', 'speed', 'normalize', 'pitch', 'bandpass', 'tempo'])
def commands_handler(message):
    fx = pysndfx.AudioEffectsChain()
    args = message.text.split()[0:]
    match args[0]:
        case '/reverb':
            fx.reverb(reverberance=args[1], hf_damping=args[2], room_scale=args[3], stereo_depth=args[4],
                      pre_delay=args[5], wet_gain=args[6])
        case '/speed':
            fx.speed(float(args[1]))
        case '/normalize':
            fx.normalize()
        case '/pitch':
            fx.pitch(int(args[1]) * 100)
        case '/bandpass':
            fx.bandpass(args[2], args[3])
        case '/tempo':
            fx.tempo(float(args[1]))
    fx(infile, outfile)
    with open(outfile, 'rb') as f1:
        bot.send_audio(message.chat.id, f1)
    os.remove(outfile)
    os.remove(infile)


bot.polling(non_stop=True)
