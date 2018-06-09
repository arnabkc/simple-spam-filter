import os
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app
from spamfilter.main.config import basedir

from spamfilter.main.service.spam_or_ham import is_spam

class TestModelPredict(TestCase):
    def create_app(self):
        app.config.from_object('spamfilter.main.config.DevelopmentConfig')
        return app
        
    def test_spam_or_ham(self):
        emails_test = [
            '''Subject: flat screens 
            hello ,
            please call or contact regarding the other flat screens requested .
            trisha tlapek - eb 3132 b
            michael sergeev - eb 3132 a
            also the sun blocker that was taken away from eb 3131 a .
            trisha should two monitors also michael .
            thanks
            kevin moore''',
            '''Subject: having problems in bed ? we can help !
            cialis allows men to enjoy a fully normal conjugal life without problem.
            if we let things terrify us , life will not be worth living .
            brevity is the soul of lingerie .
            suspicion always haunts the guilty mind .''',
            
            '''Subject: christmas tree farm pictures''',
            
            '''Subject: vastar resources , inc .
            gary , production from the high island larger block a - 1 # 2 commenced on
            saturday at 2 : 00 p . m . at about 6 , 500 gross . carlos expects between 9 , 500 and
            10 , 000 gross for tomorrow . vastar owns 68 % of the gross production .
            george x 3 - 6992
            - - - - - - - - - - - - - - - - - - - - - - forwarded by george weissman / hou / ect on 12 / 13 / 99 10 : 16
            am - - - - - - - - - - - - - - - - - - - - - - - - - - -
            daren j farmer
            12 / 10 / 99 10 : 38 am
            to : carlos j rodriguez / hou / ect @ ect
            cc : george weissman / hou / ect @ ect , melissa graves / hou / ect @ ect
            subject : vastar resources , inc .
            carlos ,
            please call linda and get everything set up .
            i ' m going to estimate 4 , 500 coming up tomorrow , with a 2 , 000 increase each
            following day based on my conversations with bill fischer at bmar .
            d .
            - - - - - - - - - - - - - - - - - - - - - - forwarded by daren j farmer / hou / ect on 12 / 10 / 99 10 : 34
            am - - - - - - - - - - - - - - - - - - - - - - - - - - -
            enron north america corp .
            from : george weissman 12 / 10 / 99 10 : 00 am
            to : daren j farmer / hou / ect @ ect
            cc : gary bryan / hou / ect @ ect , melissa graves / hou / ect @ ect
            subject : vastar resources , inc .
            darren ,
            the attached appears to be a nomination from vastar resources , inc . for the
            high island larger block a - 1 # 2 ( previously , erroneously referred to as the
            # 1 well ) . vastar now expects the well to commence production sometime
            tomorrow . i told linda harris that we ' d get her a telephone number in gas
            control so she can provide notification of the turn - on tomorrow . linda ' s
            numbers , for the record , are 281 . 584 . 3359 voice and 713 . 312 . 1689 fax .
            would you please see that someone contacts linda and advises her how to
            submit future nominations via e - mail , fax or voice ? thanks .
            george x 3 - 6992
            - - - - - - - - - - - - - - - - - - - - - - forwarded by george weissman / hou / ect on 12 / 10 / 99 09 : 44
            am - - - - - - - - - - - - - - - - - - - - - - - - - - -
            " linda harris " on 12 / 10 / 99 09 : 38 : 43 am
            to : george weissman / hou / ect @ ect
            cc :
            subject : hi a - 1 # 2
            effective 12 - 11 - 99
            | - - - - - - - - + - - - - - - - - - - + - - - - - - - - - - - |
            | | | |
            | mscf / d | min ftp | time |
            | | | |
            | - - - - - - - - + - - - - - - - - - - + - - - - - - - - - - - |
            | | | |
            | 4 , 500 | 9 , 925 | 24 hours |
            | | | |
            | - - - - - - - - + - - - - - - - - - - + - - - - - - - - - - - |
            | | | |
            | 6 , 000 | 9 , 908 | 24 hours |
            | | | |
            | - - - - - - - - + - - - - - - - - - - + - - - - - - - - - - - |
            | | | |
            | 8 , 000 | 9 , 878 | 24 hours |
            | | | |
            | - - - - - - - - + - - - - - - - - - - + - - - - - - - - - - - |
            | | | |
            | 10 , 000 | 9 , 840 | 24 hours |
            | | | |
            | - - - - - - - - + - - - - - - - - - - + - - - - - - - - - - - |
            | | | |
            | 12 , 000 | 9 , 793 | 24 hours |
            | | | |
            | - - - - - - - - + - - - - - - - - - - + - - - - - - - - - - - |
            | | | |
            | 14 , 000 | 9 , 738 | 24 hours |
            | | | |
            | - - - - - - - - + - - - - - - - - - - + - - - - - - - - - - - |
            | | | |
            | 16 , 000 | 9 , 674 | 24 hours |
            | | | |
            | - - - - - - - - + - - - - - - - - - - + - - - - - - - - - - - |
            | | | |
            | 18 , 000 | 9 , 602 | 24 hours |
            | | | |
            | - - - - - - - - + - - - - - - - - - - + - - - - - - - - - - - |
            | | | |
            | 20 , 000 | 9 , 521 | 24 hours |
            | | | |
            | - - - - - - - - + - - - - - - - - - - + - - - - - - - - - - - |
            | | | |
            | 22 , 000 | 9 , 431 | 24 hours |
            | | | |
            | - - - - - - - - + - - - - - - - - - - + - - - - - - - - - - - |
            | | | |
            | 24 , 000 | 9 , 332 | 24 hours |
            | | | |
            | - - - - - - - - + - - - - - - - - - - + - - - - - - - - - - - |
            | | | |
            | 26 , 000 | 9 , 224 | 24 hours |
            | | | |
            | - - - - - - - - + - - - - - - - - - - + - - - - - - - - - - - |
            | | | |
            | 28 , 000 | 9 , 108 | 24 hours |
            | | | |
            | - - - - - - - - + - - - - - - - - - - + - - - - - - - - - - - |
            | | | |
            | 30 , 000 | 8 , 982 | 24 hours |
            | | | |
            | - - - - - - - - + - - - - - - - - - - + - - - - - - - - - - - |
            | | | |
            | 32 , 000 | 8 , 847 | 24 hours |
            | | | |
            | - - - - - - - - + - - - - - - - - - - + - - - - - - - - - - - |
            | | | |
            | 34 , 000 | 8 , 703 | 24 hours |
            | | | |
            | - - - - - - - - + - - - - - - - - - - + - - - - - - - - - - - |
            | | | |
            | 36 , 000 | 8 , 549 | 24 hours |
            | | | |
            | - - - - - - - - + - - - - - - - - - - + - - - - - - - - - - - |''',
            
            '''Subject: dobmeos with hgh my energy level has gone up ! stukm
            introducing
            doctor - formulated
            hgh
            human growth hormone - also called hgh
            is referred to in medical science as the master hormone . it is very plentiful
            when we are young , but near the age of twenty - one our bodies begin to produce
            less of it . by the time we are forty nearly everyone is deficient in hgh ,
            and at eighty our production has normally diminished at least 90 - 95 % .
            advantages of hgh :
            - increased muscle strength
            - loss in body fat
            - increased bone density
            - lower blood pressure
            - quickens wound healing
            - reduces cellulite
            - improved vision
            - wrinkle disappearance
            - increased skin thickness texture
            - increased energy levels
            - improved sleep and emotional stability
            - improved memory and mental alertness
            - increased sexual potency
            - resistance to common illness
            - strengthened heart muscle
            - controlled cholesterol
            - controlled mood swings
            - new hair growth and color restore
            read
            more at this website
            unsubscribe
            ''',
        ]

        predicted_labels, returncode = is_spam(emails_test)

        print(returncode)
        print(predicted_labels)

        # [0: ham, 1: spam, 2: ham, 3: ham, 4: spam]
        self.assertEqual(predicted_labels[0], 'Ham')
        self.assertEqual(predicted_labels[1], 'Spam')
        self.assertEqual(predicted_labels[2], 'Ham')
        self.assertEqual(predicted_labels[3], 'Ham')
        self.assertEqual(predicted_labels[4], 'Spam')
