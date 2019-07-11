# Distributed-Controller
Topologi distributed controller pada jaringan SDN menggunakan POX Controller.

## Requirements
- Pox Controller
- Create 2 Virtual Machine (untuk controller 1 dan controller 2)
- RabbitMQ (Message Broker bisa local atau public)
- Mininet

## Running program!!!
1. File l2_learning.py code untuk controller 1 (on VM1) dan l2_learning2.py untuk controller 2 (on VM 2)
2. Jalankan POX Controller pada masing-masing VM

- ./pox.py forwarding.l2_learning openflow.of_01 –port=6633 (controller 1)
- ./pox.py forwarding.l2_learning openflow.of_01 –port=6634 (controller 2)

3. jalankan program di main terminal (pexpect.py, TopologiAA.py, TopologiAB.py)

