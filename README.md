# JobSeeker
Automated email sender.


Simple console app, first created to send CV here and there, but you may use it for daily business mailing as well.
Console menu with two options: 
- to send a standard email to various receivers;
- to send different messages to each receiver;

You need to set up three files (I used simple 'txt' format, but you may redo the code and use .csv or whatever you need):
- 'receivers' - a list of receivers
- 'subject'/'subjects' - email subject/list of subjects for various messages
- 'text'/'texts' - message text/set of texts for various messages
- 'attachments' - if you need to attach a file to your letter

Before running the program please make sure all the files for the automated mailing are updated!

What I added:
*Reading lines uses now reading whole and splitting to lines in file standard_message.py, since splitlines generate problem with end of line marker \n
*be aware that you should use gmail to send email
*to log in to gmail via ap you need device key - more info here: https://support.google.com/accounts/answer/185833?visit_id=638780884007847211-3252833778&p=InvalidSecondFactor&rd=1
*I created bash script to fill missing file and folder structure, in my opinion code was incomplete without them. After running script with 'bash folder-maker.sh' you just need to edit files with correct informations.
*as attachment I tested with .pdf
*I used it to send up to 4 emails so far, big scale feedback soon