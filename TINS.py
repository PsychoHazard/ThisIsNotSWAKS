#!/usr/bin/python

# This Is Not SWAKS
# TINS version 1.4.7
# Copyright (c) 2018 Rob Voss
# rvoss@proofpoint.com

import time
import sys
import getopt
import os
import mimetypes
import platform
import logging
from tempfile import TemporaryFile
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import make_msgid
from email.mime.base import MIMEBase
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from random import randint
from email import charset

PNAME = "TINS"
VERSION = "1.4.7"

def spam_subject(subject_seed):
	logging.info("Generating spammy subject")
	if subject_seed == 1:
		spammy_subject = "Guaranteed to lose 10-12 lbs in 30 days 10.206"
	elif subject_seed == 2:
		spammy_subject = "STOP THE MLM INSANITY"
	else:
		spammy_subject = "Real Protection, Stun Guns!  Free Shipping! Time:2:01:35 PM"
	return spammy_subject

def spam_text_body(text_seed):
	logging.info("Generating spammy text")
	if text_seed == 1:
		spammy_text ="""\
1) Fight The Risk of Cancer!
http://www.adclick.ws/p.cfm?o=315&s=pk007

2) Slim Down - Guaranteed to lose 10-12 lbs in 30 days
http://www.adclick.ws/p.cfm?o=249&s=pk007

3) Get the Child Support You Deserve - Free Legal Advice
http://www.adclick.ws/p.cfm?o=245&s=pk002

4) Join the Web's Fastest Growing Singles Community
http://www.adclick.ws/p.cfm?o=259&s=pk007

5) Start Your Private Photo Album Online!
http://www.adclick.ws/p.cfm?o=283&s=pk007

Have a Wonderful Day,
Offer Manager
PrizeMama
"""
	elif text_seed == 2:
		spammy_text ="""\
Greetings!

You are receiving this letter because you have expressed an interest in 
receiving information about online business opportunities. If this is 
erroneous then please accept my most sincere apology. This is a one-time 
mailing, so no removal is necessary.

If you've been burned, betrayed, and back-stabbed by multi-level marketing, 
MLM, then please read this letter. It could be the most important one that 
has ever landed in your Inbox.

MULTI-LEVEL MARKETING IS A HUGE MISTAKE FOR MOST PEOPLE

MLM has failed to deliver on its promises for the past 50 years. The pursuit 
of the "MLM Dream" has cost hundreds of thousands of people their friends, 
their fortunes and their sacred honor. The fact is that MLM is fatally 
flawed, meaning that it CANNOT work for most people.

The companies and the few who earn the big money in MLM are NOT going to 
tell you the real story. FINALLY, there is someone who has the courage to 
cut through the hype and lies and tell the TRUTH about MLM.

HERE'S GOOD NEWS

There IS an alternative to MLM that WORKS, and works BIG! If you haven't yet 
abandoned your dreams, then you need to see this. Earning the kind of income 
you've dreamed about is easier than you think!

With your permission, I'd like to send you a brief letter that will tell you 
WHY MLM doesn't work for most people and will then introduce you to 
something so new and refreshing that you'll wonder why you haven't heard of 
this before.

I promise that there will be NO unwanted follow up, NO sales pitch, no one 
will call you, and your email address will only be used to send you the 
information. Period.

To receive this free, life-changing information, simply click Reply, type 
"Send Info" in the Subject box and hit Send. I'll get the information to you 
within 24 hours. Just look for the words MLM WALL OF SHAME in your Inbox.

Cordially,

Siddhi

P.S. Someone recently sent the letter to me and it has been the most 
eye-opening, financially beneficial information I have ever received. I 
honestly believe that you will feel the same way once you've read it. And 
it's FREE!


------------------------------------------------------------
This email is NEVER sent unsolicited.  THIS IS NOT "SPAM". You are receiving 
this email because you EXPLICITLY signed yourself up to our list with our 
online signup form or through use of our FFA Links Page and E-MailDOM 
systems, which have EXPLICIT terms of use which state that through its use 
you agree to receive our emailings.  You may also be a member of a Altra 
Computer Systems list or one of many numerous FREE Marketing Services and as 
such you agreed when you signed up for such list that you would also be 
receiving this emailing.
Due to the above, this email message cannot be considered unsolicitated, or 
spam.
-----------------------------------------------------------
"""
	else:
		spammy_text = """\
The Need For Safety Is Real In 2002, You Might Only Get One Chance - Be Ready!
Free Shipping & Handling Within The (USA) If You Order Before May 25, 2002! 
3 Day Super Sale, Now Until May 7, 2002!  Save Up To $30.00 On Some Items!

IT'S GETTING TO BE SPRING AGAIN, PROTECT YOURSELF AS YOU WALK,
JOG AND EXERCISE OUTSIDE.  ALSO PROTECT YOUR LOVED ONES AS
THEY RETURN HOME FROM COLLEGE!

*     LEGAL PROTECTION FOR COLLEGE STUDENTS!

*     GREAT UP'COMING OUTDOOR PROTECTION GIFTS!

*     THERE IS NOTHING WORTH MORE PROTECTING THAN LIFE!

*     OUR STUN DEVICES & PEPPER PRODUCTS ARE LEGAL PROTECTION!

JOIN THE WAR ON CRIME!

STUN GUNS AND BATONS 

EFFECTIVE - SAFE - NONLETHAL

PROTECT YOUR LOVED ONES AND YOURSELF

No matter who you are, no matter what City or Town you live in,
if you live in America, you will be touched by crime.
You hear about it on TV.  You read about it in the newspaper.
It's no secret that crime is a major problem in the U.S. today.
Criminals are finding it easier to commit crimes all the time.
Weapons are readily available.  Our cities' police forces have
more work than they can handle.  Even if these criminal are
caught, they won't be spending long in our nation's overcrowded
jails.  And while lawmakers are well aware of the crime problem,
they don't seem to have any effective answers.

Our Email Address:  Merchants4all@aol.com

INTERESTED:

You will be protecting yourself within 7 days!  Don't Wait,
visit our web page below, and join The War On Crime!

*****************
http://www.geocities.com/realprotection_20022003/
*****************

Well, there is an effective answer.  Take responsibility for
your own security.  Our site has a variety of quality personal
security products.  Visit our site, choose the personal security
products that are right for you.  Use them, and join the war on
crime!

FREE PEPPER SPRAY WITH ANY STUN UNIT PURCHASE.
(A Value of $15.95)

We Ship Orders Within 5 To 7 Days, To Every State In The U.S.A.
by UPS, FEDEX, or U.S. POSTAL SERVICE.  Visa, MasterCard, American
Express & Debt Card Gladly Accepted.

Ask yourself this question, if you don't help your loved ones,
who will?

INTERESTED:

*****************
http://www.geocities.com/realprotection_20022003/
*****************

___The Stun Monster 625,000 Volts ($86.95)

___The Z-Force Slim Style 300,000 Volts ($64.95)

___The StunMaster 300,000 Volts Straight ($59.95)

___The StunMaster 300,000 Volts Curb ($59.95)

___The StunMaster 200,000 Volts Straight ($49.95)

___The StunMaster 200,000 Volts Curb ($49.95)

___The StunBaton 500,000 Volts ($89.95)

___The StunBaton 300,000 Volts ($79.95)

___Pen Knife (One $12.50, Two Or More $9.00)

___Wildfire Pepper Spray  (One $15.95, Two Or More $11.75)

___Add $5.75 For Shipping & Handling Charge.


To Order by postal mail, please send to the below address.

Make payable to Mega Safety Technology.

Mega Safety Technology
3215 Merrimac Ave.
Dayton, Ohio  45405

Our Email Address:  mailto:Merchants4all@aol.com

Order by 24 Hour Fax!!!  775-257-6657.

*****

Important Credit Card Information! Please Read Below!

*     Credit Card Address, City, State and Zip Code, must match
      billing address to be processed. 

CHECK____  MONEYORDER____  VISA____ MASTERCARD____ AmericanExpress___
Debt Card___

Name_______________________________________________________
(As it appears on Check or Credit Card)

Address____________________________________________________
(As it appears on Check or Credit Card)

___________________________________________________
City,State,Zip(As it appears on Check or Credit Card)

___________________________________________________
Country

___________________________________________________
(Credit Card Number)

Expiration Month_____  Year_____

___________________________________________________
Authorized Signature

*****IMPORTANT NOTE*****

If Shipping Address Is Different From The Billing Address Above,
Please Fill Out Information Below.

Shipping Name______________________________________________

Shipping Address___________________________________________

___________________________________________________________
Shipping City,State,Zip

___________________________________________________________
Country

___________________________________________________________
Email Address & Phone Number(Please Write Neat)
"""
	return spammy_text

