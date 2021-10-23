# import sys

import mysql.connector as mysql
from flask import Flask, render_template, request, jsonify,send_file, request, session, abort,flash
#import file
import  pandas as pd

import openpyxl
# from flask_mysqldb import MySQL
# import random, json
# from getpass import getpass
# from mysql.connector import connect, Error


detail = {'aadarsh.ft221001@greatlakes.edu.in': 'FT221001', 'aamir.ft221002@greatlakes.edu.in': 'FT221002',
		  'aayush.ft221003@greatlakes.edu.in': 'FT221003', 'abhilasha.ft221004@greatlakes.edu.in': 'FT221004',
		  'abhimanyu.ft221005@greatlakes.edu.in': 'FT221005', 'abhinavsingh.ft221006@greatlakes.edu.in': 'FT221006',
		  'abhinavsharma.ft221007@greatlakes.edu.in': 'FT221007', 'abhisek.ft221008@greatlakes.edu.in': 'FT221008',
		  'abhishekbisht.ft221009@greatlakes.edu.in': 'FT221009',
		  'abhishekgupta.ft221010@greatlakes.edu.in': 'FT221010', 'abishek.ft221012@greatlakes.edu.in': 'FT221012',
		  'aditi.ft221013@greatlakes.edu.in': 'FT221013', 'adityasharma.ft221015@greatlakes.edu.in': 'FT221015',
		  'aishwarya.ft221017@greatlakes.edu.in': 'FT221017', 'ajay.ft221018@greatlakes.edu.in': 'FT221018',
		  'ajmal.ft221019@greatlakes.edu.in': 'FT221019', 'akashagarwal.ft221022@greatlakes.edu.in': 'FT221022',
		  'akchaiya.ft221023@greatlakes.edu.in': 'FT221023', 'akhand.ft221024@greatlakes.edu.in': 'FT221024',
		  'akshat.ft221025@greatlakes.edu.in': 'FT221025', 'akshay.ft221026@greatlakes.edu.in': 'FT221026',
		  'alex.ft221028@greatlakes.edu.in': 'FT221028', 'allada.ft221029@greatlakes.edu.in': 'FT221029',
		  'allok.ft221030@greatlakes.edu.in': 'FT221030', 'amaan.ft221031@greatlakes.edu.in': 'FT221031',
		  'aman.ft221032@greatlakes.edu.in': 'FT221032', 'amar.ft221033@greatlakes.edu.in': 'FT221033',
		  'amartya.ft221034@greatlakes.edu.in': 'FT221034', 'ambuj.ft221035@greatlakes.edu.in': 'FT221035',
		  'amitkumar.ft221036@greatlakes.edu.in': 'FT221036', 'amol.ft221037@greatlakes.edu.in': 'FT221037',
		  'amrit.ft221038@greatlakes.edu.in': 'FT221038', 'amrita.ft221039@greatlakes.edu.in': 'FT221039',
		  'anantha.ft221042@greatlakes.edu.in': 'FT221042', 'ananya.ft221043@greatlakes.edu.in': 'FT221043',
		  'anaranya.ft221044@greatlakes.edu.in': 'FT221044', 'aniruddha.ft221046@greatlakes.edu.in': 'FT221046',
		  'ankitasahana.ft221047@greatlakes.edu.in': 'FT221047', 'ankitabasak.ft221048@greatlakes.edu.in': 'FT221048',
		  'ankitajaiswal.ft221049@greatlakes.edu.in': 'FT221049', 'anshuljain.ft221050@greatlakes.edu.in': 'FT221050',
		  'anshulgupta.ft221051@greatlakes.edu.in': 'FT221051', 'antas.ft221052@greatlakes.edu.in': 'FT221052',
		  'anubha.ft221053@greatlakes.edu.in': 'FT221053', 'anubhav.ft221054@greatlakes.edu.in': 'FT221054',
		  'anwesha.ft221055@greatlakes.edu.in': 'FT221055', 'apoorv.ft221056@greatlakes.edu.in': 'FT221056',
		  'aritra.ft221057@greatlakes.edu.in': 'FT221057', 'arkodaya.ft221058@greatlakes.edu.in': 'FT221058',
		  'arunchandran.ft221059@greatlakes.edu.in': 'FT221059', 'arun.ft221060@greatlakes.edu.in': 'FT221060',
		  'arusharka.ft221061@greatlakes.edu.in': 'FT221061', 'arushi.ft221062@greatlakes.edu.in': 'FT221062',
		  'ashishviresh.ft221063@greatlakes.edu.in': 'FT221063', 'ashlesh.ft221064@greatlakes.edu.in': 'FT221064',
		  'ashwin.ft221065@greatlakes.edu.in': 'FT221065', 'asthadikshit.ft221066@greatlakes.edu.in': 'FT221066',
		  'asthamishra.ft221067@greatlakes.edu.in': 'FT221067', 'atharv.ft221068@greatlakes.edu.in': 'FT221068',
		  'avilash.ft221069@greatlakes.edu.in': 'FT221069', 'avinash.ft221070@greatlakes.edu.in': 'FT221070',
		  'avisha.ft221071@greatlakes.edu.in': 'FT221071', 'ayushitomar.ft221072@greatlakes.edu.in': 'FT221072',
		  'balram.ft221073@greatlakes.edu.in': 'FT221073', 'banugu.ft221074@greatlakes.edu.in': 'FT221074',
		  'boddu.ft221076@greatlakes.edu.in': 'FT221076', 'chaitanya.ft221077@greatlakes.edu.in': 'FT221077',
		  'chevendra.ft221078@greatlakes.edu.in': 'FT221078', 'deep.ft221079@greatlakes.edu.in': 'FT221079',
		  'deepika.ft221080@greatlakes.edu.in': 'FT221080', 'dhananjay.ft221081@greatlakes.edu.in': 'FT221081',
		  'dinesh.ft221082@greatlakes.edu.in': 'FT221082', 'divya.ft221083@greatlakes.edu.in': 'FT221083',
		  'fiona.ft221085@greatlakes.edu.in': 'FT221085', 'girish.ft221086@greatlakes.edu.in': 'FT221086',
		  'jayashree.ft221087@greatlakes.edu.in': 'FT221087', 'kanchan.ft221088@greatlakes.edu.in': 'FT221088',
		  'katyayni.ft221089@greatlakes.edu.in': 'FT221089', 'mustanseer.ft221090@greatlakes.edu.in': 'FT221090',
		  'rahul.ft221091@greatlakes.edu.in': 'FT221091', 'supreetha.ft221092@greatlakes.edu.in': 'FT221092',
		  'yaman.ft221094@greatlakes.edu.in': 'FT221094', 'yeddula.ft221095@greatlakes.edu.in': 'FT221095',
		  'amitthakur.ft222001@greatlakes.edu.in': 'FT222001', 'apurva.ft222002@greatlakes.edu.in': 'FT222002',
		  'archak.ft222003@greatlakes.edu.in': 'FT222003', 'archit.ft222004@greatlakes.edu.in': 'FT222004',
		  'arin.ft222005@greatlakes.edu.in': 'FT222005', 'arindam.ft222006@greatlakes.edu.in': 'FT222006',
		  'avi.ft222007@greatlakes.edu.in': 'FT222007', 'ayushraj.ft222009@greatlakes.edu.in': 'FT222009',
		  'ayushgogia.ft222010@greatlakes.edu.in': 'FT222010', 'ayushimittal.ft222011@greatlakes.edu.in': 'FT222011',
		  'bavneet.ft222012@greatlakes.edu.in': 'FT222012', 'bhavyakandpal.ft222013@greatlakes.edu.in': 'FT222013',
		  'chandi.ft222014@greatlakes.edu.in': 'FT222014', 'dawa.ft222016@greatlakes.edu.in': 'FT222016',
		  'dhairya.ft222017@greatlakes.edu.in': 'FT222017', 'dhruvil.ft222018@greatlakes.edu.in': 'FT222018',
		  'dipanjandutta.ft222020@greatlakes.edu.in': 'FT222020', 'divyansh.ft222021@greatlakes.edu.in': 'FT222021',
		  'gagandeep.ft222022@greatlakes.edu.in': 'FT222022', 'gaurav.ft222023@greatlakes.edu.in': 'FT222023',
		  'harshanidhi.ft222025@greatlakes.edu.in': 'FT222025', 'harshamangnani.ft222026@greatlakes.edu.in': 'FT222026',
		  'harshaljat.ft222027@greatlakes.edu.in': 'FT222027', 'harshalbhardwaj.ft222028@greatlakes.edu.in': 'FT222028',
		  'harshit.ft222029@greatlakes.edu.in': 'FT222029', 'himanshu.ft222031@greatlakes.edu.in': 'FT222031',
		  'indrani.ft222032@greatlakes.edu.in': 'FT222032', 'jampana.ft222034@greatlakes.edu.in': 'FT222034',
		  'jason.ft222035@greatlakes.edu.in': 'FT222035', 'joe.ft222037@greatlakes.edu.in': 'FT222037',
		  'joji.ft222038@greatlakes.edu.in': 'FT222038', 'jonathan.ft222039@greatlakes.edu.in': 'FT222039',
		  'jostin.ft222040@greatlakes.edu.in': 'FT222040', 'joy.ft222041@greatlakes.edu.in': 'FT222041',
		  'kalava.ft222042@greatlakes.edu.in': 'FT222042', 'kapil.ft222043@greatlakes.edu.in': 'FT222043',
		  'karansarpal.ft222044@greatlakes.edu.in': 'FT222044', 'karangupta.ft222045@greatlakes.edu.in': 'FT222045',
		  'karanrai.ft222046@greatlakes.edu.in': 'FT222046', 'karankhazanchi.ft222047@greatlakes.edu.in': 'FT222047',
		  'karanam.ft222048@greatlakes.edu.in': 'FT222048', 'karthik.ft222049@greatlakes.edu.in': 'FT222049',
		  'kartik.ft222050@greatlakes.edu.in': 'FT222050', 'kaushikkalyan.ft222051@greatlakes.edu.in': 'FT222051',
		  'kaushikkumar.ft222052@greatlakes.edu.in': 'FT222052', 'kaustavsen.ft222053@greatlakes.edu.in': 'FT222053',
		  'kaustavpaul.ft222054@greatlakes.edu.in': 'FT222054', 'keerthi.ft222055@greatlakes.edu.in': 'FT222055',
		  'koushik.ft222056@greatlakes.edu.in': 'FT222056', 'kratika.ft222057@greatlakes.edu.in': 'FT222057',
		  'krishnaabhilash.ft222058@greatlakes.edu.in': 'FT222058',
		  'krishnamadhavan.ft222059@greatlakes.edu.in': 'FT222059', 'kriti.ft222060@greatlakes.edu.in': 'FT222060',
		  'mahak.ft222061@greatlakes.edu.in': 'FT222061', 'mahima.ft222062@greatlakes.edu.in': 'FT222062',
		  'manas.ft222063@greatlakes.edu.in': 'FT222063', 'mandar.ft222064@greatlakes.edu.in': 'FT222064',
		  'manishtalreja.ft222065@greatlakes.edu.in': 'FT222065', 'mansi.ft222067@greatlakes.edu.in': 'FT222067',
		  'manu.ft222068@greatlakes.edu.in': 'FT222068', 'manveen.ft222069@greatlakes.edu.in': 'FT222069',
		  'mayankkishore.ft222071@greatlakes.edu.in': 'FT222071', 'megha.ft222072@greatlakes.edu.in': 'FT222072',
		  'milan.ft222073@greatlakes.edu.in': 'FT222073', 'miti.ft222074@greatlakes.edu.in': 'FT222074',
		  'mohammad.ft222075@greatlakes.edu.in': 'FT222075', 'mohitlaxman.ft222076@greatlakes.edu.in': 'FT222076',
		  'mohitshrivastava.ft222077@greatlakes.edu.in': 'FT222077', 'mohitbaid.ft222078@greatlakes.edu.in': 'FT222078',
		  'mrunali.ft222079@greatlakes.edu.in': 'FT222079', 'muaaz.ft222080@greatlakes.edu.in': 'FT222080',
		  'naveen.ft222081@greatlakes.edu.in': 'FT222081', 'nayan.ft222082@greatlakes.edu.in': 'FT222082',
		  'nihal.ft222083@greatlakes.edu.in': 'FT222083', 'nikhilkrishnan.ft222084@greatlakes.edu.in': 'FT222084',
		  'nikhita.ft222085@greatlakes.edu.in': 'FT222085', 'nithya.ft222086@greatlakes.edu.in': 'FT222086',
		  'preethisri.ft222087@greatlakes.edu.in': 'FT222087', 'prekshi.ft222088@greatlakes.edu.in': 'FT222088',
		  'priya.ft222089@greatlakes.edu.in': 'FT222089', 'priyankapotnuru.ft222090@greatlakes.edu.in': 'FT222090',
		  'richa.ft222091@greatlakes.edu.in': 'FT222091', 'samrat.ft222092@greatlakes.edu.in': 'FT222092',
		  'vishruth.ft222093@greatlakes.edu.in': 'FT222093', 'yerradoddi.ft222094@greatlakes.edu.in': 'FT222094',
		  'sakshi.ft222096@greatlakes.edu.in': 'FT222096', 'bhavyasikri.ft223001@greatlakes.edu.in': 'FT223001',
		  'chirag.ft223002@greatlakes.edu.in': 'FT223002', 'mayanksharma.ft223004@greatlakes.edu.in': 'FT223004',
		  'mohd.ft223005@greatlakes.edu.in': 'FT223005', 'mohitsrivastava.ft223006@greatlakes.edu.in': 'FT223006',
		  'mohit.ft223007@greatlakes.edu.in': 'FT223007', 'nihit.ft223008@greatlakes.edu.in': 'FT223008',
		  'nikhilvyas.ft223009@greatlakes.edu.in': 'FT223009', 'nikhilkumar.ft223010@greatlakes.edu.in': 'FT223010',
		  'nikhilramachandran.ft223011@greatlakes.edu.in': 'FT223011',
		  'omkardattatraya.ft223013@greatlakes.edu.in': 'FT223013', 'omkarajay.ft223014@greatlakes.edu.in': 'FT223014',
		  'palash.ft223015@greatlakes.edu.in': 'FT223015', 'parimi.ft223016@greatlakes.edu.in': 'FT223016',
		  'piyush.ft223019@greatlakes.edu.in': 'FT223019', 'ponsaravanan.ft223020@greatlakes.edu.in': 'FT223020',
		  'pradeep.ft223023@greatlakes.edu.in': 'FT223023', 'pradyumna.ft223024@greatlakes.edu.in': 'FT223024',
		  'prafull.ft223025@greatlakes.edu.in': 'FT223025', 'praharsha.ft223026@greatlakes.edu.in': 'FT223026',
		  'pranav.ft223027@greatlakes.edu.in': 'FT223027', 'pranit.ft223028@greatlakes.edu.in': 'FT223028',
		  'pranjal.ft223029@greatlakes.edu.in': 'FT223029', 'prashanth.ft223031@greatlakes.edu.in': 'FT223031',
		  'prathamesh.ft223032@greatlakes.edu.in': 'FT223032', 'pravesh.ft223035@greatlakes.edu.in': 'FT223035',
		  'preksha.ft223036@greatlakes.edu.in': 'FT223036', 'priyadarshini.ft223037@greatlakes.edu.in': 'FT223037',
		  'priyank.ft223038@greatlakes.edu.in': 'FT223038', 'priyankarajhans.ft223039@greatlakes.edu.in': 'FT223039',
		  'pronoy.ft223040@greatlakes.edu.in': 'FT223040', 'pulkitkumar.ft223041@greatlakes.edu.in': 'FT223041',
		  'pulkitrajan.ft223042@greatlakes.edu.in': 'FT223042', 'pushkar.ft223043@greatlakes.edu.in': 'FT223043',
		  'rachana.ft223044@greatlakes.edu.in': 'FT223044', 'rahulrajput.ft223045@greatlakes.edu.in': 'FT223045',
		  'rahulmondal.ft223046@greatlakes.edu.in': 'FT223046', 'raj.ft223047@greatlakes.edu.in': 'FT223047',
		  'rajashree.ft223048@greatlakes.edu.in': 'FT223048', 'rajatkumar.ft223049@greatlakes.edu.in': 'FT223049',
		  'rajatjoshi.ft223050@greatlakes.edu.in': 'FT223050', 'rajatmittal.ft223051@greatlakes.edu.in': 'FT223051',
		  'rakesh.ft223052@greatlakes.edu.in': 'FT223052', 'rakeshan.ft223053@greatlakes.edu.in': 'FT223053',
		  'ramagnish.ft223054@greatlakes.edu.in': 'FT223054', 'rameez.ft223055@greatlakes.edu.in': 'FT223055',
		  'ramkumar.ft223056@greatlakes.edu.in': 'FT223056', 'ratika.ft223057@greatlakes.edu.in': 'FT223057',
		  'ravali.ft223058@greatlakes.edu.in': 'FT223058', 'ravi.ft223059@greatlakes.edu.in': 'FT223059',
		  'rehan.ft223060@greatlakes.edu.in': 'FT223060', 'rishav.ft223061@greatlakes.edu.in': 'FT223061',
		  'rituparna.ft223062@greatlakes.edu.in': 'FT223062', 'rohit.ft223064@greatlakes.edu.in': 'FT223064',
		  'roobhini.ft223065@greatlakes.edu.in': 'FT223065', 'rushil.ft223066@greatlakes.edu.in': 'FT223066',
		  'bharatwaj.ft223067@greatlakes.edu.in': 'FT223067', 'sabyasachi.ft223069@greatlakes.edu.in': 'FT223069',
		  'sachin.ft223070@greatlakes.edu.in': 'FT223070', 'sagarkhurana.ft223071@greatlakes.edu.in': 'FT223071',
		  'saipramod.ft223073@greatlakes.edu.in': 'FT223073', 'sam.ft223074@greatlakes.edu.in': 'FT223074',
		  'sampadatiwari.ft223075@greatlakes.edu.in': 'FT223075', 'sampadaulhas.ft223076@greatlakes.edu.in': 'FT223076',
		  'samuel.ft223077@greatlakes.edu.in': 'FT223077', 'sanket.ft223078@greatlakes.edu.in': 'FT223078',
		  'santhoju.ft223079@greatlakes.edu.in': 'FT223079', 'sarani.ft223080@greatlakes.edu.in': 'FT223080',
		  'saronee.ft223081@greatlakes.edu.in': 'FT223081', 'saurabhdeep.ft223082@greatlakes.edu.in': 'FT223082',
		  'saurav.ft223083@greatlakes.edu.in': 'FT223083', 'sayali.ft223084@greatlakes.edu.in': 'FT223084',
		  'shaista.ft223085@greatlakes.edu.in': 'FT223085', 'shalika.ft223086@greatlakes.edu.in': 'FT223086',
		  'shubhamsharma.ft223088@greatlakes.edu.in': 'FT223088', 'soumya.ft223089@greatlakes.edu.in': 'FT223089',
		  'soundarya.ft223090@greatlakes.edu.in': 'FT223090', 'tanmay.ft223091@greatlakes.edu.in': 'FT223091',
		  'tanya.ft223092@greatlakes.edu.in': 'FT223092', 'thota.ft223093@greatlakes.edu.in': 'FT223093',
		  'vigneshradhakrishnan.ft223094@greatlakes.edu.in': 'FT223094', 'vivek.ft223095@greatlakes.edu.in': 'FT223095',
		  'vishalsoni.ft223096@greatlakes.edu.in': 'FT223096', 'suraj.ft223097@greatlakes.edu.in': 'FT223097',
		  'prithiviraj.ft223098@greatlakes.edu.in': 'FT223098', 'dawood.ft223099@greatlakes.edu.in': 'FT223099',
		  'abhisheksnehel.ft224001@greatlakes.edu.in': 'FT224001', 'adityadilip.ft224002@greatlakes.edu.in': 'FT224002',
		  'akansha.ft224003@greatlakes.edu.in': 'FT224003', 'gautam.ft224004@greatlakes.edu.in': 'FT224004',
		  'rishabh.ft224005@greatlakes.edu.in': 'FT224005', 'ritvick.ft224006@greatlakes.edu.in': 'FT224006',
		  'rohan.ft224007@greatlakes.edu.in': 'FT224007', 'rupam.ft224008@greatlakes.edu.in': 'FT224008',
		  'sagarroy.ft224009@greatlakes.edu.in': 'FT224009', 'sagarhiten.ft224010@greatlakes.edu.in': 'FT224010',
		  'sagarravindra.ft224011@greatlakes.edu.in': 'FT224011', 'sahil.ft224012@greatlakes.edu.in': 'FT224012',
		  'saketsanjeev.ft224013@greatlakes.edu.in': 'FT224013', 'sanchit.ft224015@greatlakes.edu.in': 'FT224015',
		  'sanjay.ft224016@greatlakes.edu.in': 'FT224016', 'sankhadeep.ft224017@greatlakes.edu.in': 'FT224017',
		  'saurab.ft224020@greatlakes.edu.in': 'FT224020', 'saurabhvyas.ft224021@greatlakes.edu.in': 'FT224021',
		  'sayan.ft224022@greatlakes.edu.in': 'FT224022', 'shaifalee.ft224023@greatlakes.edu.in': 'FT224023',
		  'shantanu.ft224024@greatlakes.edu.in': 'FT224024', 'shashang.ft224025@greatlakes.edu.in': 'FT224025',
		  'shashi.ft224026@greatlakes.edu.in': 'FT224026', 'shayan.ft224027@greatlakes.edu.in': 'FT224027',
		  'shikha.ft224028@greatlakes.edu.in': 'FT224028', 'shivanandhreddy.ft224029@greatlakes.edu.in': 'FT224029',
		  'shivani.ft224030@greatlakes.edu.in': 'FT224030', 'shivashankar.ft224031@greatlakes.edu.in': 'FT224031',
		  'shreedevi.ft224032@greatlakes.edu.in': 'FT224032', 'shreenidhi.ft224033@greatlakes.edu.in': 'FT224033',
		  'shrey.ft224034@greatlakes.edu.in': 'FT224034', 'shreyabanerjee.ft224035@greatlakes.edu.in': 'FT224035',
		  'shreyakeshri.ft224036@greatlakes.edu.in': 'FT224036', 'shreyansh.ft224037@greatlakes.edu.in': 'FT224037',
		  'shreyas.ft224039@greatlakes.edu.in': 'FT224039', 'shruti.ft224040@greatlakes.edu.in': 'FT224040',
		  'shubhabrata.ft224041@greatlakes.edu.in': 'FT224041', 'shubhamkaushik.ft224042@greatlakes.edu.in': 'FT224042',
		  'sibiraj.ft224045@greatlakes.edu.in': 'FT224045', 'siddartha.ft224046@greatlakes.edu.in': 'FT224046',
		  'siddharthpanda.ft224047@greatlakes.edu.in': 'FT224047',
		  'siddharthshrivastava.ft224048@greatlakes.edu.in': 'FT224048',
		  'siddharth.ft224049@greatlakes.edu.in': 'FT224049', 'siddharthbhatt.ft224050@greatlakes.edu.in': 'FT224050',
		  'siddharthchakraborti.ft224051@greatlakes.edu.in': 'FT224051',
		  'snehal.ft224052@greatlakes.edu.in': 'FT224052', 'soham.ft224053@greatlakes.edu.in': 'FT224053',
		  'sonali.ft224054@greatlakes.edu.in': 'FT224054', 'soujatya.ft224055@greatlakes.edu.in': 'FT224055',
		  'souvik.ft224056@greatlakes.edu.in': 'FT224056', 'stuti.ft224059@greatlakes.edu.in': 'FT224059',
		  'subhasree.ft224061@greatlakes.edu.in': 'FT224061', 'sudhana.ft224062@greatlakes.edu.in': 'FT224062',
		  'sumadyuti.ft224063@greatlakes.edu.in': 'FT224063', 'suman.ft224064@greatlakes.edu.in': 'FT224064',
		  'sunmeet.ft224066@greatlakes.edu.in': 'FT224066', 'sushant.ft224067@greatlakes.edu.in': 'FT224067',
		  'swati.ft224068@greatlakes.edu.in': 'FT224068', 'tanishka.ft224069@greatlakes.edu.in': 'FT224069',
		  'taraswi.ft224070@greatlakes.edu.in': 'FT224070', 'thanushk.ft224071@greatlakes.edu.in': 'FT224071',
		  'thumma.ft224072@greatlakes.edu.in': 'FT224072', 'trishla.ft224073@greatlakes.edu.in': 'FT224073',
		  'tushal.ft224074@greatlakes.edu.in': 'FT224074', 'tushar.ft224075@greatlakes.edu.in': 'FT224075',
		  'udit.ft224076@greatlakes.edu.in': 'FT224076', 'uppu.ft224078@greatlakes.edu.in': 'FT224078',
		  'utkarsh.ft224079@greatlakes.edu.in': 'FT224079', 'saiganesh.ft224080@greatlakes.edu.in': 'FT224080',
		  'varsha.ft224081@greatlakes.edu.in': 'FT224081', 'varunmaddineni.ft224082@greatlakes.edu.in': 'FT224082',
		  'varungangadharan.ft224083@greatlakes.edu.in': 'FT224083', 'varunraaj.ft224084@greatlakes.edu.in': 'FT224084',
		  'venkata.ft224085@greatlakes.edu.in': 'FT224085', 'venkatasai.ft224086@greatlakes.edu.in': 'FT224086',
		  'venkatesh.ft224087@greatlakes.edu.in': 'FT224087', 'vigneshramkumar.ft224088@greatlakes.edu.in': 'FT224088',
		  'vikash.ft224089@greatlakes.edu.in': 'FT224089', 'vinay.ft224090@greatlakes.edu.in': 'FT224090',
		  'vishalguha.ft224091@greatlakes.edu.in': 'FT224091', 'vishalgarg.ft224092@greatlakes.edu.in': 'FT224092',
		  'vishraj.ft224093@greatlakes.edu.in': 'FT224093', 'vrishti.ft224094@greatlakes.edu.in': 'FT224094',
		  'yatin.ft224095@greatlakes.edu.in': 'FT224095', 'mohdaquil.ft224096@greatlakes.edu.in': 'FT224096',
		  'girish.ft224097@greatlakes.edu.in': 'FT224097', 'testpm@greatlakes.edu.ins': 'FT00001'};

