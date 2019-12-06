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