def spam_html_body(html_seed):
	logging.info("Generating spammy HTML")
	if html_seed == 1:
		spammy_html = """\
<ol>
   <li><a href="http://www.adclick.ws/p.cfm?o=315&s=pk007">Fight The Risk of Cancer!</a></li>
   <li><a href="http://www.adclick.ws/p.cfm?o=249&s=pk007">Slim Down - Guaranteed to lose 10-12 lbs in 30 days</a></li>
   <li><a href="http://www.adclick.ws/p.cfm?o=245&s=pk002">Get the Child Support You Deserve - Free Legal Advice</a></li>
   <li><a href="http://www.adclick.ws/p.cfm?o=259&s=pk007">Join the Web's Fastest Growing Singles Community</a></li>
   <li><a href="http://www.adclick.ws/p.cfm?o=283&s=pk007">Start Your Private Photo Album Online!</a></li>
</ol>
<p>Have a Wonderful Day,<br>
Offer Manager<br>
PrizeMama</p>
"""
	elif html_seed == 2:
		spammy_html = """\
<p>Greetings!</p>
</p>You are receiving this letter because you have expressed an interest in receiving information about online business opportunities. If this is erroneous then please accept my most sincere apology. This is a one-time mailing, so no removal is necessary.</p>
<p>If you've been burned, betrayed, and back-stabbed by multi-level marketing, MLM, then please read this letter. It could be the most important one that has ever landed in your Inbox.</p>
<p>MULTI-LEVEL MARKETING IS A HUGE MISTAKE FOR MOST PEOPLE</p>
<p>MLM has failed to deliver on its promises for the past 50 years. The pursuit of the "MLM Dream" has cost hundreds of thousands of people their friends, their fortunes and their sacred honor. The fact is that MLM is fatally flawed, meaning that it CANNOT work for most people.</p>
<p>The companies and the few who earn the big money in MLM are NOT going to tell you the real story. FINALLY, there is someone who has the courage to cut through the hype and lies and tell the TRUTH about MLM.</p>
<p>HERE'S GOOD NEWS</p>
<p>There IS an alternative to MLM that WORKS, and works BIG! If you haven't yet abandoned your dreams, then you need to see this. Earning the kind of income you've dreamed about is easier than you think!</p>
<p>With your permission, I'd like to send you a brief letter that will tell you WHY MLM doesn't work for most people and will then introduce you to something so new and refreshing that you'll wonder why you haven't heard of this before.</p>
<p>I promise that there will be NO unwanted follow up, NO sales pitch, no one will call you, and your email address will only be used to send you the information. Period.</p>
<p>To receive this free, life-changing information, simply click Reply, type "Send Info" in the Subject box and hit Send. I'll get the information to you within 24 hours. Just look for the words MLM WALL OF SHAME in your Inbox.</p>
<p>Cordially,</p>
<p>Siddhi</p>
<p>P.S. Someone recently sent the letter to me and it has been the most eye-opening, financially beneficial information I have ever received. I honestly believe that you will feel the same way once you've read it. And it's FREE!</p>
<hr>
<p>This email is NEVER sent unsolicited.  THIS IS NOT "SPAM". You are receiving this email because you EXPLICITLY signed yourself up to our list with our online signup form or through use of our FFA Links Page and E-MailDOM systems, which have EXPLICIT terms of use which state that through its use you agree to receive our emailings.  You may also be a member of a Altra Computer Systems list or one of many numerous FREE Marketing Services and as such you agreed when you signed up for such list that you would also be receiving this emailing.</p>
<p>Due to the above, this email message cannot be considered unsolicitated, or spam.</p>
<hr>
"""
	else:
		spammy_html = """\
<center>
<h3>
<font color="blue">
<b>
The Need For Safety Is Real In 2002, You Might Only Get One Chance - Be Ready!
<p>
Free Shipping & Handling Within The (USA) If You Order Before May 25, 2002! 
<p>
3 Day Super Sale, Now Until May 7, 2002!  Save Up To $30.00 On Some Items!

</b>
</font>
</h3>
</center>
<p>
IT'S GETTING TO BE SPRING AGAIN, PROTECT YOURSELF AS YOU WALK,<br>
JOG AND EXERCISE OUTSIDE.  ALSO PROTECT YOUR LOVED ONES AS<br>
THEY RETURN HOME FROM COLLEGE!<br>
<p>
*     LEGAL PROTECTION FOR COLLEGE STUDENTS!<br>
*     GREAT UP'COMING OUTDOOR PROTECTION GIFTS!<br>
*     THERE IS NOTHING WORTH MORE PROTECTING THAN LIFE!<br>
*     OUR STUN DEVICES & PEPPER PRODUCTS ARE LEGAL PROTECTION!
<p>
<b>
<font color="red">
JOIN THE WAR ON CRIME!
</b>
</font>
<p>

STUN GUNS AND BATONS 
<p>
EFFECTIVE - SAFE - NONLETHAL
<p>
PROTECT YOUR LOVED ONES AND YOURSELF
<p>
No matter who you are, no matter what City or Town you live in,<br>
if you live in America, you will be touched by crime.
<p>
You hear about it on TV.  You read about it in the newspaper.<br>
It's no secret that crime is a major problem in the U.S. today.<br>
Criminals are finding it easier to commit crimes all the time.
<p>
Weapons are readily available.  Our cities' police forces have<br>
more work than they can handle.  Even if these criminal are<br>
caught, they won't be spending long in our nation's overcrowded<br>
jails.  And while lawmakers are well aware of the crime problem,<br>
they don't seem to have any effective answers.
<p>
Our Email Address:  <a
href="mailto:Merchants4all@aol.com">Merchants4all@aol.com</a>
<p>
INTERESTED:
<p>
You will be protecting yourself within 7 days!  Don't Wait,<br>
visit our web page below, and join The War On Crime!
<p>
*****************<br>
<a
href="http://www.geocities.com/realprotection_20022003/">http://www.geocities.com/realprotection_20022003/</a><br>
*****************
<p>
Well, there is an effective answer.  Take responsibility for<br>
your own security.  Our site has a variety of quality personal<br>
security products.  Visit our site, choose the personal security<br>
products that are right for you.  Use them, and join the war on
crime!
<p>
FREE PEPPER SPRAY WITH ANY STUN UNIT PURCHASE.<br>
(A Value of $15.95)
<p>
We Ship Orders Within 5 To 7 Days, To Every State In The U.S.A.<br>
by UPS, FEDEX, or U.S. POSTAL SERVICE.  Visa, MasterCard, American<br>
Express & Debt Card Gladly Accepted.
<p>
Ask yourself this question, if you don't help your loved ones,
who will?
<p>
INTERESTED:
<p>
*****************<br>
<a
href="http://www.geocities.com/realprotection_20022003/">http://www.geocities.com/realprotection_20022003/</a><br>
*****************
<p>
___The Stun Monster 625,000 Volts ($86.95)<br>
___The Z-Force Slim Style 300,000 Volts ($64.95)<br>
___The StunMaster 300,000 Volts Straight ($59.95)<br>
___The StunMaster 300,000 Volts Curb ($59.95)<br>
___The StunMaster 200,000 Volts Straight ($49.95)<br>
___The StunMaster 200,000 Volts Curb ($49.95)<br>
___The StunBaton 500,000 Volts ($89.95)<br>
___The StunBaton 300,000 Volts ($79.95)<br>
___Pen Knife (One $12.50, Two Or More $9.00)<br>
___Wildfire Pepper Spray  (One $15.95, Two Or More $11.75)
<p>
___Add $5.75 For Shipping & Handling Charge.
<p>

To Order by postal mail, please send to the below address.<br>
Make payable to Mega Safety Technology.
<p>
Mega Safety Technology<br>
3215 Merrimac Ave.<br>
Dayton, Ohio  45405<br>
Our Email Address:  <a
href="mailto:Merchants4all@aol.com">Merchants4all@aol.com</a>
<p>
Order by 24 Hour Fax!!!  775-257-6657.
<p>
*****<br>
<b><font color="red">Important Credit Card Information! Please Read Below!</b></font>
 <br><br>
*     Credit Card Address, City, State and Zip Code, must match
      billing address to be processed. 
<br><br>

CHECK____  MONEYORDER____  VISA____ MASTERCARD____ AmericanExpress___
Debt Card___
<br><br>
Name_______________________________________________________<br>
(As it appears on Check or Credit Card)
<br><br>
Address____________________________________________________<br>
(As it appears on Check or Credit Card)
<br><br>
___________________________________________________<br>
City,State,Zip(As it appears on Check or Credit Card)
<br><br>
___________________________________________________<br>
Country
<br><br>
___________________________________________________<br>
(Credit Card Number)
<br><br>
Expiration Month_____  Year_____
<br><br>
___________________________________________________<br>
Authorized Signature
<br><br>
<b>
*****IMPORTANT NOTE*****
</b>
<br><br>
If Shipping Address Is Different From The Billing Address Above,
Please Fill Out Information Below.
<br><br>
Shipping Name______________________________________________
<br><br>
Shipping Address___________________________________________
<br><br>
___________________________________________________________<br>
Shipping City,State,Zip
<br><br>
___________________________________________________________<br>
Country
<br><br>
___________________________________________________________<br>
Email Address & Phone Number(Please Write Neat)
"""
	return spammy_html