app = Flask(__name__)

db = mysql.connect(
		host="localhost",
		user="root",
		passwd="1234",
		database="testingdb"
	)

cursor = db.cursor()

@app.route('/')
def index():
	# serve index template #
	return render_template('index.html')
@app.route('/front',methods = ['POST','GET'])
def front():
	# serve index template #
	if(request.method == 'POST'):

		global user
		global pswd

		user=request.form.get('user')
		pswd=request.form.get('pword')

		if user in detail and pswd ==detail[user]:
			print(pswd, user)

			cursor.execute("SELECT * FROM course2 WHERE regno =  '{}' ;".format(pswd) )
			user1 = cursor.fetchone()
			user2=list(user1)
			print(user2)
			return render_template('FrontPage.html',user=user,regno=pswd)
		else:

			return  render_template('login page.html')





@app.route('/preview')
def preview():
	# serve index template
	return render_template('preview.html',user=user,regno=pswd)



@app.route('/download')
def download_file1():
	path1 = "t1-Financial Statement Analysis - Manaswee SamalList.csv"

	return send_file(path1, as_attachment=True)


@app.route('/download')
def download_file2():
	path2 = "t1-IT Consulting - Sriram RajagopalanList.csv"
	return send_file(path2, as_attachment=True)


@app.route('/submit', methods = ['POST','GET'])
def worker():
	if request.method == 'POST':
		print('Incoming..')
		print(request.get_json())# parse as JSON
		datas=request.get_json()
		s_id=pswd
		s_name = user
		course1 = request.json['course1']
		course2 = request.json['course2']
		course3 = request.json['course3']
		course4 = request.json['course4']
		course5 = request.json['course5']
		course6 = request.json['course6']
		course7 = request.json['course7']
		course8 = request.json['course8']
		course9 = request.json['course9']
		course10 = request.json['course10']
		course11 = request.json['course11']
		course12 = request.json['course12']
		course13 = request.json['course13']
		course14 = request.json['course14']
		course15 = request.json['course15']
		course16 = request.json['course16']
		course17 = request.json['course17']
		course18 = request.json['course18']
		course19 = request.json['course19']
		course20 = request.json['course20']
		values = ( s_name,s_id, course1, course2, course3, course4, course5, course6, course7, course8, course9, course10, course11 , course12, course13, course14, course15, course16, course17, course18, course19, course20)


		query = """INSERT INTO course2
				(email,regno,course1,course2,course3,course4,course5,course6,course7,course8,course9,course10,course11,course12,course13,course14,course15,course16,course17,course18,course19,course20)
				VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
				ON DUPLICATE KEY UPDATE
  				  email=VALUES(email),
  				 course1=VALUES(course1),
  				 course2=VALUES(course2),
  				 course3=VALUES(course3),
  				 course4=VALUES(course4),
  				 course5=VALUES(course5),
  				 course6=VALUES(course6),
  				 course7=VALUES(course7),
  				 course8=VALUES(course8),
  				 course9=VALUES(course9),
  				 course10=VALUES(course10),
  				 course11=VALUES(course11),
  				 course12=VALUES(course12),
  				 course13=VALUES(course13),
  				 course14=VALUES(course14),
  				 course15=VALUES(course15),
  				 course16=VALUES(course16),
  				 course17=VALUES(course17),
  				 course18=VALUES(course18),
  				 course19=VALUES(course19),
  				 course20=VALUES(course20)"""




		print(datas)

		cursor.execute(query, values )

		db.commit()

		print(cursor.rowcount, "record inserted")

		query = "SELECT * FROM course2"

		cursor.execute("SELECT * FROM course2")
		results = cursor.fetchall()
		print(results)
		dresult_dataFrame = pd.read_sql(query, db)
		print(dresult_dataFrame)

		f1 = dresult_dataFrame.to_csv("course.csv", index=False)
		db.close()
		f = pd.read_csv('course.csv', header=None)
		f.columns = ['timr', 'Regno', 'Name', 'sub1', 'sub2', 'sub3', 'sub4', 'sub5', 'sub6', 'sub7', 'sub8', 'sub9',
					 'sub10',
					 'sub11',
					 'sub12', 'sub13', 'sub14', 'sub15', 'sub16', 'sub17', 'sub18', 'sub19', 'sub20']

		f.drop_duplicates(subset="Regno", keep='first', inplace=True)

		d = f.sort_values(by=['sub1', 'sub2', 'sub3'], ascending=True)
		SUBJECTList = ['t1-Financial Statement Analysis - Manaswee Samal', 't1-IT Consulting - Sriram Rajagopalan']
		for SUBJECTName in SUBJECTList:
			f1 = d[(d['sub1'] == SUBJECTName) | (d['sub2'] == SUBJECTName) | (d['sub3'] == SUBJECTName) | (
					d['sub4'] == SUBJECTName) |
				   (d['sub5'] == SUBJECTName) | (d['sub6'] == SUBJECTName) | (d['sub7'] == SUBJECTName) | (
						   d['sub8'] == SUBJECTName) | (d['sub9'] == SUBJECTName) |
				   (d['sub10'] == SUBJECTName) | (d['sub11'] == SUBJECTName) | (d['sub12'] == SUBJECTName) | (
						   d['sub13'] == SUBJECTName) | (d['sub14'] == SUBJECTName) |
				   (d['sub15'] == SUBJECTName) | (d['sub16'] == SUBJECTName) | (d['sub17'] == SUBJECTName) | (
						   d['sub18'] == SUBJECTName) | (d['sub19'] == SUBJECTName) |
				   (d['sub20'] == SUBJECTName)]

			f1.index.name = SUBJECTName
			f2 = f1.filter(['Name'])

			for i in range(len(SUBJECTList)):
				if SUBJECTList[i] == SUBJECTName:
					f2.to_csv(SUBJECTName + '.csv', encoding='utf-8', index=False)
					f4 = pd.read_csv(SUBJECTName + '.csv')
					f4 = f2.rename(columns={'Name': SUBJECTName}, inplace=False)
					f4.to_csv(SUBJECTName + 'List.csv', encoding='utf-8', index=False)
		l1 = pd.read_csv(SUBJECTList[0] + 'List.csv')
		l2 = pd.read_csv(SUBJECTList[1] + 'List.csv')

		global df
		global df1

		df = len(l1.index)
		df1 = len(l2.index)

		return 'OK sudess', 200

	# GET request
	else :

		message = {'greeting': 'Hello from Flask!'}
		return jsonify(message)  # serialize and use JSON headers


