import os 
import json


backup_dir = 'scraped/'
user = '+1234567890'


for source in os.listdir(backup_dir):

    attachments = os.path.join(backup_dir, source, 'attachments')
    
    chatmaps = {}
    for file in os.listdir(os.path.join(backup_dir, source)):
        if file.endswith('.json'):
            with open(os.path.join(backup_dir, source, file), 'r') as f:
                chatmaps[file] = json.load(f)

    for c in chatmaps:

        divs = [

        ]

        for message in chatmaps[c]:


            if message['who'] == user:
                divclass = 'you'
            else:
                divclass = 'notyou'

            if (type(message['value']) == list): # <-- apparently using "type(...) == ..." is frowned upon in python, so be wary of that
                

                for media in message['value']:
                    if type(media) == dict:
                        if media['name'].lower().endswith(('.mov','.mp4','.amv')):
                            val = '<video src="attachments/{}" alt="video"></video>'.format(media['name'])

                        elif media['name'].lower().endswith(('.jpeg','.jpg','.png','.giff','.gif')):
                            val = '<img src="attachments/{}" alt="image" width="100%">'.format(media['name'])

                        divs.append(
                '''
    <div class=.main>
        <p style="font-size: 11px;">{}</p>
        <div class="{}">
            {}
        </div>
    </div>
                '''.format(message['who'], divclass + '_img', val)
                        )

                    else:
                        val = '<p>' + media + '</p>'
                        divs.append(
                '''
    <div class=.main>
        <p style="font-size: 11px;">{}</p>
        <div class="{}">
            {}
        </div>
    </div>
                '''.format(message['who'], divclass, val)
                        )

            else:
                val = '<p>' + message['value'] + '</p>'

                divs.append(
                '''
    <div class=.main>
        <p style="font-size: 11px;">{}</p>
        <div class="{}">
            {}
        </div>
    </div>
                '''.format(message['who'], divclass, val)
                )


        chat = '''
<!DOCTYPE html>
<html>
<head>
    <title>{}</title>
    <style>
        .main {{
        }}
        .main {{

        }}
        .you {{
            background-color: rgb(0, 109, 231);
            color: white;
            border-radius: 10px;
            padding: 1px;
            padding-left: 2%;
            padding-right: 2%;
            margin: 3px;
            margin-left:auto;
            margin-right: 0;
            width: 30%;
        }}
        .notyou {{
            background-color: rgb(220, 220, 220);
            border-radius: 10px;
            padding: 1px;
            padding-left: 2%;
            padding-right: 2%;
            margin: 3px;
            margin-right:auto;
            margin-left: 0;
            width: 30%;
        }}
        .you_img {{
            margin: 3px;
            margin-left:auto;
            margin-right: 0;
            width: 40%;
        }}
        .notyou_img {{
            margin: 3px;
            margin-right:auto;
            margin-left: 0;
            width: 40%;
        }}

    </style>
</head>
<body>
    {}
</body>
</html>
        '''.format(source, '\n'.join(divs))
        with open(os.path.join(backup_dir, source, c + '.html'), 'w') as output:
            output.write(chat)
    