def mime_headers(mime_multipart, mime_msg_id, mime_xmailer, mime_timestamp, mime_subject, mime_from_header, mime_to_header, mime_importance, mime_priority):
	logging.info("Generating MIME headers")
	try:
		mime_msg = MIMEMultipart(mime_multipart)
		mime_msg['Date'] = mime_timestamp
		mime_msg['Subject'] = mime_subject
		mime_msg['From'] = mime_from_header
		mime_msg['To'] = mime_to_header
		mime_msg['Message-Id'] = mime_msg_id
		mime_msg['Importance'] = mime_importance
		mime_msg['X-Priority'] = mime_priority
		mime_msg['X-Mailer'] = mime_xmailer
	except Exception, exc:
		logging.critical( "Adding MIME headers failed: %s\r\nExiting." % str(exc) )
		sys.exit( "Adding MIME headers failed: %s\r\nExiting." % str(exc) ) # give a error message
	return mime_msg

def text_mime(text_msg, mime_text, zip_text, url_text, ssn_text, text_charset):
	logging.info("Generating text body")
	zip_mime_text = ""
	ssn_mime_text = ""
	url_mime_text = "\r\n"
	try:
		if zip_text:
			logging.info("Adding ZIP text to text body")
			zip_mime_text = '\r\nPlease see the attached.\r\nIf needed, password = "test"\r\n'
		if ssn_text:
			logging.info("Adding SSN text to text body")
			ssn_mime_text = '\r\nHave some SSN numbers:\r\n623-57-9564\r\nSSN 215-79-8735\r\n544 71 7243\r\n112968357\r\n'
		if url_text:
			logging.info("Adding URL text to text body")
			url_mime_text = "\r\nFor awesome stuff and free candy go to http://tapdemo.evilscheme.org/files/tapdemo_313533343139383733322e3939.docx\r\nWe promise it's totally safe!\r\n"
		mime_text_body = mime_text + ssn_mime_text + zip_mime_text + url_mime_text
		text_part = MIMEText(mime_text_body.encode(text_charset), 'plain', text_charset)
		text_msg.attach(text_part)
	except Exception, exc:
		logging.critical( "Adding text body failed: %s\r\nExiting." % str(exc) )
		sys.exit( "Adding text body failed: %s\r\nExiting." % str(exc) ) # give a error message
	return text_msg
	