@app.route('/admin')
def admin():



	f = pd.read_csv('course.csv', header=None)
	f.columns = ['timr','Regno', 'Name', 'sub1', 'sub2', 'sub3', 'sub4', 'sub5', 'sub6', 'sub7', 'sub8', 'sub9', 'sub10',
				 'sub11',
				 'sub12', 'sub13', 'sub14', 'sub15', 'sub16', 'sub17', 'sub18', 'sub19', 'sub20']

	f.drop_duplicates(subset="Regno", keep='first', inplace=True)

	d = f.sort_values(by=['sub1', 'sub2', 'sub3'], ascending=True)
	SUBJECTList = ['t1-Financial Statement Analysis - Manaswee Samal', 't1-IT Consulting - Sriram Rajagopalan']
	for SUBJECTName in SUBJECTList:
		f1 = d[(d['sub1'] == SUBJECTName) | (d['sub2'] == SUBJECTName) | (d['sub3'] == SUBJECTName) | (
				d['sub4'] == SUBJECTName) |
			   (d['sub5'] == SUBJECTName) | (d['sub6'] == SUBJECTName) | (d['sub7'] == SUBJECTName) | (
					   d['sub8'] == SUBJECTName) | (d['sub9'] == SUBJECTName) |
			   (d['sub10'] == SUBJECTName) | (d['sub11'] == SUBJECTName) | (d['sub12'] == SUBJECTName) | (
					   d['sub13'] == SUBJECTName) | (d['sub14'] == SUBJECTName) |
			   (d['sub15'] == SUBJECTName) | (d['sub16'] == SUBJECTName) | (d['sub17'] == SUBJECTName) | (
					   d['sub18'] == SUBJECTName) | (d['sub19'] == SUBJECTName) |
			   (d['sub20'] == SUBJECTName)]

		f1.index.name = SUBJECTName
		f2 = f1.filter(['Name'])

		for i in range(len(SUBJECTList)):
			if SUBJECTList[i] == SUBJECTName:
				f2.to_csv(SUBJECTName + '.csv', encoding='utf-8', index=False)
				f4 = pd.read_csv(SUBJECTName + '.csv')
				f4 = f2.rename(columns={'Name': SUBJECTName}, inplace=False)
				f4.to_csv(SUBJECTName + 'List.csv', encoding='utf-8', index=False)
	l1 = pd.read_csv(SUBJECTList[0] + 'List.csv')
	l2 = pd.read_csv(SUBJECTList[1] + 'List.csv')

	global df
	global df1

	df = len(l1.index)
	df1 = len(l2.index)

	output1 = df
	output2 = df1

	return render_template('adminpage.html', output1=output1, output2=output2)




if __name__ == '__main__':
	# run!
	app.run(debug=True)