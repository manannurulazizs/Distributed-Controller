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

    info("*** Adding 16 switch")
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
    switch9 = net.addSwitch('switch9')
    switch10 = net.addSwitch('switch10')
    switch11 = net.addSwitch('switch11')
    switch12 = net.addSwitch('switch12')
    switch13 = net.addSwitch('switch13')
    switch14 = net.addSwitch('switch14')
    switch15 = net.addSwitch('switch15')
    switch16 = net.addSwitch('switch16')

    print("(16 switch)")
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
    host17 = net.addHost('h17', ip='192.168.1.17')
    host18 = net.addHost('h18', ip='192.168.1.18')
    host19 = net.addHost('h19', ip='192.168.1.19')
    host20 = net.addHost('h20', ip='192.168.1.20')
    host21 = net.addHost('h21', ip='192.168.1.21')
    host22 = net.addHost('h22', ip='192.168.1.22')
    host23 = net.addHost('h23', ip='192.168.1.23')
    host24 = net.addHost('h24', ip='192.168.1.24')
    host25 = net.addHost('h25', ip='192.168.1.25')
    host26 = net.addHost('h26', ip='192.168.1.26')
    host27 = net.addHost('h27', ip='192.168.1.27')
    host28 = net.addHost('h28', ip='192.168.1.28')
    host29 = net.addHost('h29', ip='192.168.1.29')
    host30 = net.addHost('h30', ip='192.168.1.30')
    host31 = net.addHost('h31', ip='192.168.1.31')
    host32 = net.addHost('h32', ip='192.168.1.32')


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
    net.addLink(host17, switch9)
    net.addLink(host18, switch9)
    net.addLink(host19, switch10)
    net.addLink(host20, switch10)
    net.addLink(host21, switch11)
    net.addLink(host22, switch11)
    net.addLink(host23, switch12)
    net.addLink(host24, switch12)
    net.addLink(host25, switch13)
    net.addLink(host26, switch13)
    net.addLink(host27, switch14)
    net.addLink(host28, switch14)
    net.addLink(host29, switch15)
    net.addLink(host30, switch15)
    net.addLink(host31, switch16)
    net.addLink(host32, switch16)

    net.addLink(switch1, switch2)
    net.addLink(switch2, switch3)
    net.addLink(switch3, switch4)
    net.addLink(switch4, switch5)
    net.addLink(switch5, switch6)
    net.addLink(switch6, switch7)
    net.addLink(switch7, switch8)
    net.addLink(switch8, switch9)
    net.addLink(switch9, switch10)
    net.addLink(switch10, switch11)
    net.addLink(switch11, switch12)
    net.addLink(switch12, switch13)
    net.addLink(switch13, switch14)
    net.addLink(switch14, switch15)
    net.addLink(switch15, switch16)

    net.build()

    for controller in net.controllers:
        controller.start()

    net.get('switch1').start([c1])
    net.get('switch2').start([c1])
    net.get('switch3').start([c1])
    net.get('switch4').start([c1])
    net.get('switch5').start([c1])
    net.get('switch6').start([c1])
    net.get('switch7').start([c1])
    net.get('switch8').start([c1])
    net.get('switch9').start([c2])
    net.get('switch10').start([c2])
    net.get('switch11').start([c2])
    net.get('switch12').start([c2])
    net.get('switch13').start([c2])
    net.get('switch14').start([c2])
    net.get('switch15').start([c2])
    net.get('switch16').start([c2])

    print("")

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    MyNetwork()
