import json

# debugger
# set break point

def get_emails(names):
    print(f'* Getting emails for {names}')

    address_book = {
        'Spock': 'spock@example.com',
        'Picard': 'picard@example.com',
        'Kirk': 'kirk@example.com',
        'Sisko': 'sisko@example.com'
    }

    emails = {}

    for name in names:
        emails[name] = address_book[name]

    return emails

# ['Kirk', 'Spock', 'Picard']
# get_emails(['Kirk', 'Spock', 'Picard'])

#['kirk@example.com', 'spock@example.com']

def schedule_meeting(subject, recipients, time):
    print(f"* Meeting '{subject}' scheduled for {time} with {recipients}")
    return {'success': True}


def process_function_call(function_call):
    name = function_call['name']
    args = function_call['args']

    functions = {
        'get_emails': get_emails,
        'schedule_meeting': schedule_meeting,
    }

    return functions[name](**args)


'''
# Test get_emails
print("~Test get_emails~")
name_list = ['Kirk']
print(get_emails(name_list))
print("---------------")
print()


# Test schedule_meeting
print("~Test schedule_meeting~")
subject = "Star Trek"
recipient = "Kirk"
time = "Monday at noon"
schedule_meeting(subject, recipient, time)
print("---------------")
print()

'''
# Test process_function_call
print("~Test process_function_call~")

content_string1 = "{ \"name\": \"get_emails\", \"args\": { \"names\": [\"Sisko\"] } }"
function_call = json.loads(content_string1)
result = process_function_call(function_call)

print(result)


print("---------------")
print()

content_string2 = '{ "name": "schedule_meeting", "args": { "subject": "Meeting in HMB", "recipients": ["sisko@example.com"], "time": "Monday" } }'
function_call = json.loads(content_string2)
result = process_function_call(function_call)

print("---------------")