def html_mime(html_msg, mime_html_text, zip_html, url_html, ssn_html, html_charset):
	logging.info("Generating HTML body")
	zip_mime_html = "\r\n"
	ssn_mime_html = ""
	url_mime_html = ""
	if zip_html:
		logging.info("Adding ZIP text to HTML body")
		zip_mime_html = '\r\n		<p>Please see the attached.<br>\r\n		If needed, password = "test"</p>\r\n'
	if ssn_html:
		logging.info("Adding SSN text to HTML body")
		ssn_mime_html = '\r\n		<p>Have some SSN numbers:<br>\r\n		623-57-9564<br>\r\n		SSN 215-79-8735<br>\r\n		544 71 7243<br>\r\n		112968357</p>\r\n'
	if url_html:
		logging.info("Adding URL text to HTML body")
		url_mime_html = '		<p>For awesome stuff and free candy go to <a href="http://tapdemo.evilscheme.org/files/tapdemo_313533343139383733322e3939.docx">totallysafe.unmarkedvan.com</a></p>\r\n'
	try:
		mime_html1 = """\
		<html>
			<body>
		"""
		mime_html2 = mime_html_text + ssn_mime_html + zip_mime_html + url_mime_html
		mime_html3 = """\
			</body>
		</html>
		"""
		mime_html_body = mime_html1 + "\r\n" + mime_html2 + "\r\n" + mime_html3
		html_part = MIMEText(mime_html_body.encode(html_charset), 'html', html_charset)
		html_msg.attach(html_part)
	except Exception, exc:
		logging.critical( "Adding html body failed: %s\r\nExiting." % str(exc) )
		sys.exit( "Adding html body failed: %s\r\nExiting." % str(exc) ) # give a error message
	return html_msg

