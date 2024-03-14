cd pox/pox/misc/
touch custom_switch_firewall.py

./pox.py misc.custom_switch_firewall

sudo mn --topo single,3 --mac --switch ovsk --controller remote

# In mininet
pingall
h1 ping h2

