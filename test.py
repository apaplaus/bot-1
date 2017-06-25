import vk_api, sys


vk = vk_api.VkApi(login = sys.argv[1],password = sys.argv[2])
vk.auth()

print("Hello!")
