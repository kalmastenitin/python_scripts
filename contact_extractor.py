'''This Script will convert vcf contact file exported from google contacts to comma seperated values
   To conver the vcf file vcf file should be placed inside the same folder with this Script
   This Script is simple if you want you can add more features to it.
'''

with open('my_contacts.vcf', encoding='utf-8') as f:
    contacts = f.read().strip().split('\n')
names = []
name = ''
Email = ''
mobile = ''
for contact in contacts:
    if 'EMAIL' in contact:
        Email = contact.split(':')[-1]
    if 'FN' in contact:
        name = contact.split(':')[-1]
    if 'TEL' in contact:
        mobile = contact.split(':')[-1]
    if contact == 'END:VCARD':
        names.append('{},{},{}'.format(name,Email,mobile))

for name in names:
    print(name)
