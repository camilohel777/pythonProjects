from mininet.topo import Topo

class MyTopo(Topo):

        def __init__(self):
                "Creating custom topology"

                #Initialize topology
                Topo.__init__(self)

                #Adding hosts and switches
                topLeftHost = self.addHost('h1')
                botLeftHost = self.addHost('h2')
                topRightHost = self.addHost('h3')
                botRightHost = self.addHost('h4')
                leftSwitch = self.addSwitch('s1')
                rightSwitch = self.addSwitch('s2')

                #adding links
                self.addLink(topLeftHost, leftSwitch,bw = 10)
                self.addLink(botLeftHost, leftSwitch,bw = 15)
                self.addLink(leftSwitch, rightSwitch, bw= 20)
                self.addLink(topRightHost, rightSwitch,bw= 15)
                self.addLink(botRightHost, rightSwitch,bw = 5)

topos = { 'mytopo': ( lambda: MyTopo() ) }
