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

    info("*** Adding 32 switch")
    print("")
    # add switch
    switch1 = net.addSwitch('switch1')
    switch2 = net.addSwitch('switch2')
    switch3 = net.addSwitch('switch3')
    switch4 = net.addSwitch('switch4')
    switch5 = net.addSwitch('switch5')
    switch6 = net.addSwitch('switch6')
    switch7 = net.addSwitch('switch7')
    switch8 = net.addSwitch('switch8')


    print("(8 switch)")
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
    host9 = net.addHost('h9', ip='192.168.1.9')
    host10 = net.addHost('h10', ip='192.168.1.10')
    host11 = net.addHost('h11', ip='192.168.1.11')
    host12 = net.addHost('h12', ip='192.168.1.12')
    host13 = net.addHost('h13', ip='192.168.1.13')
    host14 = net.addHost('h14', ip='192.168.1.14')
    host15 = net.addHost('h15', ip='192.168.1.15')
    host16 = net.addHost('h16', ip='192.168.1.16')


    # add link
    net.addLink(host1, switch1)
    net.addLink(host2, switch1)
    net.addLink(host3, switch2)
    net.addLink(host4, switch2)
    net.addLink(host5, switch3)
    net.addLink(host6, switch3)
    net.addLink(host7, switch4)
    net.addLink(host8, switch4)
    net.addLink(host9, switch5)
    net.addLink(host10, switch5)
    net.addLink(host11, switch6)
    net.addLink(host12, switch6)
    net.addLink(host13, switch7)
    net.addLink(host14, switch7)
    net.addLink(host15, switch8)
    net.addLink(host16, switch8)


    net.addLink(switch1, switch2)
    net.addLink(switch2, switch3)
    net.addLink(switch3, switch4)
    net.addLink(switch4, switch5)
    net.addLink(switch5, switch6)
    net.addLink(switch6, switch7)
    net.addLink(switch7, switch8)


    net.build()

    for controller in net.controllers:
        controller.start()

    net.get('switch1').start([c1])
    net.get('switch2').start([c1])
    net.get('switch3').start([c1])
    net.get('switch4').start([c1])
    net.get('switch5').start([c2])
    net.get('switch6').start([c2])
    net.get('switch7').start([c2])
    net.get('switch8').start([c2])


    print("")

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    MyNetwork()
