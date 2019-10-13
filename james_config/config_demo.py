import configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {'ServerAliveInterval': '45', 'Compression': 'yes', 'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'james'
config['bitbucket.org']['Password'] = 'password'

topsecret = config['topsecret.server.com'] = {}
topsecret['Host Port'] = '50022'
topsecret['ForwardX11'] = 'no'

config['DEFAULT']['ForwardX11'] = 'yes'

with open('james_config.ini', 'w') as configfile:
    config.write(configfile)

config.read('james_config.ini')
print(config['bitbucket.org']['User'])
print(config['DEFAULT']['Compression'])

# print(config.defaults())

for key in config['bitbucket.org']:
    print('%s -> %s' % (key, config['bitbucket.org'][key]))

config.set('bitbucket.org','user','jj')

with open('james_config.ini', 'w') as configfile:
    config.write(configfile)