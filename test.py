import vk_api, sys, time

def write_msg(user_id, s):
    vk.method('messages.send', {'user_id':user_id,'message':s})


if __name__ == '__main__':
    vk = vk_api.VkApi(login = sys.argv[1],password = sys.argv[2])
    vk.auth()

    msg ="All is ok"
    to_id = 92358050
    # write_msg(to_id,msg)

    values = {'out': 0,'count': 100,'time_offset': 60}
    try:
        ids = {}
        while True:
            resp = vk.method('messages.get',values)
            if resp['items']:
                values["last_message_id"] = resp['items'][0]['id']
            for item in resp['items']:
                # if item[u'user_id'] != 92358050:
                    # write_msg(item[u'user_id'],u'Ty che, ebat?')
                text = item['body']
                if text[:5] == u'Игорь':
                    if item[u'user_id'] not in ids.keys():
                        write_msg(item[u'user_id'],u'О, привет, Я - Игорь, а ты - хуй :-)')
                        ids[item[u'user_id']] = 1
                    elif ids[item[u'user_id']] <= 5:
                        write_msg(item[u'user_id'],u'Ну что ты хочешь?')
                        ids[item[u'user_id']] += 1
                    else:
                        write_msg(item[u'user_id'],u'Да как ты надоел мне,>(( глупый пользователь')
                        ids[item[u'user_id']] = 1
            time.sleep(1)
    except Exception as e:
        print(e.message)
