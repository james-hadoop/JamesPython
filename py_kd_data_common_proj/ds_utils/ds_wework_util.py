import requests
import json


class WeWorkUtil(object):
    corpid = 'wxab249edd27d57738'
    secret = 'zbYzspY7eDRpmr9DMzKK2yp21-BjaxjtQFvJuS91V4g'

    @staticmethod
    def get_access_token():
        data = {
            'corpid': WeWorkUtil.corpid,
            'corpsecret': WeWorkUtil.secret,
        }
        R = requests.get(url='http://in.qyapi.weixin.qq.com/cgi-bin/gettoken',
                         params=data, timeout=5)
        return R.json().get('access_token', '')

    @staticmethod
    def create_chat(name, userlist):
        access_token = WeWorkUtil.get_access_token()
        data = json.dumps({
            'name': name,
            'userlist': userlist
        })
        R = requests.post(url='http://in.qyapi.weixin.qq.com/cgi-bin/tencent/chat/create?access_token=' + access_token,
                          data=data, timeout=5)
        print(R.text)
        return R.json().get('chatid', '')

    @staticmethod
    def modify_chat(chatid, add_user_list=[], del_list=[]):
        try:
            access_token = WeWorkUtil.get_access_token()
            user_list = WeWorkUtil.get_userid(add_user_list)
            data = json.dumps({
                'chatid': chatid,
                'add_user_list': user_list,
                'del_user_list': del_list
            })
            R = requests.post(
                url='http://in.qyapi.weixin.qq.com/cgi-bin/tencent/chat/update?access_token=' + access_token,
                data=data, timeout=5)
            print(R.text)
            return R.text
        except Exception as e:
            return {'msg': 'add user_list wework fail'}

    @staticmethod
    def send_message(chatid, content, mentioned_list=[], type='group', ):
        try:
            access_token = WeWorkUtil.get_access_token()
            user_list = WeWorkUtil.get_userid(mentioned_list)
            data = json.dumps({
                "receiver": {
                    "type": type,
                    "id": chatid,
                },
                "msgtype": "rich_text",
                "rich_text": [{
                    "type": "mentioned",
                    "mentioned": {
                        "userlist": user_list
                    }
                },
                    {
                        "type": "text",
                        "text": {
                            "content": content
                        }
                    }
                ]
            })
            R = requests.post(
                url='http://in.qyapi.weixin.qq.com/cgi-bin/tencent/chat/send?access_token=' + access_token,
                data=data, timeout=5)
            print(R.text)
            return R.text
        except Exception as e:
            return {'msg': 'send message fail'}

    @staticmethod
    def get_userid(rtx_list):
        ret = []
        try:
            access_token = WeWorkUtil.get_access_token()
            data = json.dumps({
                "name_list": rtx_list
            })
            R = requests.post(
                url='http://in.qyapi.weixin.qq.com/cgi-bin/tencent/user/convert_to_userid?access_token=' + access_token,
                data=data)
            user_list = R.json().get('user_list', '')
            for user in user_list:
                ret.append(user.get('userid'))
            return ret
        except Exception as e:
            return {'msg': 'get userid fail'}
