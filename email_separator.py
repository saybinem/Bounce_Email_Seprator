# -*- coding: utf-8 -*-
import string
def get_sent_email_list(sent_emails_file):
	all_emails=[]
	f=open(sent_emails_file,'r')
	for i in f:
		i=i.replace('\n','')
		i=i.lower()
		if '\t' in i:
			i=i.lower()
			i=i.replace(' ','').replace('\t','\n')
			i=i.split('\n')
			for e in i:
				all_emails.append(e)
		else:
			all_emails.append(i)
	return all_emails

def get_bounce_email_list(bounce_emails_file):
	bounce_emails=[]
	f=open(bounce_emails_file,'r')
	for i in f:
		if 'Final-Recipient' in i:
			i=i.replace('\n','')
			i=i.split(';')
			i=i[1]
			i=i.replace(' ','')
			i=i.lower()
			bounce_emails.append(i)
	return bounce_emails

def get_bounce_email_list_new_ui(bounce_emails_file):
	bounce_emails=[]
	f=open(bounce_emails_file,'r')
	for i in f:
		try:
			i=i.replace('\'','')
			if 'delivered to' in i:
				i=i.split(' to ')
				i=i[1]
				i=i.strip(' ')
				i=i.split(' ')[0]
				i=i.lower()
				bounce_emails.append(i)
			if 'Your message' in i:
				i=i.split(' to ')
				i=i[1]
				i=i.strip(' ')
				i=i.split(' ')[0]
				i=i.lower()
				bounce_emails.append(i)

			if 'problem delivering' in i:
				i=i.split(' to ')
				i=i[1]
				i=i.strip(' ').strip('.')
				i=i.split(' ')[0]
				i=i.lower()
				i=i.strip('.')
				bounce_emails.append(i)
		except:
			None
	f=open(bounce_emails_file,'r')
	data_list=[]
	for i in f:
		data_list.append(i)
	for i in data_list:
		if 'A message that you sent could not be delivered to one or more of its' in i:

			b=data_list[data_list.index(i)+3].strip('\n').strip(' ')
			#print b
			del data_list[data_list.index(i)]
			bounce_emails.append(b)

	f=open(bounce_emails_file,'r')
	data_list=[]
	for i in f:
		data_list.append(i)
	for i in data_list:
		if 'Delivery has failed to these recipients or groups' in i:
			#print i
			b=data_list[data_list.index(i)+2].strip('\n')
			#print b
			del data_list[data_list.index(i)]
			bounce_emails.append(b)
	f=open(bounce_emails_file,'r')
	data_list=[]
	for i in f:
		data_list.append(i)
	for i in data_list:
		if 'host' in i:
			#print i
			b=i.split('>:')[0].strip('<')
			#print b
			# del data_list[data_list.index(i)]
			bounce_emails.append(b)

	f=open(bounce_emails_file,'r')
	data_list=[]
	for i in f:
		data_list.append(i)
	for i in data_list:
		if 'The following addresses had permanent fatal errors' in i:
			b=data_list[data_list.index(i)+1].replace('<','').replace('>','').strip('\n')
			#print b
			del data_list[data_list.index(i)]
			bounce_emails.append(b)

	f=open(bounce_emails_file,'r')
	data_list=[]
	for i in f:
		data_list.append(i)
	for i in data_list:
		if 'For assistance, please contact your email system administrator and include the following problem report' in i:
			b=data_list[data_list.index(i)+2].replace('<','').replace('>','').strip('\n')
			b=b.split(':')[0].strip(' ').replace('<','').replace('>','')
			del data_list[data_list.index(i)]
			bounce_emails.append(b)
	return bounce_emails

def get_email_status(all_emails,bounce_emails):
	sent_emails=[]
	for i in all_emails:
		if i in bounce_emails:
			sent_emails.append(0)
		else:
			sent_emails.append(i)
	for i in all_emails:
		if i in bounce_emails:
			print 0
		else:
			# print 1,i
			print 1

if __name__ == '__main__':
	sent_emails_file='sent_emails.txt'
	bounce_emails_file='gmail_emails_text_all.txt'
	sent_email_list=get_sent_email_list(sent_emails_file)
	bounce_email_list=get_bounce_email_list_new_ui(bounce_emails_file)
	#bounce_email_list=get_bounce_email_list(bounce_emails_file)
	get_email_status(sent_email_list,bounce_email_list)
	