def eicar(eicar_msg):
	logging.info("Attaching EICAR virus")
	try:
		eicar_base64 = 'WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy1URVNU\r\nLUZJTEUhJEgrSCo=\r\n'
		eicar_part = MIMEBase('application','octet-stream')
		eicar_part.set_payload(eicar_base64)
		eicar_part.add_header('Content-Disposition', 'attachment; filename="eicar.com.txt"')
		eicar_part.add_header('Content-Transfer-Encoding', 'base64')
		eicar_msg.attach(eicar_part)
	except Exception, exc:
		logging.critical( "Adding EICAR virus failed: %s\r\nExiting." % str(exc) )
		sys.exit( "Adding EICAR virus failed: %s\r\nExiting." % str(exc) ) # give a error message
	return eicar_msg

def pass_zip(zip_msg):
	logging.info("Attaching ZIP file")
	try:
		zip_base64 = 'UEsDBAoACQAAACl7aDTABgONIAAAABQAAAARABUAYXJjaGl2ZXMvdGVzdC50eHRVVAkAA95nD0Te\r\nZw9EVXgEAOYn5ieyjOxAmV7wTzO2Ecxui1HKQBjXwV22GTqb6O99X3KDd1BLBwjABgONIAAAABQA\r\nAABQSwECFwMKAAkAAAApe2g0wAYDjSAAAAAUAAAAEQANAAAAAAABAAAAtIEAAAAAYXJjaGl2ZXMv\r\ndGVzdC50eHRVVAUAA95nD0RVeAAAUEsFBgAAAAABAAEATAAAAHQAAAAAAA==\r\n'
		zip_part = MIMEBase('application','octet-stream')
		zip_part.set_payload(zip_base64)
		zip_part.add_header('Content-Transfer-Encoding', 'base64')
		zip_part.add_header('Content-Disposition', 'attachment; filename="../test.zip"')
		zip_msg.attach(zip_part)
	except Exception, exc:
		logging.critical( "Adding zip file failed: %s\r\nExiting." % str(exc) )
		sys.exit( "Adding zip file failed: %s\r\nExiting." % str(exc) ) # give a error message
	return zip_msg

