from datetime import datetime

class Call(object):
    NUM_CALLS = 0
    def __init__(self, caller, phone_num, reason):
        self.caller = caller
        self.phone_num = phone_num
        self.time_of_call = datetime.now()
        self.reason = reason
        self.id = Call.NUM_CALLS
        
        Call.NUM_CALLS += 1
    
    def display(self):
        print "Call ID: {}".format(self.id)
        print "Caller Name: {}".format(self.caller)
        print "Caller Phone: {}".format(self.phone_num)
        print "Time of Call: {}".format(self.time_of_call)
        print "Reason for Call: {}".format(self.reason)
        return self


class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = self.get_queue_size()

    def get_queue_size(self):
        return len(self.calls)
       

    def add(self, call):
        self.calls.append(call)
        return self

    def remove(self, call):
        self.calls.remove(call)
        return self 

    def info(self):
        for call in self.calls:
            call.display()
        

#add 2 calls by mike and denise
call1 = Call("Mike", "9171234567", "Refund")
call2 = Call ("Denise", "2125436742", "Customer Support")

#create att call center and add the 2 calls from mike and denise
att = CallCenter()
att.add(call1).add(call2)

#remove call 2 and display all calls in call center att
att.remove(call1)
att.info()


