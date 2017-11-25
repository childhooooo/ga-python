
from fastpass import Fastpass

class Attraction(object):

    def __init__(self, name, value, latency, fastpass):
        self.__name = name
        self.__value = value
        self.__fastpass = fastpass
        self.__latency = latency


    def ride(self, guest):
        latency = 20 # To ride attraction takes 20 minutes at least

        now = guest.now()
        hasFastpass = self.__analize_tickets(guest.showTickets(), now)

        if(hasFastpass):
            latency += 10
        elif(now < 840):
            latency += self.__latency[now//30]
        else:
            latency = 0

        if((now + latency) > 780):
            value = 0
        else:
            value = self.__value

        return [latency, value]


    def ticket(self, guest):
        latency = 10
        now = guest.now()
        last = guest.lastTimeGotTicket()
        ticket = Fastpass(self.__name)

        if((now - last) > 120 and now < 840):
            lower = self.__fastpass[now//30]
            if(lower == 0):
                ticket.disable()
            ticket.setTime(lower)
        else:
            ticket.disable()

        return [latency, ticket]


    def __analize_tickets(self, tickets, time):
        for t in tickets:
            if(t.getName() == self.__name and t.isAvailable() and t.isInTime(time)):
                return True

        return False

