import os
import json
jsfile = open('2015-01-01-15.json\\2015-01-01-15.json', 'r', encoding = 'utf-8')
actid_set = set()
repid_set = set()
allper_list = []
i = 0
for x in jsfile:
    js_dict = json.loads(x)
    print(js_dict)
    if js_dict['actor']['id'] in actid_set:
            pass
    else:
        actid_set.add(js_dict['actor']['id'])
        person_dict = dict(actor_id = js_dict['actor']['id'], PushEvent = 0, IssueCommentEvent = 0, IssuesEvent = 0, PullRequestEvent = 0 )
        allper_list.append(person_dict)
    if js_dict['type'] == 'PushEvent':
        person_dict['PushEvent'] += 1
    elif js_dict['type'] == 'IssueCommentEvent':
        person_dict['IssueCommentEvent'] += 1
    elif js_dict['type'] == 'IssuesEvent':
        person_dict['IssuesEvent'] += 1
    elif js_dict['type'] == 'PullRequestEvent':
        person_dict['PullRequestEvent'] += 1
# per_id = int(input('请输入你要查询的id：'))
for x in allper_list:
    print(x['actor_id'])
    print(f"PushEvent : {x['PushEvent']}")
    print(f"IssueCommentEvent : {x['IssueCommentEvent']}")
    print(f"IssuesEvent : {x['IssuesEvent']}")
    print(f"PullRequestEvent : {x['PullRequestEvent']}")
jsfile.close()