def attach_file(attach_msg, file_attach):
	try:
		ctype, encoding = mimetypes.guess_type(file_attach)
		if ctype is None or encoding is not None:
			ctype = 'application/octet-stream'
		logging.info("Attaching " + file_attach)
		logging.info(file_attach + " MIME type = " + ctype)
		maintype, subtype = ctype.split('/', 1)
		if maintype == 'text':
			af = open(file_attach, 'r')
			attach_part = MIMEText(af.read(), _subtype=subtype)
			af.close()
		elif maintype == 'image':
			af = open(file_attach, 'rb')
			attach_part = MIMEImage(af.read(), _subtype=subtype)
			af.close()
		elif maintype == 'audio':
			af = open(file_attach, 'rb')
			attach_part = MIMEAudio(af.read(), _subtype=subtype)
			af.close()
		else:
			af = open(file_attach, 'rb')
			attach_part = MIMEBase(maintype, subtype)
			attach_part.set_payload(af.read())
			af.close()
			encoders.encode_base64(attach_part)
		attach_part.add_header('Content-Disposition', 'attachment', filename=file_attach)
		attach_msg.attach(attach_part)
	except Exception, exc:
		logging.critical( "Adding %s file failed: %s\r\nExiting." % (file_attach, str(exc)) )
		sys.exit( "Adding %s file failed: %s\r\nExiting." % (file_attach, str(exc)) ) # give a error message
	return attach_msg

def try_tls(tls_serv):
	logging.info("Trying TLS")
	try:
		tls_serv.starttls()
	except Exception, exc:
		logging.critical( "Email failed: %s\r\nExiting." % str(exc) )
		sys.exit( "Email failed: %s\r\nExiting." % str(exc) ) # give a error message

def send_email(send_target, send_port, send_sender, send_recipient, send_body, send_tls):
	logging.info("Sending email")
	t = TemporaryFile()
	available_fd = t.fileno()
	t.close()
	os.dup2(2,available_fd)
	t = TemporaryFile()
	os.dup2(t.fileno(),2)
	try:
		server = SMTP(send_target, send_port)
		server.set_debuglevel(100)
		server.ehlo_or_helo_if_needed()
		if send_tls:
			try_tls(server)
		server.sendmail(send_sender, send_recipient, send_body)
		server.quit()
		sys.stderr.flush()
		t.flush()
		t.seek(0)
		stderr_output = t.read()
		t.close()
		os.dup2(available_fd,2)
		os.close(available_fd)
		count = 0
		for line in stderr_output.decode('utf-8').split("\n"):
			count += 1
			logging.debug(line)
			print (line)
	except Exception, exc:
		logging.critical( "Email failed: %s\r\nExiting." % str(exc) ) # log error message
		sys.exit( "Email failed: %s\r\nExiting." % str(exc) ) # give an error message

def write_eml_file(write_eml_name, write_body):
	logging.info("Writing email to " + write_eml_name)
	try:
		emf = open(write_eml_name, 'w')
		emf.write(write_body)
		emf.close()
		print 'Email written to file:', write_eml_name
	except Exception, exc:
		logging.critical( "Writing to file failed: %s\r\nExiting." % str(exc) )
		sys.exit( "Writing to file failed: %s\r\nExiting." % str(exc) ) # give a error message

