from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink


def MyNetwork():
    net = Mininet(topo=None, build=False, ipBase='192.168.1.0/24', link=TCLink)

    info("*** Creating Network")
    print("")
    print("")

    info("*** Adding Controller 1 and Controller 2")
    print("")
    print("")
    # add Controller 1
    c1 = net.addController(name='Controller1',
                           controller=RemoteController,
                           ip='192.168.56.101',
                           port=6633)

    # add Controller 2
    c2 = net.addController(name='Controller2',
                           controller=RemoteController,
                           ip='192.168.56.102',
                           port=6634)

    info("*** Adding four switch")
    print("")
    # add switch
    switch1 = net.addSwitch('switch1')
    switch2 = net.addSwitch('switch2')
    switch3 = net.addSwitch('switch3')
    switch4 = net.addSwitch('switch4')
    print("(switch1,switch2,switch3,switch4)")
    print("")

    # add host
    host1 = net.addHost('h1', ip='192.168.1.1')
    host2 = net.addHost('h2', ip='192.168.1.2')
    host3 = net.addHost('h3', ip='192.168.1.3')
    host4 = net.addHost('h4', ip='192.168.1.4')
    host5 = net.addHost('h5', ip='192.168.1.5')
    host6 = net.addHost('h6', ip='192.168.1.6')
    host7 = net.addHost('h7', ip='192.168.1.7')
    host8 = net.addHost('h8', ip='192.168.1.8')

    # add link
    net.addLink(host1, switch1)
    net.addLink(host2, switch1)
    net.addLink(host3, switch2)
    net.addLink(host4, switch2)
    net.addLink(host5, switch3)
    net.addLink(host6, switch3)
    net.addLink(host7, switch4)
    net.addLink(host8, switch4)

    net.addLink(switch1, switch2)
    net.addLink(switch2, switch3)
    net.addLink(switch3, switch4)

    net.build()

    for controller in net.controllers:
        controller.start()

    net.get('switch1').start([c1,c2])
    net.get('switch2').start([c1,c2])
    net.get('switch3').start([c2,c1])
    net.get('switch4').start([c2,c1])

    print("")

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    MyNetwork()
