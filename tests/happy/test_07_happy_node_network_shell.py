#!/usr/bin/env python

#
#    Copyright (c) 2016-2017 Nest Labs, Inc.
#    All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#

##
#    @file
#       Tests happy node joining and leaving a network.
#

import pexpect
import os
import unittest


class test_happy_node_network_shell(unittest.TestCase):
    def setUp(self):
        pass

    def test_node(self):
        os.system("happy-node-add node01")
        os.system("happy-network-add -t thread network01")
        os.system("happy-node-join node01 network01")

        os.system("happy-node-add -i node02")
        os.system("happy-network-add -t wifi -i network02")
        os.system("happy-node-join -i node02 -n network02")
        os.system("happy-node-join -i node01 -n network02")

        os.system("happy-node-add -i node03 --ap")
        os.system("happy-node-add -i node04 --service")
        os.system("happy-node-add -i node05 --local")
        os.system("happy-node-add -i node06")
        os.system("happy-network-add -t wan network03")
        os.system("happy-node-join node03 network03")
        os.system("happy-node-join node04 network03")
        os.system("happy-node-join node05 network03")
        os.system("happy-node-join node06 network03")

        os.system("happy-node-leave node01 network01")
        os.system("happy-node-leave node02 network02")
        os.system("happy-node-leave node01 network02")
        os.system("happy-node-leave node03 network03")
        os.system("happy-node-leave node04 network03")
        os.system("happy-node-leave node05 network03")
        os.system("happy-node-leave node06 network03")

        os.system("happy-node-delete node01")
        os.system("happy-node-delete node02")
        os.system("happy-node-delete node03")
        os.system("happy-node-delete node04")
        os.system("happy-node-delete node05")
        os.system("happy-node-delete node06")

        os.system("happy-network-delete network01")
        os.system("happy-network-delete network02")
        os.system("happy-network-delete network03")

        child = pexpect.spawn("happy-state")
        child.expect('   Prefixes\r\n\r\nNODES      Name    Interface    Type                                          IPs\r\n\r\n')
        child.close(force=True)

    def tearDown(self):
        os.system("happy-state-delete")

if __name__ == "__main__":
    unittest.main()
