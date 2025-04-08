def get_contact_make_vcf():
    name = input("ENTER NAME: ")
    number = input("ENTER PHONE NUMBER: ")
    email = input("ENTER MAIL(if any): ")
    
    vcftxt = "BEGIN:VCARD\n"
    vcftxt += "PE:" + name + "\n"
    vcftxt += "TEL:" + number + "\n"
    vcftxt += "EMAIL:" + email + "\n"
    vcftxt += "END:VCARD\n"
    with open('my_contact.vcf', 'w') as f:
        f.write(vcftxt)
    print("Saved to my_contact.vcf")
get_contact_make_vcf()