def tty_rows(tty_count):
	rows, columns = os.popen('stty size', 'r').read().split()
	tty_lines = int(rows) - 2
	if tty_lines <= tty_count:
		if platform.python_version().startswith("2"):
			raw_input('<[PRESS ENTER TO CONTINUE]>')
		elif platform.python_version().startswith("3"):
			input('<[PRESS ENTER TO CONTINUE]>')
		tty_count = 0
	return tty_count

def help_out():
	out = PNAME + " v" + VERSION + """

Usage:
   TINS.py <options>
Options:
   -h, --help [this info]
   -s, --server, --target [target mail server]
   -p, --port [target port]
   -t, --to, --recipient [recipient]
   -f, --from, --sender [sender]
   -x, --xm, --x-mailer [X-Mailer header]
   --log [enable logging]
   --log-level [set logging level, implies --log
      valid values are:
         debug
         info
         warning (default)
         error
         critical]
   --log-file [set name of log file, defaults to TINS.log, implies --log]
   --mix, --mixed [use multipart/mixed instead of multipart/alternative]
   --to-header [to: header if different from recipient]
   --from-header [from: header if different from sender]
   --body-text [text body string]
   --body-html [html body string]
   --text-encode, --text-charset [character encoding for text section]
   --html-encode, --html-charset [character encoding for html section]
   --encode, --charset [character encoding for both text and html sections
      (overrides --text-encode/--text-charset/--html-encode/--html-charset)]
   --high, --low [message importance (default is medium)]
   --ssl, --tls [use ssl/tls]
   --url [include malicious url]
   --ssn [include ssn numbers]
   --av, --virus [include eicar test virus]
   --zip [include password protected zip file]
   --eml, --write [write email to eml file]
   --no-send [do not send email (implies --eml/--write)]
   --eml-name [email file name (implies --eml/--write)]
   --no-text [no text body]
   --no-html [no html body]
   --spam [generate test spam]
   --adult [generate test adult spam (overrides --spam)]
   --text-body [text body from specified file]
   --html-body [html body from specified file]
   --attach [attach specified file]"""
	count = 0
	for line in out.splitlines():
		print (line)
		count = tty_rows(count) + 1

