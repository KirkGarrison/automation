import re

def filter_phone_number(num):
  regex = r"[0-9]"
  phone_value = ''
  while len(phone_value)<3:
    for char in num:
      if re.match(regex, char):
        phone_value += char
  return int(phone_value)

def filter_email(email):
  email_value = []
  for char in email[:]:
    value = ord(char) - 97
    email_value.append(value)

  return email_value


def write_phone_email_info(path):
  with open(f"{path}") as file:
    potential_contact_txt = file.read()

  regex_phone_finder = r"\(?\d{3}\)?[ -.]\d{3}[ -.]\d{4}"

  phone_numbers = re.findall(regex_phone_finder, potential_contact_txt)
  phone_numbers = list(set(phone_numbers))
  phone_numbers.sort(key=filter_phone_number)
  phone_list = ''
  for numbers in phone_numbers:
    phone_list +=f"{str(numbers)}\n"

  regex_email_finder = r'[\w.+-]+@[\w-]+\.[\w.-]+'

  emails = re.findall(regex_email_finder, potential_contact_txt)
  emails = list(set(emails))
  emails.sort(key=filter_email)
  email_temp = ''
  for email in emails:
    email_temp +=f"{str(email)}\n"


  with open('automation/phone_numbers.txt','w') as phone_txt:
    phone_txt.write(phone_list)

  with open('automation/emails.txt','w') as email_txt:
    email_txt.write(email_temp)

if __name__ == "__main__":
  
  write_phone_email_info("automation/potential_contacts.txt")