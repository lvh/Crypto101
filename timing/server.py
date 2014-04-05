import random
import string
import sys

from twisted.internet import reactor
from twisted.manhole import telnet
from twisted.python import log

alphabet = string.ascii_letters + string.digits + "?!.;:*+"
length = random.randrange(10, 20)
password = "".join(random.choice(alphabet) for _ in xrange(length))

factory = telnet.ShellFactory()
factory.password = password

log.startLogging(sys.stdout)
log.msg("Password: {}".format(password))

reactor.listenTCP(9999, factory)
reactor.run()
