import re

def prob_check(user_msg, wordlist_present, single_res=False, keywords=[]):
    msg_occurence = 0
    has_keywords = True
    for word in user_msg:
        if word in wordlist_present:
            msg_occurence += 1

    percentage = float(msg_occurence) / float(len(wordlist_present))

    for word in keywords:
        if word not in user_msg:
            has_keywords= False
            break
    if has_keywords or single_res:
        return int(percentage * 100)
    else:
        return 0

def select_message(message):
    message_prob = {}
    def response(bot_message, word_list, single_res=False, keywords = []):
        nonlocal message_prob
        message_prob[bot_message] = prob_check(message, word_list, single_res, keywords)
    response('Hello', ['hi', 'hey', 'hello'], single_res=True)
    response('i am good', ['how', 'are', 'you'], keywords= ['how'])

    best_res = max(message_prob, key = message_prob.get)
    return best_res



def get_response(user_input):
    message_split = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = select_message(message_split)
    return response


while True:
    print('Bot: ' + get_response(input('You: ')))