def main(argv):
	timestamp = time.strftime("%a, %d %b %Y %H:%M:%S %z")
	subject = "Test Message: " + timestamp
	sender = "sender@example.com"
	from_header = sender
	recipient = "recipient@example.com"
	to_header = recipient
	target = "smtp.example.com"
	port = 25
	helo = ""
	msg_id = make_msgid()
	xmailer = PNAME + " v" + VERSION
	text = "This is a test message.\r\nThe python has spoken!\r\nNyaah!"
	html_text = '		<p><b>This is a test message!</b></p>\r\n		<p>The python has spoken! Nyaah!</p>'
	av_test = False
	spam_test = False
	adult_test = False
	url_test = False
	zip_test = False
	ssn_test = False
	tls = False
	use_text = True
	use_html = True
	eml_send = True
	eml_file = False
	eml_name = time.strftime("%Y%m%d%H%M%S%z") + ".eml"
	no_has_to = True
	no_has_from = True
	text_encode = 'us-ascii'
	html_encode = 'us-ascii'
	all_encode = 'us-ascii'
	encode_both = False
	seed = randint(0,2)
	multi_type = 'alternative'
	msg_importance = 'medium'
	msg_priority = '3'
	textfile = 'NONE'
	htmlfile = 'NONE'
	attachfile = 'NONE'
	is_attach = False
	is_logging = False
	log_level = logging.WARNING
	log_file = 'TINS.log'
	log_init = ''
	log_warn = False

	try:
		opts, args = getopt.getopt(argv,"h:s:p:t:f:e:x:",["server=","target=","port=","to=","recipient=","from=","sender=","ehlo=","helo=","to-header=","from-header=","subject=","ssl","tls","spam","adult","virus","av","url","zip","eml","write","no-send","eml-name=","no-text","no-html","xm=","x-mailer=","text-encode=","text-charset=","html-encode=","html-charset=","encode=","charset=","body-text=","body-html=","ssn","mix","mixed","high","low","text-body=","html-body=","attach=","log","log-level=","log-file="])
	except getopt.GetoptError:
		help_out()
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			help_out()
		elif opt in ("-s", "--server", "--target"):
			target = arg
		elif opt in ("-p", "--port"):
			port = arg
		elif opt in ("-t", "--to", "--recipient"):
			recipient = arg
		elif opt in ("-f", "--from", "--sender"):
			sender = arg
		elif opt in ("--tls", "--ssl"):
			tls = True
		elif opt in ("--virus", "--av"):
			av_test = True
		elif opt in ("--mix", "--mixed"):
			multi_type = 'mixed'
		elif opt == '--subject':
			subject = arg
		elif opt == '--to-header':
			to_header = arg
			no_has_to = False
		elif opt == '--from-header':
			from_header = arg
			no_has_from = False
		elif opt == '--spam':
		 	spam_test = True
		elif opt == '--adult':
		 	adult_test = True
		elif opt == '--url':
		 	url_test = True
		elif opt == '--zip':
			zip_test = True
		elif opt == '--ssn':
		 	ssn_test = True
		elif opt in ("--eml", "--write"):
			eml_file = True
		elif opt == "--no-send":
			eml_send = False
			eml_file = True
		elif opt == '--eml-name':
			eml_name = arg
			eml_file = True
		elif opt == '--no-text':
			use_text = False
		elif opt == '--no-html':
			use_html = False
		elif opt in ("-x", "--xm", "--x-mailer"):
			xmailer = arg
		elif opt in ("--text-encode", "--text-charset"):
			text_encode = arg
			charset.add_charset(text_encode.lower(), charset.SHORTEST, charset.QP)
		elif opt in ("--html-encode", "--html-charset"):
			html_encode = arg
			charset.add_charset(html_encode.lower(), charset.SHORTEST, charset.QP)
		elif opt in ("--encode", "--charset"):
			all_encode = arg
			charset.add_charset(all_encode.lower(), charset.SHORTEST, charset.QP)
			encode_both = True
		elif opt == '--body-text':
			text = arg
		elif opt == '--body-html':
			html_text = arg
		elif opt == '--low':
			msg_importance = 'low'
			msg_priority = '5'
		elif opt == '--high':
			msg_importance = 'high'
			msg_priority = '1'
		elif opt == '--text-body':
			textfile = arg
			tb = open(textfile, 'r')
			text = tb.read()
			tb.close()
		elif opt == '--html-body':
			htmlfile = arg
			hb = open(htmlfile, 'r')
			html_text = hb.read()
			hb.close()
		elif opt == '--attach':
			is_attach = True
			attachfile = arg
		elif opt == '--log':
			is_logging = True
		elif opt == '--log-level':
			is_logging = True
			log_init = "Logging initialized."
			if arg.lower() == 'debug':
				log_level = logging.DEBUG
			elif arg.lower() == 'info':
				log_level = logging.INFO
			elif arg.lower() == 'warning':
				log_level = logging.WARNING
			elif arg.lower() == 'error':
				log_level = logging.ERROR
			elif arg.lower() == 'critical':
				log_level = logging.CRITICAL
			else:
				log_init = "Invalid log level. Falling back to default."
				log_level = logging.WARNING
				log_warn = True
			print (log_init)
		elif opt == '--log-file':
			is_logging = True
			log_file = arg

	if is_logging:
		logging.basicConfig(format='[%(asctime)s] <%(levelname)s> %(message)s', filename=log_file, level=log_level)
	else:
		logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.ERROR)

	if log_warn:
		logging.warning(log_init)
	else:
		logging.info(log_init)

	logging.debug('Parameters:' + str(sys.argv[1:]))
	logging.info("Beginning email creation")

	if encode_both:
		text_encode = all_encode
		html_encode = all_encode
	
	if no_has_to:
		to_header = recipient

	if no_has_from:
		from_header = sender
	
	if adult_test:
		logging.info("Generating Adult email")
		subject = "Wanna hook up? I love you all night long!"
		text = "Hey. Great profile. See mine. XoXo Julz, http://gonie.info"
		html_text = '		<p>Hey. Great profile.<br>See mine.<br>XoXo Julz, <a href="http://gonie.info">Click here to see my profile!</a></p>'
	elif spam_test:
		subject = spam_subject(seed)
		text = spam_text_body(seed)
		html_text = spam_html_body(seed)

	msg = mime_headers(multi_type, msg_id, xmailer, timestamp, subject, from_header, to_header, msg_importance, msg_priority)
	
	if use_text:
		msg_text = text_mime(msg, text, zip_test, url_test, ssn_test, text_encode)
		msg = msg_text
	
	if use_html:
		msg_html = html_mime(msg, html_text, zip_test, url_test, ssn_test, html_encode)
		msg = msg_html

	if av_test:
		av_message = eicar(msg)
		msg = av_message

	if zip_test:
		zip_message = pass_zip(msg)
		msg = zip_message

	if is_attach:
		attach_message = attach_file(msg, attachfile)
		msg = attach_message

	body = msg.as_string()
	logging.info("Email creation completed")

	if eml_send:
		send_email(target, port, sender, recipient, body, tls)

	if eml_file:
		write_eml_file(eml_name, body)

if __name__ == "__main__":
	main(sys.argv[1:])
